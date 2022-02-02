from django.contrib import admin
from .models import signup

# Register your models here.


@admin.register(signup)
class signupAdmin(admin.ModelAdmin):
    list_displays=('firstname','lastname','mobile','email',
                    'password','Confirmpassword')
