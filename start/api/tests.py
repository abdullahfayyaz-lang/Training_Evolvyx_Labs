from django.test import TestCase
from api.models import Order, User ,Product
from django.core.exceptions import ValidationError
from django.urls import reverse
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework import status

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




     



