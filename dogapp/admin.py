from django.contrib import admin
from .models import Post,Comment,Like,Message,PetProfile,Breed,Training,Category
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Message)
admin.site.register(PetProfile)
admin.site.register(Breed)
admin.site.register(Training)
admin.site.register(Category)
