from django.urls import path

from school.views import AllCursesListView

app_name = 'school'

urlpatterns = [
    path('curses/', AllCursesListView.as_view(), name='all_curses'),
    path('calendar/<year>', AllCursesListView.as_view(), name='calendar'),
   
]