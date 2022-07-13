from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Message, Members

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from .serializers import MessageSerializer
from .permissions import IsOwnerOrReadOnly


class MessageViewSet(generics.CreateAPIView):
    serializer_class = MessageSerializer


class MessagesListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all().order_by('room')
    permission_classes = (IsAdminUser,)


class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all().order_by('room')
    permission_classes = (IsOwnerOrReadOnly,)


@login_required
def index(request):
    auth_id = request.user.id
    members = Members.objects.filter(user_id=auth_id)
    return render(request, 'main/main.html', {'members': members})


@login_required
def room(request, group_id):
    username = request.user.username
    messages = Message.objects.filter(room=group_id)[0:25]
    return render(request, 'chat/room.html', {'room_name': group_id, 'username': username, 'messages': messages})
