from django.shortcuts import render
from .models import Category, Gallery,Portfolio,PortfolioCategory,Blog,Comment,GalleryCategory,Book,Portfolio_single
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from hitcount.views import HitCountDetailView
from django.core.paginator import Paginator
from .forms import ContactForm
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from .bot import send_message
from django.views.generic.list import ListView

class ContactFormView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        
        name = (form.cleaned_data.get('name'))
        email = (form.cleaned_data.get('email'))
        content = (form.cleaned_data.get('content'))
        text = f"Name : {name}\nEmail : {email}\nContent : {content}"
        send_message(text)


        form.save()
        return super().form_valid(form)


def index_view(request):
 return render(request,'index.html')

def about_view(request):
 return render(request,'about.html')

# def books_view(request):
#  return render(request,'books.html')



class PortfolioListView(ListView):
    model = Portfolio
    # paginate_by = 100  # if pagination is desired
    context_object_name = 'portfolios'
    template_name = "portfolio.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = PortfolioCategory.objects.all()
        return context

# def gallery_view(request):
#  return render(request, 'gallery.html')

class GalleryListView(ListView):
   model = GalleryCategory
   context_object_name = 'gallery'
   template_name = "gallery.html"

class GalleryDetailView(DetailView):
    model = GalleryCategory
    template_name = "single-gallery.html"
    context_object_name = "category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["gallery"] = Gallery.objects.filter(category=context.get('category'))

        return context
    
# def blog_view(request):
#  return render(request, 'blog.html')

class BlogListView(ListView):
    model = Blog
    # paginate_by = 100  # if pagination is desired
    context_object_name = 'blogs'
    template_name = "blog.html"
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog-single.html"
    context_object_name = "blog"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(blog=context.get('blog'))
        context['comments_count'] = Comment.objects.filter(blog=context.get('blog')).count()

        return context


def books_view(request):
    books = Book.objects.all()
    context = {
        "books" : books,
    }
    return render(request, 'books.html',context)