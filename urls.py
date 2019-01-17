from django.urls import path

from . import views

app_name = "cuba"

urlpatterns = [
    path('', views.TopView.as_view(), name='index'),
    path('blog/', views.IndexView.as_view(), name='blog'),
    path('blog/<int:pk>', views.CategoryView.as_view(), name='category'),
    path('about/', views.about, name='about'),
    path('blog/detail/<int:pk>/', views.DetailAndCreateView.as_view(), name='detail'),

]

