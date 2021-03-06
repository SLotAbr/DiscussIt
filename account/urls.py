from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
	# post views
	# path('login/', views.user_login, name='login'),
	path('login/', auth_views.LoginView.as_view(), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('', views.dashboard, name='dashboard'),

	# change password urls
	path('password_change/',
		 auth_views.PasswordChangeView.as_view(),
		 name='password_change'),
	path('password_change/done/',
		 auth_views.PasswordChangeDoneView.as_view(),
		 name='password_change_done'),

	path('register/', views.register, name='register'),

	path('posts/', views.post_list, name='post_list'),
	path('posts/<int:year>/<int:month>/<int:day>/<slug:post>/',
		  views.post_detail,
		  name='post_detail'),
]