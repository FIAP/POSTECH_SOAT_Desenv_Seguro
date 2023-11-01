import requests
from src.app.http_client import create_request_session


def test_should_create_session_successfully():
    def mock_token_generator():
        return 'xpto'

    session = create_request_session(mock_token_generator)

    assert isinstance(session, requests.Session)
    assert session.headers['authorization'] == 'token xpto'
