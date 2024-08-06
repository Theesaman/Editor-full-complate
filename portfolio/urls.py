from django.urls import path
from .views import index_view,books_view,PortfolioListView,about_view,GalleryListView,BlogListView,ContactFormView,BlogDetailView,GalleryDetailView

urlpatterns = [
    path('',index_view,name='index-page'),
    path('contact/',ContactFormView.as_view(),name='contact-page'),
    path('books/',books_view,name='books-page'),
    path('portfolio/',PortfolioListView.as_view(),name='portfolio-page'),
    path('about/',about_view,name='about-page'),
    path('gallery/',GalleryListView.as_view(),name='gallery-page'),
    path('blog/',BlogListView.as_view(),name='blog-page'),
    path('blog/<int:pk>',BlogDetailView.as_view(),name="blog-single-page"),
    path('gallery/<int:pk>',GalleryDetailView.as_view(),name="gallery-single-page"),
    path('portfolio/',PortfolioListView.as_view(),name='portfolio-page'),

]
