from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter




urlpatterns = [
    path('musicians/', views.MusicianListView.as_view()),
    path('musicians/<int:pk>/', views.MusicianView.as_view()),
    path('albums/', views.AlbumListView.as_view()),
    path('albums/<int:pk>/', views.AlbumView.as_view()),
    path('songs/', views.SongListView.as_view()),
    path('songs/<int:pk>/', views.SongView.as_view()),
    path('musicians/<int:pk>/albums/', views.AlbumListView.as_view()),
    path('musicians/<int:musician_pk>/albums/<int:album_pk>', views.album_detail, name='album-detail'),

    #change to viewset
    ]


