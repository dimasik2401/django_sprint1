from django.contrib import admin

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls'), name='pages'),
    path('', include('blog.urls'), name='blog')
]
