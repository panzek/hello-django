"""django_todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_todo_list, name='get_todo_list'),
    path('add', views.add_item, name='add'),
    path('edit/<item_id>', views.edit_item, name='edit'),
    path('toggle/<item_id>', views.toggle_item, name='toggle'),
    path('delete/<item_id>', views.delete_item, name='delete')
]

#PATH Function Explained
# import get_todo_list, add_item, toggle_item, edit_item, and delete_item functions from views. Because the list of imports is getting 
# quite long, instead of importing each view individually: "from todo.views import get_todo_list, etc", we remove them and change to: 
# "from todo import views", and simply add views dot in front of all the views. Everything is exactly the same, but a little less verbose.

# Next, define the url that will trigger the "get_todo_list" function and return the http response to the browser.
# To do that, we use the built-in "path" function which typically takes three arguments:
# 1st parameter, url (we pass it an empty string so this will act as our home page.
# 2nd parameter, get_todo_list function, which is the "view" function that it's going to return.
# 3rd is a name parameter which we'll be the name of our page when we run server.

# The same process for the "add_item", "toggle_item", "edit_item" templates, and delete_item.
# The angular bracket syntax in edit path: "edit/<item_id>", is common in Django URLs, and is the mechanism by which the item 
# ID makes its way from links or forms in our templates, through the URL, and into the view which expects it as a parameter.

# with the new URL ready, let's go to "view.py" to create a "view" for it.

