# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Album
from .forms import AlbumForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# views.py


def home_page(request):
    return render(request, 'albums/base.html')


@login_required
def album_list(request):
    albums = Album.objects.filter(user=request.user)
    return render(request, 'albums/album_list.html', {'albums': albums})


@login_required
def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.user = request.user
            album.save()
            return redirect('album_list')
    else:
        form = AlbumForm()
    return render(request, 'albums/album_form.html', {'form': form})


@login_required
def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    other_albums = album.artist.albums.exclude(pk=album.pk)
    context = {
        'album': album,
        'other_albums': other_albums,
    }

    return render(request, 'albums/album_detail.html', context)


@login_required
def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)

    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    else:
        form = AlbumForm(instance=album)

    return render(request, 'albums/album_form.html', {'form': form})


@login_required
def favorite_album(request, pk):
    user = get_object_or_404(User, pk=pk)
    album = get_object_or_404(Album, pk=pk)

    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=favorite)
        if form.is_valid():
            breakpoint
            form.save()
            return redirect('album_list')
    else:
        form = AlbumForm(instance=album)

    return render(request, 'albums/album_form.html', {'form': form})
    # user.favorites


@login_required
def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)

    if request.method == 'POST':
        album.delete()
        return redirect('album_list')
    return render(request, 'albums/album_confirm_delete.html', {'album': album})