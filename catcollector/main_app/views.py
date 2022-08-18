from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Cat, CatToy
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'cats/index.html')

def cat_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/all_cats.html', { 'cats': cats})

def cat_show(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/show.html', {'cat': cat})

class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
    success_url = '/cats'
    template_name = 'cats/cat_form.html'

    def form_valid(self, form):
        #commit=false makes sure we don't save to the DB
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/cats') 

class CatUpdate(UpdateView):
    model = Cat
    fields = ['name', 'breed', 'description', 'age']
    template_name = 'cats/cat_form.html'
    
    def form_valid(self, form):
        #commit=false makes sure we don't save to the DB
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/cats/' + str(self.object.pk)) 

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats'
    template_name = 'cats/cat_confirm_delete.html'

def profile(request, username):
    user = User.objects.get(username=username)
    cats = Cat.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'cats': cats})

#######CatToy Views########
class CatToyCreate(CreateView):
    model = CatToy
    fields = '__all__'
    success_url = '/cattoys'
    template_name = 'cat_toys/cattoy_form.html'

    def form_valid(self, form):
        #commit=false makes sure we don't save to the DB
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/cattoys') 

class CatToyUpdate(UpdateView):
    model = CatToy
    fields = ['name', 'color']
    template_name = 'cat_toys/cattoy_form.html'
    
    def form_valid(self, form):
        #commit=false makes sure we don't save to the DB
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/cattoys/' + str(self.object.pk)) 

class CatToyDelete(DeleteView):
    model = CatToy
    success_url = '/cattoys'
    template_name = 'cat_toys/cattoy_confirm_delete.html'

# Add these CatToy View functions

def cattoys_index(request):
    cattoys = CatToy.objects.all()
    return render(request, 'cat_toys/index.html', { 'cattoys': cattoys })

def cattoys_detail(request, cattoy_id):
    cattoy = CatToy.objects.get(id=cattoy_id)
    return render(request, 'cat_toys/detail.html', { 'cattoy': cattoy })