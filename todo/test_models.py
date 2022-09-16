from django.test import TestCase
from .models import Item

# Create your tests here.

class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertEqual(str(item), 'Test Todo Item')
    
# import TestCase from django.test and our item model from .models
# create a new class called TestModels which inherits TestCase.
# And inside it a method called test_done_defaults_to_false, which takes self as parameter

# "Self" here refers to our "TestModels" class, which because it inherits the TestCase 
# class, will have a bunch of pre-built methods and functionality that we can use.
# We create an item using item.objects.create and call this item "Test Todo Item".
# And then use assertFalse to confirm that it's done status is, in fact, false by default

# run this specific test in the terminal: "python manage.py test todo.test_models"

# TEST 2 - test the string method of our item model in models.py.
# We create a new test called test_item_string_method_returns_name
# use item.objects.create to create an item with the name of Tests Todo Item.
# And use "self.assertEqual" to confirm that this name is returned when we render this item as a string.
