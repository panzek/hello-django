""" import our packages """
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm


# Create the views here

def get_todo_list(request):
    """ Create todo list function """
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "todo/todo_list.html", context)

def add_item(request):
    """ Create add item function """
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = ItemForm()
    context = {
        'form':form
    }
    return render(request, "todo/add_item.html", context)

def edit_item(request, item_id):
    """ Create edit item function """
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = ItemForm(instance=item)
    context = {
        'form':form
    }
    return render(request, "todo/edit_item.html", context)

def toggle_item(request, item_id):
    """ Create toggle item function """
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_todo_list')

def delete_item(request, item_id):
    """ Create delete item function """
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_list')

# Let's step through the code: 
# import Item from .models", which allows the use of Item model in our views.
# import ItemForm from .forms to make sure we've form.py available for use in the template,

# GET_TODO_list view:
# Next, we define a function called "get_todo_list. This is the views function (view for short)
# Each view function takes an HttpRequest object as its first parameter, typically named "request"
# We get a query set of all the items in the database and store it in "items" variable.
# create a variable called context, which is a dictionary with all of our items in it:
# it has a key of items and the value is our items variable that we just created.
# We then add that context as a third argument to the render function. This will 
# ensure that we have access to it in our "todo_list.html" template.

# On return render:
# Instead of writing HTML as a string in Python, we write it in an actual HTML file and pass it to the render function to let Django do the work.
# We use the render function, which was imported into this views.py file when we created our app originally.
# The render function takes an HTTP "request" and a template name: todo/todo_list.html, as it's two arguments and it returns render.

# ADD_item view:
# POST Handler - in the request.post handler, instead of trying to create the item manually, we let our form from forms.py do it.
# we create empty form and populate the form in Django with the request.post data and call the is_valid method on the form.
# Django will automatically compare the data submitted in the POST request to the data required on the model and make sure everything matches up.
# To save our item, we call "form.save" and then redirect to the get_todo list view

# Create an instance of the ItemForm and add the context, which contains the empty form
# then return the context to the template and go to the "add_item" template to render the 
# form just like we would any other template variable.

# EDIT_item view:
# this view will take in the request and an item_id parameter, that's, the item.id we attached to the 
# edit link in todo_list.html file.

# we get a copy of the item from the database using a built in django shortcut called get_object_or_404, 
# which we'll use to say we want to get an instance of the item model with an ID equal to the item ID that was passed 
# into the view via the URL. This method will either return the item if it exists. Or a 404 page not found if not.

# POST Handler - without writing a post handler add_item wouldn't update.
# Everythin about our post handler is the same as in add_item except that we 
# give our form the specific item instance we want to update: instance=item.  

# We then create an instance of our item form and return it to the template in the context.
# To pre-populate the form with the items current details, we pass in an instance argument to 
# the form, telling it that it should be prefilled with the information for the "item" we just got 
# from the database: instance=item. "item" is the variable that we stored the get_object_or_404 value
# Lastly, we import the "get_object_or_404" from django shortcut. 

# TOGGLE_item view:
# This view won't have a template because it's just going to toggle the item status and then redirect back to the to-do list.
# like the edit_item view. It'll take in the request as well as the item ID the user wants to toggle.
# We then use the same logic to get the item in question. Change it's done status to the opposite by using not, 
# which will just flip it to the opposite of whatever it currently is. And then save the item. So this will make 
# it so that when a user clicks toggle. Our view will get the item, and if it's done status is currently true it 
# will flip it to false and vice versa. Finally, we'll just redirect back to they get_todo list view

# DELETE_item view:
# For the ability to delete items, our structure will be pretty much identical to everything we've done so far.
# But instead of changing the item status and saving it, we simply delete the item and then redirect.
# Of course, we'll need a URL for this so we'll do that in urls.py

# What will happen here is, when somebody hits this "add_item" URL, for example, they're going to end up in this "add_item" view.
# If it's a GET request, then we just return (the last return) the add_item HTML template by rendering it to them.
# But if it's a POST request, we get the information from the form that comes in from this template and use it to create a new item. 
# And then we'll redirect them back to the get_todo_list view where they'll see their updated todo list.

# But how do we make this function available to the web browser? 
# The answer is we do it through urls.py. We need a new URL to access these templates because right now if 
# we click the link we'll get a page not found error. So go to urls.py under urlpatterns object and update the path.

# SUMMARY
# The basic functionality of a django web application included writing a simple Python 
# function in views.py that returns an HTTP response saying hello to the browser. 
# And then connecting that Python function to a URL using the path function in urls.py.

