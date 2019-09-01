from django.urls import path
from . import views

app_name = "board"

urlpatterns = [
    path("boardlist/", views.boardlist, name='boardlist'),
    path('create/', views.create, name='create'),
    path('newboard/', views.boardform, name='newboard'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('remove/<int:pk>', views.remove, name='remove'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('detail/<int:board_id>/<int:comment_id>', views.comment_delete, name='comment_delete'),
    ##모바일뷰
    path('Mboard/', views.Mboard , name ='Mboard'),
]