"""palindrome_game_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from palindrome_game_app import views

urlpatterns = [
    path('',views.home),
    # path('admin/', admin.site.urls),
    path('create_user/', views.create_user, name='create_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('update_user/<int:user_id>/', views.update_user, name='update_user'),
    path('user_login/', views.user_login, name='user_login'),
    path('start_game/', views.start_game, name='start_game'),
    path('get_board/<str:game_id>/', views.get_board, name='get_board'),
    path('update_board/<str:game_id>/', views.update_board, name='update_board'),
]
