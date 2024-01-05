from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("core.urls", namespace='core')),
    path('cart/', include("cart.urls", namespace ='cart')),
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # unique url path for images coming to media from outside ? uniqe url path for images


#or u can just append it to the list via :
# urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  