from django.urls import path
from . import views

urlpatterns = [
    path('musicians/', views.MusicianListView.as_view()),
    path('musicians/<int:pk>/', views.MusicianView.as_view()),
    path(
        'musicians/<int:musician_pk>/albums/',
        views.AlbumList.as_view()
        ),
    path(
        'musicians/<int:musician_pk>/albums/<int:album_pk>',
        views.AlbumDetail.as_view()
        ),
    path(
        'musicians/<int:musician_pk>/albums/<int:album_pk>/songs',
        views.SongList.as_view()
        ),
    path(
        'musicians/<int:musician_pk>/' +
        'albums/<int:album_pk>/songs/<int:song_pk>',
        views.SongDetail.as_view()
        )
]
