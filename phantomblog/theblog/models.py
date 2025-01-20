from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

# Category model
class Category(models.Model):
    name = models.CharField(max_length=100 , unique=True, blank=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    
    # Meta class to provide a human-readable name for the model
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
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=1)
    img = models.ImageField(upload_to='photos/%Y/%m/%d/', default='photos/no-image.png', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=1)  # Assuming 'Uncategorized' has ID 1

    def save(self, *args, **kwargs):
        # Automatically generate the title_tag if not provided
        if not self.title_tag:
            self.title_tag = self.title

        # If slug is not provided, generate it from the title
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)
    
    def __str__(self):
        full_name = f"{str(self.author.first_name)} {str(self.author.last_name)}".strip()
        return f"{self.title} | {full_name if full_name else self.author.username}"

    # Redirect to the detail page of the post after creating a new post
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"category_slug": self.category.slug, "slug": self.slug})
