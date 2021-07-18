from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Category
from .forms import PostForm,EditForm,CategoryForm
from django.urls import reverse_lazy
# def home(request):
#     return render(request,'home.html',{})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    def get_context_data(self,*args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context
    
class BlogView(DetailView):
    model = Post
    template_name = 'blog_detail.html'
    def get_context_data(self,*args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(BlogView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context
class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'
    success_url = reverse_lazy('home')
    #fields = '__all__'
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    success_url = reverse_lazy('home')
    #fields = ['title','body']
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    #fields = ['title','body']
class CreateCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'create_cat.html'
    success_url = reverse_lazy('edit-cat')
class DeleteCategoryView(DeleteView):
    model = Category
    template_name = 'delete_cat.html'
    success_url = reverse_lazy('edit-cat')
class EditCategoryView(ListView):
    model = Category
    template_name = 'edit_cat.html'
    ordering = ['name']
def CategoryView(request,cat):
    posts = Post.objects.filter(category = cat.replace('-',' '))   
    return render(request,'posts_cat.html',{'cats':cat,'posts':posts})
    # def get_context_data(self,*args, **kwargs):
    #     cat_menu = Category.objects.all()
    #     context = super(CategoryView,self).get_context_data(*args,**kwargs)
    #     context["cat_menu"] = cat_menu
    #     return context