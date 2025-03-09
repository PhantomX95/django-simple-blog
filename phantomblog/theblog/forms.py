from django import forms
from .models import Post, Category, Comment

class PostForm(forms.ModelForm):
    new_category = forms.CharField(
        required=False,
        help_text="Create a new category if not listed.",
        widget= forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'New Category'}),
        label=''
        )

    class Meta:
        model = Post
        fields = ('title', 'slug', 'title_tag', 'img', 'content', 'snippet', 'category')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder': 'Title', 'required': ''}),
            'slug': forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder': 'Slug'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder': 'Title Tag'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control mb-4', 'placeholder': 'Snippet Text', 'rows': '2', 'required': ''}),
            'category': forms.Select(attrs={'class': 'form-control mb-4'}),
            'img': forms.FileInput(attrs={'class': 'form-control mb-4', 'type': 'file', 'accept': 'image/*', 'required': ''}),
        }
        labels = {
            'title': '',
            'slug': '',
            'title_tag': '',
            'snippet': '',
            'category': '',
            'img': '',
            'content': '',
        }
    
    # Save the new category if provided
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
    new_category = forms.CharField(
    required=False,
    help_text="Create a new category if not listed.",
    widget= forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'New Category'}),
    label=''
    )

    class Meta:
        model = Post
        fields = ('title', 'slug', 'title_tag', 'img', 'content', 'snippet', 'category')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-4', 'required': ''}),
            'slug': forms.TextInput(attrs={'class': 'form-control mb-4'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control mb-4'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control mb-4', 'rows': '2', 'required': ''}),
            'img': forms.FileInput(attrs={'class': 'form-control mb-4', 'type': 'file', 'accept': 'image/*', 'required': ''}),
            'category': forms.Select(attrs={'class': 'form-control mb-4'}),
        }

        labels = {
            'title': '',
            'slug': '',
            'title_tag': '',
            'snippet': '',
            'category': '',
            'img': '',
            'content': '',
        }

    # Save the new category if provided
    def save(self, commit=True):
        instance = super().save(commit=False)
        new_category = self.cleaned_data['new_category']

        if new_category and new_category.strip():
            category, created = Category.objects.get_or_create(name=new_category)
            instance.category = category

        instance.save()
        return instance
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = ({'body': '',})
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 1, 'placeholder': 'Write Your Comment...'}),
        }

# Search form
class SearchForm(forms.Form):
    search = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search...',
            'aria-describedby': 'button-addon2',
            }
        )
    )

