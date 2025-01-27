from django.db import models

# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=100, unique=True, primary_key=True)
    #related_tags = models.ManyToManyField(Tag, blank=True, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True, primary_key=True)


class Post(models.Model):
    author = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    template_name = models.CharField(max_length=500)
    slug = models.SlugField(unique=True)
    tags = models.ManyToManyField(Tag, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    # image associated with the post

    def get_template_name(self):
        return "post/%s" % self.template_name

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail-post", kwargs={"slug": self.slug})
