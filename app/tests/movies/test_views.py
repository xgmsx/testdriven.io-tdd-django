import pytest

from movies.models import Movie


@pytest.mark.django_db
def test_add_movie(client):
    resp = client.post(
        "/api/movies/",
        {
            "title": "The Big Lebowski",
            "genre": "comedy",
            "year": "1998",
        },
        content_type="application/json"
    )
    assert resp.status_code == 201
    assert resp.data["title"] == "The Big Lebowski"

    movies = Movie.objects.filter(title="The Big Lebowski")
    assert len(movies) == 1


@pytest.mark.django_db
def test_add_movie_invalid_json(client):
    resp = client.post(
        "/api/movies/",
        {},
        content_type="application/json"
    )
    assert resp.status_code == 400


@pytest.mark.django_db
def test_add_movie_invalid_json_keys(client):
    resp = client.post(
        "/api/movies/",
        {
            "title": "The Big Lebowski",
            "genre": "comedy",
        },
        content_type="application/json"
    )
    assert resp.status_code == 400

    movies = Movie.objects.filter(title="The Big Lebowski")
    assert len(movies) == 0


@pytest.mark.django_db
def test_get_single_movie(client, add_movie):
    movie = add_movie(title="The Big Lebowski", genre="comedy", year="1998")
    resp = client.get(f"/api/movies/{movie.id}/")
    assert resp.status_code == 200
    assert resp.data["title"] == "The Big Lebowski"


def test_get_single_movie_incorrect_id(client):
    resp = client.get(f"/api/movies/foo/")
    assert resp.status_code == 404


@pytest.mark.django_db
def test_get_all_movies(client, add_movie):
    add_movie(title="The Big Lebowski", genre="comedy", year="1998")
    add_movie("No Country for Old Men", "thriller", "2007")

    movies = Movie.objects.filter(title="The Big Lebowski")
    assert len(movies) == 1
    movies = Movie.objects.filter(title="No Country for Old Men")
    assert len(movies) == 1
    resp = client.get(f"/api/movies/")
    assert resp.status_code == 200
    assert len(resp.data) >= 2
