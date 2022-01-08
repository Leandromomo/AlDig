from django.urls import path
from Valsinaapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include




urlpatterns = [

    path('',views.home, name="Home"),
    
    path('accounts/', include('django.contrib.auth.urls')),

    path('registro/', include ('login.urls')),
   
] 

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)