import factory
from pytest_factoryboy import register

from product.models import Category, Brand, Product

@register
class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("category test")
    
@register
class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.Faker("brand test")
    
@register
class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker("product test")
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)
    is_digital = factory.Faker("boolean")
    description = factory.Faker("text")
    
