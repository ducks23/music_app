from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter




urlpatterns = [
    path('musicians/', views.MusicianListView.as_view()),
    path('musicians/<int:pk>/', views.MusicianView.as_view()),
    path('songs/', views.SongListView.as_view()),
    path('songs/<int:pk>/', views.SongView.as_view()),
    path('musicians/<int:musician_pk>/albums/', views.AlbumList.as_view()),
    path('musicians/<int:musician_pk>/albums/<int:album_pk>', views.AlbumDetail.as_view(), name='album-detail'),
    path('musicians/<int:musician_pk>/albums/<int:album_pk>/songs', views.SongList.as_view(), name='song-list'),
    path('musicians/<int:musician_pk>/albums/<int:album_pk>/songs/<int:song_pk>', views.SongDetail.as_view(), name='song-list'),

    #change to viewset
    ]


