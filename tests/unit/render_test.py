from unittest.mock import patch, mock_open
from src.app.render import payload_as_json


def test_should_render_payload_by_keyword():
    expected_payload = {'config': {'url': 'https://tekton.ppay.me/microservices'}} 
    with patch('builtins.open', mock_open(read_data='{"config": {"url": "https://tekton.ppay.me/microservices"}}')):
        payload = payload_as_json('webhook')
        assert payload == expected_payload
