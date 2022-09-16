from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'done']


# Step through the code:
# import "forms" which will allow us to leverage some of the built-in Django form functionality.
# import our "Item" model. Just like when we created the item model itself.

# Our form will be a class that inherits a built-in Django class to give it some basic functionality.
# we call it "ItemForm" and it inherits all the functionality of "forms.ModelForm". 
# To tell the form which model it's going to be associated with, we provide an "inner Meta" class. 
# This inner class gives our form some information about itself such as which fields it should render, 
# how it should display error messages, and so on.

# define our model, which is going to be our item model. 
# define fields which tells it we want to display: the "name" and "done" fields from the model.

# The idea of creating this form in Django is that rather than writing an entire form ourselves in HTML, we can simply render it out as a template variable.
# To make sure we've got it available for use in the template, we import the item form in views.py