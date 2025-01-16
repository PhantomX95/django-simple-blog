from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

STATUS = (
    (0,"Draft"),
    (1,"Pending"),
    (2,"Published"),
)

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

    def get_absolute_url(self):
        return reverse("home")
