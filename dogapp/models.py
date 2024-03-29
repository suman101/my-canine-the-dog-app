from django.db import models
from django.core.validators import FileExtensionValidator
from authentication.models import User
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    caption = models.TextField()
    image = models.ImageField(upload_to = 'images/')
    pet_name = models.CharField(max_length=50,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('created',)

    def __str__(self): 
        return self.pet_name
    
class Comment(models.Model):
    comment = models.TextField(max_length=254, blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=100,null=True,blank=True)
    
    class Meta: 
        ordering = ('created',) 
        
    def __str__(self): 
        return self.user.username  
    
class Like(models.Model):
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete= models.CASCADE)
    
    
class Message(models.Model):
    text = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')
    senderId = models.ForeignKey(User, on_delete=models.CASCADE,related_name='sender_id')
    receiverId = models.ForeignKey(User, on_delete=models.CASCADE,related_name='receiver_id')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.text}'
        
    
class Breed(models.Model):
    title = models.CharField(max_length=55)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images/',null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='breed_user',default=None)
    
    def __str__(self):
        return self.title
    
class PetProfile(models.Model):
    name = models.CharField(max_length=45)
    date_of_birth = models.DateField(default=None)
    adult = models.BooleanField(default=False)
    address = models.CharField(max_length=55)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None,related_name='pet_user')
    pet_bio = models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name


    def is_adult(self):
        import datetime
        if (datetime.date.today() - self.date_of_birth) > datetime.timedelta(days=18*365):
            self.adult = True

    def save(self, *args, **kwargs):
        self.is_adult()
        super(PetProfile, self).save(*args, **kwargs)

     

class TrainingCategory(models.Model):
        title = models.CharField(max_length=100)
        image = models.ImageField(upload_to= 'category_upload/',null=True)
        days = models.IntegerField(null=True,blank=True)

        def __str__(self):
            return self.title
    
class Training(models.Model):
    title = models.CharField(max_length=85)
    description = models.TextField()
    video = models.FileField(upload_to='videos_uploaded',null=True,blank=True,
            validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    image = models.ImageField(upload_to = 'images_uploaded/', null = True)
    category = models.ForeignKey(TrainingCategory,on_delete=models.CASCADE,related_name='category')
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    breed = models.ManyToManyField(Breed)
    age_limit = models.CharField(max_length=2,null=True,blank=True)
    
    def __str__(self):
        return self.title

    
        
    
class Transaction(models.Model):
    price= models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    address = models.CharField(max_length=55)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=14)
    
    def __str__(self):
        return self.price
    
    

    
    
    
    