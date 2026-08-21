from django.urls import reverse


def test_hello_world_view(client):
    url = reverse("home")

    response = client.get(url)

    assert response.status_code == 200
    assert response.content == b"Hello, World!"