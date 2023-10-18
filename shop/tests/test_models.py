from django.test import TestCase
from shop.models import Category, Product


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Test Category", slug="test-category"
        )

    def test_category(self):
        self.assertEqual(self.category.name, "Test Category")
        self.assertEqual(self.category.slug, "test-category")
        self.assertEqual(str(self.category), "Test Category")


class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Test Category", slug="test-category"
        )

        self.product = Product.objects.create(
            category=self.category,
            name="Test Product",
            slug="test-product",
            description="Testing Product",
            price=9.99,
        )

    def test_product(self):
        self.assertEqual(self.product.category, self.category)
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.slug, "test-product")
        self.assertEqual(self.product.description, "Testing Product")
        self.assertEqual(self.product.price, 9.99)
        self.assertTrue(self.product.available)
