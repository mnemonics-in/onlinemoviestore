from django.shortcuts import render
from movieapp.models import Movie

from .forms import Movieform

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView # class based views
from django.urls import reverse_lazy

from django.http import HttpResponse
# Create your views here.
# def index(request):
#     k = Movie.objects.all()
#     return render(request, template_name='index.html', context={'b': k})
class MovieList(ListView): #ListView Displays all objects/records retreiving from a model.
    model=Movie
    template_name = "index.html"
    context_object_name = "b"

class Moviedelete(DeleteView):
    model=Movie
    success_url=reverse_lazy('index')
    template_name="delete.html"

# def addmovie(request):
#     if(request.method=="POST"):
#         moviename=request.POST['moviename']
#         moviedesc=request.POST['moviedesc']
#         movieyear=request.POST['movieyear']
#         movieimage=request.FILES['movieimage']
#         b=Movie.objects.create(moviename=moviename,moviedesp=moviedesc,movieyear=movieyear,movieimage=movieimage)
#         b.save()
#         return index(request)
#     return render(request,template_name='addmovie.html')
# def viewmovie(request,p):
#     b=Movie.objects.get(id=p)
#     return render(request,template_name='viewmovie.html',context={'b':b})

class Movieadd(CreateView):#CreatView displays a form for adding new object and handles form submission.
    model=Movie
    template_name ="addmovie.html"
    fields = '__all__'
    success_url = reverse_lazy('index')



class MovieDetail(DetailView):#DetailView displays a particular objects retrieving from a model.
    model=Movie
    template_name = "viewmovie.html"
    context_object_name = "b"
class Movieupdate(UpdateView):
    model=Movie
    template_name="editmovie.html"
    fields='__all__'
    success_url=reverse_lazy('index')

# def moviedelete(request,p):
#     b=Movie.objects.get(id=p)
#     b.delete()
#     return index(request)

# def movieedit(request,p):
#     b=Movie.objects.get(id=p)
#     if(request.method=="POST"):
#         form = Movieform(request.POST, request.FILES, instance=b)
#         if form.is_valid():
#             form.save()
#         return index(request)
#     form=Movieform(instance=b)
#     return render(request,template_name='editmovie.html',context={'form':form})