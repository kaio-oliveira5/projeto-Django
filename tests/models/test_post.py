import pytest

from blog.factories import PostFactory


@pytest.mark.django_db
def test_create_post():
    post = PostFactory(title='Meu primeiro post')

    assert post.title == 'Meu primeiro post'