from django.contrib import admin
from django.urls import include, path
from blog.views import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls')),
    path('', include('blog.urls')),
]

handler404 = handler404
handler500 = handler500
