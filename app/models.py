from django.db import models

class Basemodel(models.Model): 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Product_Images(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=255)
    def __str__(self):
        return self.image.url




class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Seller(Basemodel):
  name=models.CharField(max_length=255)
  image=models.ImageField(upload_to='images/')
  is_active=models.BooleanField(default=False)
  background_image=models.ImageField(upload_to='images/')
  last_active_datetime = models.DateTimeField()
  def __str__(self):
        return self.name
  
class Products(Basemodel):
    class moderation(models.TextChoices):
        tasdqilangan = 'tasdqilangan', 'tasdqilangan'   
        tasdiqlanmagan = 'tasdiqlanmagan', 'tasdiqlanmagan'
        jarayonda = 'jarayonda', 'jarayonda'

    name = models.CharField(max_length=255)
    views_count = models.IntegerField()
    description = models.TextField()
    betlar_soni=models.IntegerField()
    hajmi=models.FloatField()
    type=models.CharField(max_length=255)
    images = models.ManyToManyRel(Product_Images,to='Product_Images',related_name='images')
    price = models.DecimalField(max_digits=10)
    moderatsiya=models.CharField(max_length=200,choices=moderation.choices,default=moderation.jarayonda)
    seller=models.ForeignKey(Seller,on_delete=models.CASCADE)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
  