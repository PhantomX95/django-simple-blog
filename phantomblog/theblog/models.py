from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field

# Category model
class Category(models.Model):
    name = models.CharField(max_length=100 , unique=True, blank=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    
    # Meta class to rename the plural name of the model
    class Meta:
        verbose_name_plural = "categories"

    # Automatically generate the slug if not provided
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

STATUS = (
    (0,"Draft"),
    (1,"Pending"),
    (2,"Published"),
)

# Post model
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    title_tag = models.CharField(max_length=255, null=True, blank=True)
    content = CKEditor5Field(config_name='extends')
    snippet = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=1)
    img = models.ImageField(upload_to='photos/%Y/%m/%d/', default='photos/no-image.png')
    # You have to create the first category as 'Uncategorized' so it has ID 1
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=1)

    def save(self, *args, **kwargs):
        # Automatically generate the title_tag if not provided
        if not self.title_tag:
            self.title_tag = self.title

        # If slug is not provided, generate it from the title
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)
    
    def __str__(self):
        full_name = str(self.author.first_name) + ' ' + str(self.author.last_name)
        return f"{self.title} | {full_name if full_name else self.author.username}"

    # Redirect to the detail page of the post after creating a new post
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"category_slug": self.category.slug, "slug": self.slug})
