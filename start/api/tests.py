from django.test import TestCase,Client
from api.models import Order, User ,Product
from django.core.exceptions import ValidationError
from django.urls import reverse
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django import forms
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib import messages



#Test cases are defined here
#Testing Apis
class ProductAPItestCase(APITestCase):
    def setUp(self):#Things taht always run before runing main tests
        self.admin_user = User.objects.create_superuser(username="batman",password='batman')
        self.noraml_user = User.objects.create_user(username="test_user",password='test_user')
        self.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=9.90,
            stock=10
        )
        self.url=reverse('product-detail',kwargs={'pk':self.product.pk})

    def test_get_product(self):
        response=self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['name'],self.product.name)

    def test_unauthorized_update_product(self):
        data={'name':"Updated Product"}
        response=self.client.put(self.url,data)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    def test_unauthorized_delete_product(self):
        response=self.client.delete(self.url)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)
    
    def test_only_admins_can_delete_product(self):
        #test normal user cannot delete
        self.client.login(username="test_user",password='test_user')
        response=self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Product.objects.filter(pk=self.product.pk).exists())
        # test admin user can delete
        self.client.login(username="batman",password='batman')
        response=self.client.delete(self.url)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
        self.assertFalse(Product.objects.filter(pk=self.product.pk).exists())

        
    def test_only_admins_can_update_product(self):
        #test normal user cannot update
        self.client.login(username="test_user",password='test_user')
        response=self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Product.objects.filter(pk=self.product.pk).exists())
        # test admin user can update
        self.client.login(username="batman",password='batman')
        response=self.client.delete(self.url)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
        self.assertFalse(Product.objects.filter(pk=self.product.pk).exists())


#Testing Models


class ProductModelTest(TestCase):
    def setUp(self):
        # Create a valid product instance for reuse
        self.product = Product.objects.create(
            name="Laptop",
            description="A high-end laptop",
            price=1500.00,
            stock=10
        )

    def test_product_str_method(self):
        """__str__() should return the product name"""
        self.assertEqual(str(self.product), "Laptop")

    def test_in_stock_property_true(self):
        """in_stock property should return True when stock > 0"""
        self.assertTrue(self.product.in_stock)

    def test_in_stock_property_false(self):
        """in_stock property should return False when stock = 0"""
        self.product.stock = 0
        self.assertFalse(self.product.in_stock)

    def test_name_validation_too_short(self):
        """clean() should raise ValidationError if name is shorter than 2 characters"""
        product = Product(
            name="A",  # invalid name
            description="Test product",
            price=100.00,
            stock=5
        )
        with self.assertRaises(ValidationError):
            product.clean()

    def test_valid_product_clean_passes(self):
        """clean() should not raise an error for valid product"""
        product = Product(
            name="TV",
            description="Smart TV",
            price=400.00,
            stock=3
        )
        try:
            product.clean()  # should not raise
        except ValidationError:
            self.fail("clean() raised ValidationError unexpectedly!")

    def test_price_field_precision(self):
        """Price should store decimal values correctly"""
        self.product.price = 1999.99
        self.product.save()
        self.assertEqual(float(self.product.price), 1999.99)






