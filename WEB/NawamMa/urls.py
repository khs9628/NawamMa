from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "NawamMa"

urlpatterns = [
    path("", views.layout, name='home'),
    path("mypage/", views.mypage, name='mypage'),

    #만든이 소개
    path('maker/', views.maker , name ='maker'),
    path('extend/', views.extend , name ='extend'),
    #출발/목적지 입력
    path('start/', views.start, name = 'start'),
    path('startP/', views.startP, name = 'startP'),
    #지하철 혼잡도
    path('subway/', views.subway, name = 'subway'),
    path('subwayP/', views.subwayP, name = 'subwayP'),
    #좌석관련
    path('seat/<int:number>/', views.seat , name ='seat'),
    path('preRequset/', views.preRequset , name ='preRequset'),
    path('seatP/<int:number>/', views.seatP , name ='seatP'),
    path('MseatP/', views.MseatP, name = 'MseatP'),
    path('Mseat/', views.Mseat, name = 'Mseat'),
]
