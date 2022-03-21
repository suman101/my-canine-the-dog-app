from django.contrib import admin
from .models import Post,Comment,Like,Message,PetProfile,Breed,Training,TrainingCategory

# Register your models here.


class BreedAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']



admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Message)
admin.site.register(PetProfile)
admin.site.register(Breed,BreedAdmin)
admin.site.register(Training)
admin.site.register(TrainingCategory)
