from django.urls import path
from .import views

urlpatterns = [
    
    path('home',views.home,name='home'),
    path('detail/<int:id>',views.post_detail,name='detail'),
]

