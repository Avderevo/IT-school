from django.views.generic import TemplateView, View


class IndexPageView(TemplateView):
    template_name = 'index/index.html'


class AllCursesListView(TemplateView):
    template_name = 'school/all_curses_list.html'


