from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from task3.views import main, second, third

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('second/', second),
    path('third/', third),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
