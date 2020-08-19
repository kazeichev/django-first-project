from django.urls import path

from django_first_project.calc import views

urlpatterns = [
    path('<int:a>/<int:b>', views.IndexView.as_view(), name='calc'),
    path('history/', views.HistoryView.as_view(), name='calc'),
]