from django.db import models

# Create your models here.
class Item(models.Model):
    # define the attributes that our individual items will have
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name

# CREATE A CLASS
# First we define a item class. 
# When Django sees that we've created a new "item" class, it will 
# automatically create an item's table when we make and run the database migrations. 
# By itself this class won't do anything. We need to use "class inheritance" to give it some functionality
# CLASS INHERITANCE - to inherit the base model class, we put "models.Model" in the parentheses 
# so that our item class can do everything the built-in Django model class can do
# define the attributes that our individual items will have
# We skip the Id field since Django will create that for us automatically. 
# we define a "name" field that will use built-in Django fields called a charfield,
# charfield means it will just have characters or text in it.
# the "done" status field is a boolean field, meaning it can be either True or False.
# We give these fields a couple of restrictions:
# max length attribute of 50 characters on the name field to keep the length of our item names reasonable
# "null equals false" attribute prevents items from being created without a name programmatically and 
# "blank equals false" makes the field required on forms. 
# This way we're certain that a todo item can't be created without a name whether it's done in Python code. 
# Or by a user in a web form or even an administrator in the admin panel. 
# We do the same for the "done field": Null equals false and blank equals false. 
# But we add a default value of false, just to make sure that to-do items are marked as not done by default

# By default all models that inherit this base model class will use its built-in string
# method to display their class name followed by the word object.
# Just so that there's sort of a generic way to display them.
# And you can actually see this method defined in the base model class in django.db.models.base.
# the string method right here returns object and then the primary key. So that's what we see in the admin panel.
# To change that we need to actually override that string method with our own.
# And we can do that just by redefining it here in our own class.
# we define "__string__" and this is going to take in self. Which is the class itself as its own argument.
# And all it's going to do is just return self.name.
# So this is going to return the item class's name attribute which in our case is going to be the name that we put into the form.

# So this is the beauty of class inheritance. We still get all of the default functionality of the default Django model class,
# but we can override this string method just to change how our items are displayed.
# Doing this will make sure that in the admin we see our item names instead of item object.
# So if we go ahead and save that. And then go back to the admin. And refresh.
# We'll see that the items that we've created now display their names instead of the generic values that were displayed before.

# CREATE A TABLE
# After creating item class, we create the table in the database. Because Django uses migrations to handle 
# database operations, we run python3 manage.py makemigrations command to make a migration file: 
# 1. we run it with the dry run flag: python3 manage.py makemigrations - -dry-run, to be sure of what it's 
# going to do and that I'm not making any unintended changes. 
# 2. we run it for real: "python3 manage.py makemigrations". And what happens here is that Django sees we've added a new 
# model to our app, so it creates a new Python file in the migrations folder that contains the code to create that 
# database table based on our model. So, this code will be converted to sequel by Django and executed on the database when we run the migrations. 
# 3. we run: python3 manage.py showmigrations command to see the unapplied migration on our to-do app now. 
# 4. we apply it by running: python3 manage.py migrate (We may first run this with the plan flag: python3 manage.py migrate - -plan 
# just to be 100% certain that we’re not doing anything unintentional. And we can see that it's going to create the model item. 
# That's the planned operation. And if all looks good, we go ahead and run it without plan flag). And that migration has been applied. 


# Even though the items table has been created and we could start creating items programmatically 
# now, we won't be able to see our items in the admin until we expose them. To do that we need 
# to register our model in the todo apps admin.py file. 