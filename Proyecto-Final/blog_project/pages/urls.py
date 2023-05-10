from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('pages/', views.pages, name='pages'),
    path('pages/<int:page_id>/', views.page_detail, name='page_detail'),
]
