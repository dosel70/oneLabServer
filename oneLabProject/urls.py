from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('member/', include('member.urls')),
    path('accounts/', include('allauth.urls')),
    path('oauth/', include('oauth.urls')),
    path('onelab/', include('onelab.urls')),
    path('community/', include('community.urls')),
    # path('myPage/', include('myPage.urls')),
    # path('point/', include('point.urls')),
    path('alarm/', include('alarm.urls')),
    path('replies/', include('reply.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)