from django.shortcuts import render
from . import models
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
@login_required
def index(request):
    num_books = models.Book.objects.all().count()
    num_book_instance = models.BookInstance.objects.all().count() 
    num_book_avail = models.BookInstance.objects.filter(status__exact='a').count() 
    
    context = {
      'num_books' : num_books,  
      'num_book_instance' : num_book_instance,  
      'num_book_avail' : num_book_avail,  
    }
    
    return render(request , 'index.html' , context)

class CreateBook(LoginRequiredMixin , generic.CreateView):
    model = models.Book
    fields = '__all__'
    template_name = 'create.html'
    
class Register(generic.CreateView):
    form_class = UserCreationForm
    success_url = '/catalog'
    template_name = 'registration/register.html'
    
    
class BookDetail(generic.DeleteView):
    model = models.Book
    template_name = 'detail.html'
    context_object_name = 'books'