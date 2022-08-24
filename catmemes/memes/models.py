from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Meme(models.Model):
    title = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='pictures/%Y_%m/')
    slug = models.SlugField()
    author = models.ForeignKey(
        User, 
        blank=True, 
        null=True, 
        on_delete=models.SET_NULL
        )

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, set slug
            self.slug = slugify(self.title)

        super(Meme, self).save(*args, **kwargs)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Meme, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    text = models.TextField(max_length=400)