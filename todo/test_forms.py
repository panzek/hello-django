from django.test import TestCase
from .forms import ItemForm

# Create your tests here.

class TestItemForm(TestCase):

    # test 1
    def test_item_name_is_required(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')
    
    # test 2
    def test_done_field_is_not_required(self):
        form = ItemForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())
    
    # TEST 3
    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])

# import Testcase from django.test and our ItemForm (what we want to test) from .forms
# create a new class called TesItemForm, which will inherit Testcase and contain all 
# the pre-built methods and functionality that we can use to test this form.

# TEST 1
# We want to test to make sure that the name field is required in order to create an item.
# In general, you'll want to name your tests so that when they fail you can easily see what the issue is.
# So we call this one "test_item_name_is_required".
# "Self" here refers to our "TestItemForm" class, which because it inherits the TestCase 
# class, will have a bunch of pre-built methods and functionality that we can use.

# we begin by instantiating a form and deliberately instantiate it without a name to simulate a user who 
# submitted the form without filling it out. Note the use of curly brackets to hold a dictionary of key: value pairs

# This form should not be valid. So, we use assertFalse to ensure that that's the case.
# When the form is invalid, it should also send back a dictionary of fields on which there were errors and the Associated error messages
# Knowing this, we can be even more specific by using "assertIn" to assert whether there's a name key in the dictionary of form errors.

# Finally, to really drive the point home, we use assertEqual to check whether the error message on the name field is this field is required.
# We include the "period" at the end here as the string will need to match exactly.
# Also we're using the zero index here because the form will return a list of errors on each field.
# and this verifies that the first item in that list is our string telling us the field is required, 
# as we're now testing:
# - in the 1st assertion that the form is not valid, 
# - in the 2nd assertion, that the error occurred on the name field, and 
# - in the 3rd assertion that the specific error message is what we expect.

# TEST 2
# This 2nd test will ensure the done field is not required.
# It shouldn't be since it has a default value of false on the item model.
# create the form sending only a name and test that the form is valid as 
# it should be even without selecting a done status.

# TEST 3
# test to ensure that the only fields that are displayed in the form are the name and done fields.
# we instantiate an empty form and use assert equal to check whether the form.meta.fields attribute
# is equal to a list with name and done in it. Note that Meta begins with a capital "M". 
# Note also the use of square brackets to hold list items: "['name', 'done']"

# This will ensure that the fields are defined explicitly. And if someone changes the item model down the 
# road our form won't accidentally display information we don't want it to.
# This will also protect against the fields being reordered. Since the list must match exactly.

# RUN test in Terminal: 
# to run all the tests: "python manage.py test"
# But we can be more specific about what we're testing. We could, for example: 
# run only the "test_forms" itself: "python manage.py tests todo.test_forms"
# Run a specific "class" of test: "python manage.py tests todo.test_forms.TestItemForm"
# or run a "specific individual test": "python manage.py tests todo.test_forms.test_fields_are_explicit_in_form_metaclass" 
