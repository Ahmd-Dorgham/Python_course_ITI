from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Cast(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True, help_text="zay el batal kda")

    def __str__(self):
        return self.name

class ProductionBase(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    release_date = models.DateField(null=True, blank=True)
    
    categories = models.ManyToManyField(Category, related_name="%(class)ss")
    casts = models.ManyToManyField(Cast, related_name="%(class)ss")
    
    poster_image = models.URLField(max_length=500, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class Movie(ProductionBase):
    pass

class Series(ProductionBase):
    pass