class CustomUserCreationFormTest(TestCase):

    def test_valid_form_with_example_domain(self):
        """Form should be valid when email ends with @example.com"""
        form_data = {
            'username': 'hasnat',
            'email': 'user@example.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!'
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_email_domain(self):
        """Form should raise ValidationError for non-example.com email"""
        form_data = {
            'username': 'ali',
            'email': 'user@gmail.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!'
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
        self.assertEqual(
            form.errors['email'][0],
            'Invalid Email Domain .'
        )

    def test_password_mismatch(self):
        """Form should be invalid if passwords do not match"""
        form_data = {
            'username': 'kiran',
            'email': 'user@example.com',
            'password1': 'Password123!',
            'password2': 'DifferentPass!'
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    def test_form_fields_exist(self):
        """Form should include all specified fields"""
        form = CustomUserCreationForm()
        self.assertEqual(
            list(form.fields.keys()),
            ['username', 'email', 'password1', 'password2']
        )



class LoginViewIntegrationTest(TestCase):
    def setUp(self):
        # Create a user for testing
        self.username = "hasnat"
        self.password = "StrongPass123!"
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password,
            email="hasnat@example.com"
        )
        self.login_url = reverse('login')  # assuming your view is named 'login'

    def test_login_page_renders_correctly(self):
        """GET request should render the login template"""
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_successful_login_redirects_and_creates_token(self):
        """POST valid credentials should authenticate and redirect"""
        form_data = {
            'username': self.username,
            'password': self.password
        }
        response = self.client.post(self.login_url, data=form_data)

        # Expect redirect to /api/orders/
        self.assertEqual(response.status_code, 302)
        self.assertIn('/api/orders/', response.url)

        # Ensure user is logged in
        self.assertTrue(response.wsgi_request.user.is_authenticated)

        # Manually verify token generation logic
        refresh = RefreshToken.for_user(self.user)
        self.assertIsNotNone(str(refresh.access_token))
        self.assertIsNotNone(str(refresh))

    def test_invalid_credentials_show_error_message(self):
        """POST invalid credentials should re-render form with error message"""
        form_data = {
            'username': self.username,
            'password': 'WrongPassword123!'  # invalid password
        }
        response = self.client.post(self.login_url, data=form_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        messages_list = list(response.context['messages'])
        self.assertTrue(
            any("Invalid credentials." in str(m) for m in messages_list),
            msg="Expected 'Invalid credentials.' message not found."
        )
        # Ensure user is not authenticated
        self.assertFalse(response.wsgi_request.user.is_authenticated)

class SignupViewIntegrationTest(TestCase):
    def setUp(self):
        self.signup_url = reverse('signup')  # ensure your URL name is 'signup'

    def test_signup_page_renders_correctly(self):
        """GET request should render signup template"""
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')
        self.assertIsInstance(response.context['form'], CustomUserCreationForm)

    def test_successful_signup_creates_user_and_redirects(self):
        """POST valid data should create a new user, generate JWT, and redirect"""
        form_data = {
            'username': 'hasnat',
            'email': 'user@example.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!'
        }

        response = self.client.post(self.signup_url, data=form_data, follow=True)
        self.assertRedirects(response, '/api/login/')
        
        self.assertTrue(User.objects.filter(username='hasnat').exists())


        messages_list = list(response.context['messages'])
        self.assertTrue(any("Account created successfully!" in str(m) for m in messages_list))

        user = User.objects.get(username='hasnat')
        refresh = RefreshToken.for_user(user)
        self.assertIsNotNone(str(refresh.access_token))
        self.assertIsNotNone(str(refresh))

    def test_signup_invalid_email_domain_shows_error(self):
        """POST invalid email domain should re-render with error message"""
        form_data = {
            'username': 'ali',
            'email': 'user@gmail.com',  # invalid domain (CustomUserCreationForm rule)
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!'
        }

        response = self.client.post(self.signup_url, data=form_data)

        # Should remain on signup page
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')
        self.assertContains(response, 'Invalid Email Domain .')

        # No user should be created
        self.assertFalse(User.objects.filter(username='ali').exists())

    def test_signup_password_mismatch_shows_error(self):
        """POST with non-matching passwords should fail"""
        form_data = {
            'username': 'sana',
            'email': 'user@example.com',
            'password1': 'Password123!',
            'password2': 'WrongPassword!'
        }

        response = self.client.post(self.signup_url, data=form_data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')
        messages_list = list(response.context['messages'])
        self.assertTrue(any("Please correct the errors below and try again." in str(m) for m in messages_list))
        self.assertFalse(User.objects.filter(username='sana').exists())