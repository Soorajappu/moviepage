from django.shortcuts import render,redirect,get_object_or_404
from .models import Movie, Director
from .forms import MovieForm, DirectorForm
# Create your views here.

def moviepage(request):
    return render(request,'index.html')


def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showlist')
    else:
        form = MovieForm()
    return render(request, 'createmovie.html', {'form': form})

def director_create(request):
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('director_list')
    else:
        form = DirectorForm()
    return render(request, 'createdir.html', {'form': form})

def showlist(request):
    movies = Movie.objects.all()
    return render(request, 'list.html', {'movies': movies})

def director_list(request):
    directors = Director.objects.all()
    return render(request, 'director_list.html', {'directors': directors})

def movie_edit(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('showlist')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'createmovie.html', {'form': form})

def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('showlist')
    return render(request, 'deletemovie.html', {'movie': movie})