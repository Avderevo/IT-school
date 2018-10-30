from django.views.generic import TemplateView, View
from django.shortcuts import render


class IndexPageView(TemplateView):
    template_name = 'index/index.html'


class AllCursesListView(TemplateView):
    template_name = 'school/all_curses_list.html'


class CalendarCursesView(View):
    @staticmethod
    def get(request, year):
        template_name = "school/calendar_{}.html".format(year)
        return render(request, template_name)
