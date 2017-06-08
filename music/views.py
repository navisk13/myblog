# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, CreateView, DetailView

from music.models import Album, Song


class AlbumListView(ListView):
    model = Album
    # template_name = "album_list.html"


class AlbumCreateView(CreateView):
    model = Album
    fields = ['album_name', 'album_img', 'album_genre']
    success_url = '/music/'


class AlbumDetailView(DetailView):
    model = Album

    def get_context_data(self, **kwargs):
        context = super(AlbumDetailView, self).get_context_data(**kwargs)
        songs = Song.objects.filter(album=context['object'])
        context["songs"] = songs
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        artist = request.POST['artist']
        album = Album.objects.get(id=self.kwargs['pk'])
        song = Song(name=name, artist=artist, album=album)
        song.save()
        return redirect('album_detail', album.id)




