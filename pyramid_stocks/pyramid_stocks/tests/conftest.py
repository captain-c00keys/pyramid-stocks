from pytest import fixture
from pyramid import testing


@fixture
def dummy_request():
    return testing.DummyRequest()

@fixture
def dummy_post_request():
    return testing.DummyRequest(post={})
