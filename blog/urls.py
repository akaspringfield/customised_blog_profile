from django.urls import path    #default value
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.all_blogs, name='all_blog'),
    path('<int:blog_id>/',views.detail, name='detail'),
]
