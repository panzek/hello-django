from django.contrib import admin
from .models import Item

# Register your models here.
admin.site.register(Item)

# To Expose Items Table
# "from .models import Item": this says from the current directory’s models file we want to import the item class. 
# We use the "admin.site.register" function to actually register our item model. 
# Save it and run our project in the terminal: "python manage.py runserver"
