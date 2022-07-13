from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views


app_name = 'chat'
urlpatterns = [
    path('message/create/', views.MessageViewSet.as_view()),
    path('message/all/', views.MessagesListView.as_view()),
    path('message/detail/<int:pk>', views.MessageDetailView.as_view()),

    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('main/', views.index, name='index'),
    path('main/room/<str:group_id>/', views.room, name='room'),
]
