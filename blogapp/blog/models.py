from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null = False, blank=True, unique=True, db_index=True, editable=False)

    def save(self, *args, **kwargs): #overwrite
        self.slug = slugify(self.name)
        super().save(*args, **kwargs )


    def __str__(self):
        return f"{self.name}"

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blogs")
    # description = models.TextField() 
    description = RichTextField() # it was models.TextField() before. Changed it.
    is_active = models.BooleanField(default = False)
    is_home = models.BooleanField(default = False)
    slug = models.SlugField(null = False, blank=True, unique=True, db_index=True, editable=False)

    ## ONE to MANY relation ##
    # category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    # category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL) #if we delete related category, the blogs will be assigned to null; otherwise, with CASCADE the blogs would've been deleted as well if we delete related category.
    # category = models.ForeignKey(Category, default=1, on_delete=models.SET_DEFAULT)

    ## MANY to MANY relation
    categories = models.ManyToManyField(Category, blank = True)
        # blank is True means that we do not supposed to choose one of categories we have


    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs): #overwrite
        self.slug = slugify(self.title)
        super().save(*args, **kwargs )

