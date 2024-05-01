from product.models import Category, Brand, Product

from .factories import CategoryFactory, BrandFactory, ProductFactory


class TestModel:
    def test_category_str(self, db):
        category = CategoryFactory(name="Test Category")
        assert str(category) == "Test Category"
        
    def test_brand_str(self, db):
        brand = BrandFactory(name="Test Brand")
        assert str(brand) == "Test Brand"
        

    def test_product_str(self, db):
        # Create a brand
        brand = BrandFactory(name="Test Brand")
        # Create a category
        category = CategoryFactory(name="Test Category")
        # Create a product
        product = ProductFactory(name="Test Product", brand=brand, category=category)
        assert str(product) == "Test Product"
        
