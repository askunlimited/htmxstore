from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    
    class Meta:
      ordering = ('name',)

    def __str__(self):
        return self.name
      


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField(upload_to='products', null=True, blank=True)


    class Meta:
      ordering = ('-date_created',)
      
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
      
    