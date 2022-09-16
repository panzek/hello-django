from django.test import TestCase
from .models import Item

# Create your tests here.

class TestViews(TestCase):

    def test_todo_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        response = self.client.post('/add', {'name': 'Test Added Item'})
        self.assertRedirects(response, '/')

    def test_can_delete_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        item = Item.objects.create(name='Test Todo Item', done=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)
    
    def test_can_edit_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.post(f'/edit/{item.id}', {'name': 'Updated Name'})
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.name, 'Updated Name')

     
    
# We want to test not only that our views return a successful HTTP response and that they're using 
# the proper templates. But also, what they can do. Specifically adding toggling and deleting items.

# "Self" here refers to our "TestViews" class, which because it inherits the TestCase 
# class, will have a bunch of pre-built methods and functionality that we can use.

# TEST 1
# To test the HTTP responses of the views, we use a built-in HTTP client that comes with the Django 
# testing framework. we start with the get_todo_list view by setting a variable response equal 
# to "self.client.get" and providing the URL slash since we just want to get the home page.
# We then use assertEqual to confirm that the response.status code is equal to 200, a successful HTTP response.

# To confirm the view uses the correct template we use self.assertTemplateUsed and tell it the template we expect it to use in the response.

# TEST 2 - testing get the add_item page
# The only things we have to change are the URL we're getting and the template we expected to use.

# TEST 3 - testing get the edit_item page
# The things we have to change are the URL we're getting and the template we're expecting.
# But the URL edit will be followed by an item ID, say 99. If we just pass it a static number though the 
# test will only pass if that item ID exists in our database. And we want to be more generic than that.

# Conveniently in Django tests, we can also do CRUD operations.
# So we import the item model at the top and then create an item to use in this test.
# Testing that we can get the Edit URL is by adding on its ID, with the Python f string: f'/edit/{item.id}'.

# f strings work almost identically to the template literals you learned about in the JavaScript lessons.
# All we've got to do is add an "f" before the opening quotation mark and then anything we put 
# in curly brackets will be interpreted and turned into part of the string.

# TEST 4 - test creating an item
# we set the response equal to self.client.post on the add URL and give it a name for the item 
# as if we've just submitted the item form. If the item is added successfully, the view should 
# redirect back to the home page. So we use assert redirects to confirm that it redirects back to slash.

# TEST 5 - test whether we can delete an item.
# First, we create one using item.objects.create. And use the same syntax as we used on 
# the edit_item view to make a get request. To delete slash the items ID
# Again we'll want to assert that the view redirects us as that's what it should do if it's successful.
# And while we should technically already know the test passed at this point, just to prove that the item 
# is in fact deleted, we'll try to get it from the database using .filter and passing it the item ID, 
# since that item is the only one on the database and we just deleted it.
# We can be certain the view works by asserting whether the length of existing items is zero.

# TEST 6 - test whether toggling items is working
# The first three lines of this test will be almost the same as in TEST 5.
# But this time, we create an item with a done status of true and call the toggle URL on its ID.
# After asserting that the view redirects us, we get the item again and call it updated item.
# And then use assertFalse to check it's done status.

# TEST 7 - test the post method of our edit view
# We create a new item like we've done above in the toggle item test.
# we grab the code above we use to test getting the edit view, except this time instead 
# of using self.client.get We'll use self.client.post and post an updated name.
# We then assert that the view redirected us and get the updated item .
