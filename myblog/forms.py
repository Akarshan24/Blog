from django import forms
from .models import Post,Category
arr = Category.objects.all().values_list('name','name')
choices = []
for item in arr:
    choices.append(item)
class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title','author','category','body')
        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Blog Title'}),
            'author':forms.TextInput(attrs={'class':'form-control','value':'','id':'author', 'type':'hidden'}),
            'category': forms.Select(choices = choices,attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Blog Text'})
        }
class EditForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title','category','body')
        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control'}),            
            'category': forms.Select(choices = choices,attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'})
        }
class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ('name',)
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),    
        }
