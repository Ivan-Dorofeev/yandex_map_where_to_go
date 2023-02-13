from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from where_to_go import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('__debug__/', include('debug_toolbar.urls')),

    path('', views.main, name='main'),
    path('places/', include('places.urls'))
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)