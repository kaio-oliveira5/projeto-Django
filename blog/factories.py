import factory
from faker import Faker

from django.contrib.auth.models import User

from blog.models import Post


faker = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker("safe_email")
    username = factory.LazyAttribute(lambda x: faker.name())


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.LazyAttribute(lambda x: faker.sentence())
    slug = factory.LazyAttribute(lambda x: faker.slug())
    author = factory.SubFactory(UserFactory)
    content = factory.LazyAttribute(lambda x: faker.text())
    status = 0