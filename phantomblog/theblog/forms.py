from django import forms
from .models import Post, Category

class PostForm(forms.ModelForm):
    new_category = forms.CharField(required=False, help_text="Enter a new category if not listed.")

    class Meta:
        model = Post
        fields = ('title', 'slug', 'title_tag', 'author', 'img', 'status', 'content', 'category')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        new_category = self.cleaned_data['new_category']

        if new_category and new_category.strip():
            category, created = Category.objects.get_or_create(name=new_category)
            instance.category = category

        instance.save()
        return instance

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),}

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'title_tag', 'img', 'status', 'content', 'category')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }