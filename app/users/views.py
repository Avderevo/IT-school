from django.views.generic import View, TemplateView
from django.contrib.auth.tokens import default_token_generator as dtg
from django.contrib.auth.views import PasswordResetConfirmView, LogoutView
from .models import Activation
from django.contrib.auth import login
from django.shortcuts import get_object_or_404, redirect
from .mail_sender import send_confirm_email, send_reset_password_email
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from app import settings



class UserCreate(View):

    def post(self, request, *args, **kwargs):
        data = dict()
        form = request.POST
        if User.objects.filter(email__iexact=form["email"]).exists():
            data['form_is_valid'] = False
        else:
            user = User(
                username=form["username"],
                email=form['email'])
            user.set_password(form["password"])
            user.save()
            if settings.USER_EMAIL_ACTIVATION:
                user.is_active = False
                code = dtg.make_token(user)
                act = Activation()
                act.code = code
                act.user = user
                act.save()
                data['form_is_valid'] = True
                send_confirm_email(request, user.email, code)
            else:
                user.is_active = True
                data['form_is_valid'] = True

        return JsonResponse(data)

    def get(self, request):
        data = dict()
        data['html_form'] = render_to_string(
            'users/create.html', request=request
        )
        return JsonResponse(data)


class LogView(View):

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()

        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = dict()
        form = request.POST
        user = User.objects.filter(email=form['email']).first()

        if not user:
            data['form_is_valid'] = False

        if not user.is_active:
            data['form_is_valid'] = False

        if not user.check_password(form['password']):
            data['form_is_valid'] = False
#            raise ValidationError(('You entered an invalid password.'))

        else:
            data['form_is_valid'] = True
            login(request, user)
            

#            data['users'] = render_to_string(
#                'users_list.html', {'users': users})

        return JsonResponse(data)


class RemindPasswordView(View):

    def post(self, request, *args, **kwargs):
        data = dict()
        email = request.POST['email']
        user = User.objects.filter(email__iexact=email).first()
        if not user:
            data['form_is_valid'] = False
        if not user.is_active:
            data['form_is_valid'] = False
        else:
            token = dtg.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk)).decode()
#            act = Activation()
#            act.code = code
#            act.user = user
#            act.save()
            send_reset_password_email(self.request, user.email, token, uid)
            data['form_is_valid'] = True
       # user = User.objects.all()
       # data['users'] = render_to_string('users_list.html', {'users': user})

        return JsonResponse(data)

    def get(self, request):
        data = dict()
        data['html_form'] = render_to_string(
            'users/remind_password.html', request=request
        )
        return JsonResponse(data)


class RestorePasswordConfirmView(PasswordResetConfirmView):
    template_name = 'users/restore_password.html'

    def form_valid(self, form):
        # Изменить пароль
        form.save()

        messages.success(self.request, (
            'Ваш пароль установлен. Вы можете войти сейчас.'))

        return redirect('index')


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


class LogoutView(LogoutView):
    next_page = "index"


