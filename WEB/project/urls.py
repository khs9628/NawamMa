from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("NawamMa.urls")),  #기존기능
    path('board/', include("board.urls")), #게시판
    path('member/', include("member.urls")), #기존로그인
    path('accounts/', include('allauth.urls')), #소셜로그인
    ]
    
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)