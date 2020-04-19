from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.forms.widgets import RadioSelect
from cloudinary.models import CloudinaryField


class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50,default="")
    desc=models.CharField(max_length=300,default="")
    catrgory=models.CharField(max_length=50,default="")
    sub_category=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    pub_date=models.DateField(auto_now_add=True)
    image=models.ImageField(upload_to="game/images",default="")
    likes = models.ManyToManyField(User,related_name='likes',blank=True)
    favs =  models.ManyToManyField(User,related_name='favs',blank=True)
    
    def __str__(self):
        return self.product_name

    
    def total_likes(self):
        return self.likes.count()
    
    def get_absolute_url(self):
        return reverse("detailproduct",args=[self.id])





class Profile(models.Model):
    CHOICES=[('Male','Male'),
        ('Female','Female'),
        ('Other','Other')]
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,blank=True)
    last_name = models.CharField(max_length=100,blank=True)
    email = models.EmailField(max_length=150)
    address1=models.CharField(max_length=250,default="")
    address2=models.CharField(max_length=250,default="")
    city=models.CharField(max_length=100,default="")
    state=models.CharField(max_length=100,default="")
    gender=models.CharField(max_length=11,choices=CHOICES,blank=True)
    pin=models.CharField(max_length=15,default="")
    country=models.CharField(max_length=50,default="")
    mobileno=models.CharField(max_length=12,default=0)





    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)




class Item(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Color(models.Model):
    item=models.ForeignKey(Item,on_delete=models.CASCADE)   
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Size(models.Model):
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Design(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    price=models.PositiveIntegerField(null=True)
    item=models.ForeignKey(Item,on_delete=models.SET_NULL,null=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL,null=True)
    size = models.ForeignKey(Size, on_delete=models.SET_NULL,null=True)
    title=models.CharField("Title",max_length=200,blank=True)

    image=CloudinaryField('image',blank=True)

    def __str__(self):
        order_id="2020001"+str(self.pk)
        return order_id

    def __unicode__(self):
        try:
            public_id=self.image.public_id
        except AttributeError:
            public_id = ''
        return "Photo name <%s:%s>" %(self.title,public_id)

