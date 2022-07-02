from . import views
from django.urls import path, url

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    url(r'^about/$', views.about, name='about'),
]