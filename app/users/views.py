from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.utils.http import is_safe_url
from django.views.generic import View, FormView, ListView, TemplateView, UpdateView
from django.contrib.auth import login, authenticate, REDIRECT_FIELD_NAME
from .form_users import SignupForm, LoginForm, UserForm
from django.contrib.auth.tokens import default_token_generator as dtg
from .models import Activation, MyUser
from django.shortcuts import get_object_or_404, redirect, HttpResponseRedirect
from .mail_sender import send_confirm_email
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.decorators import method_decorator
from app import settings
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from django.template.loader import render_to_string


class SignUpView(FormView):
    template_name = 'users/sign.html'
    form_class = SignupForm

    def form_valid(self, form):
        request = self.request
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        code = dtg.make_token(user)
        act = Activation()
        act.code = code
        act.user = user
        act.save()

        send_confirm_email(request, user.email, code)
        messages.success(
                request, (
                    'You are signed up. To activate the account,\
                     follow the link sent to the mail.'))

        return redirect('/users/thanks/')


class ConfirmView(View):
    @staticmethod
    def get(request, code):
        act = get_object_or_404(Activation, code=code)
        user = act.user
        if user and dtg.check_token(user, code):
            user.is_active = True
            user.save()
            act.delete()
            return redirect('index')


class LoginView(FormView):
    template_name = 'users/forget.html'
    form_class = LoginForm

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        request = self.request
        login(request, form.user_cache)

        redirect_to = request.POST.get(REDIRECT_FIELD_NAME, request.GET.get(REDIRECT_FIELD_NAME))
        url_is_safe = is_safe_url(redirect_to, allowed_hosts=request.get_host(), require_https=request.is_secure())

        if url_is_safe:
            return redirect(redirect_to)

        return redirect(settings.LOGIN_REDIRECT_URL)


def thanks(request):
    return render(request, 'users/thanks.html')


class IndexView(TemplateView):

    template_name = "users/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = MyUser.objects.all()
        return context



class UserCreate(View):

    def post(self, request, *args, **kwargs):
        data = dict()
        form = request.POST

        if User.objects.filter(email__iexact=form["email"]).exists():
            data['form_is_valid'] = False
        else:
            user = User(
                username=form["username"],
                email=form['email'], password=form['pass_confirmation'])
            user.is_active = False
#           user.save()

#           code = dtg.make_token(user)
#           act = Activation()
#           act.code = code
#           act.user = user
#           act.save()
            data['form_is_valid'] = True
#        send_confirm_email(request, user.email, code)
#            messages.success(
 #                   request, (
 #                       'You are signed up. To activate the account,\
 #                        follow the link sent to the mail.'))

        data['users'] = render_to_string('users_list.html', {'users': user.username})
       
        return JsonResponse(data)


    def get(self, request):
        data = dict()
        data['html_form'] = render_to_string('users/create.html',
           request=request
        )
        return JsonResponse(data)





class LogView(View):
 
    def post(self, request, *args, **kwargs):
        data = dict()
        use = request.POST
#        if form.is_valid():
#            form.save()
        data['form_is_valid'] = True
#            users = MyUser.objects.all()
        users = use['password']

        data['users'] = render_to_string('users_list.html', {'users': users})
#        else:
#            data['form_is_valid'] = False
        return JsonResponse(data)

 #    @method_decorator(ensure_csrf_cookie)
 #    def get(self, request):
 #        form = UserForm()
 #        data = dict()
 #        context = {'form': form, "button": 'создать'}
 #        data['html_form'] = render_to_string('users/create.html',
 #           request=request
 #        )
 #        return JsonResponse(data)



class RemindView(View):

    def post(self, request, *args, **kwargs):
        data = dict()
        use = request.POST
#        if form.is_valid():
#            form.save()
        data['form_is_valid'] = True
#            users = MyUser.objects.all()
        name = use["email"]

        data['users'] = render_to_string('users_list.html', {'users': name})
#        else:
#            data['form_is_valid'] = False
        return JsonResponse(data)

