from django.urls import path

from school.views import AllCursesListView, CalendarCursesView

app_name = 'school'

urlpatterns = [
    path('courses/', AllCursesListView.as_view(), name='all_courses'),
    path('calendar/<year>', CalendarCursesView.as_view(), name='calendar'),
   
]