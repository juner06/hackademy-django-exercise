from django.test import TestCase
from django.urls import reverse
from activity1.forms import UserRegistrationForm
from django.contrib.auth import get_user_model



User = get_user_model()



class RegisterTest(TestCase):
   
   def setUp(self):
        
        self.form_class = UserRegistrationForm

        self.user = {
            "first_name": "tester",
            "last_name": "testerer",
            "username":"testuser1",
            "email":"testuser1@app.com",           
            "password1":'p4ssword123###',
            "password2":'p4ssword123###'
        }

        User.objects.create_user(
            username =self.user['username'],
            email=self.user['email'],
            password=self.user['password1']
        )

   
   def test_registration_creates_user_in_db(self):
        

        form = self.form_class(self.user)

        if form.is_valid():
            form.save()

        self.assertEqual(User.objects.count(), 1)


   def test_registration_redirects_to_home_page(self):
        
        user_data ={
            'username':self.user['username'],
            'password':self.user['password1']
        }

        response = self.client.post(reverse('login'), user_data)

        self.assertRedirects(response, reverse('home'))
