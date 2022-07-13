from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('chat.urls', 'chat'), namespace='chat')),
    # path('api/v1/chat/', include(('chat.urls', 'chat'), namespace='chat')),
]
