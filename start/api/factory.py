import factory
from faker import Faker  # ✅ correct import
from .models import Product, Order, User
import uuid
fake = Faker()  # ✅ instantiate faker

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.LazyAttribute(lambda _: fake.word())
    description = factory.LazyAttribute(lambda _: fake.sentence(nb_words=12))
    price = factory.LazyAttribute(lambda _: fake.pydecimal(left_digits=3, right_digits=2, positive=True))
    stock = factory.LazyAttribute(lambda _: fake.random_int(min=1, max=100))

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.LazyAttribute(lambda _: fake.name())
    email = factory.LazyAttribute(lambda _: fake.unique.email())
    password = factory.PostGenerationMethodCall("set_password", "password123")



    