from .models import Product, Category
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status


class ProductTestCase(APITestCase):
    """
    Test suite for product
    """

    def setUp(self):
        self.client = APIClient()
        self.data = {
            "name": "Mobile",
            "brand": "samsung",
            "price": 250.00,
            "quantity": 100,
        }
        self.url = "/Products/"

    def test_create_product(self):
        """
        test ProductViewSet create method
        """

        data = self.data
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, "Mobile")

    def test_create_product_without_name(self):
        """
        test ProductViewSet create method when name is not in data
        """
        data = self.data
        data.pop("name")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_product_when_name_equals_blank(self):
        """
        test ProductViewSet create method when name is blank
        """
        data = self.data
        data["name"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_product_without_quantity(self):
        """
        test ProductViewSet create method when email is not in data
        """
        data = self.data
        data.pop("quantity")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class CategoryTestCase(APITestCase):
    """
    Test suite for Category
    """

    def setUp(self):
        self.client = APIClient()
        self.data = {
            "name": "Electronics",
        }
        self.url = "/Category/"

    def test_create_category(self):
        """
        test CategoryViewSet create method
        """

        data = self.data
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().name, "Electronics")

    def test_create_category_without_name(self):
        """
        test CategoryViewSet create method when name is not in data
        """
        data = self.data
        data.pop("name")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_category_when_name_equals_blank(self):
        """
        test CategoryViewSet create method when name is blank
        """
        data = self.data
        data["name"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

