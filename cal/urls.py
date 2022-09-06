from django.urls import path
from . import views

app_name = 'cal'
urlpatterns = [
    path('^index/$', views.index, name='index'),
    path('', views.CalendarView.as_view(), name='calendar'),
    path('^event/new/$', views.event, name='event_new'),
	path('event/info/<str:pk>/', views.info_event, name='event_info'),
    path('event/info/<str:pk>/delete/', views.delete_event, name="event_delete"),
]
