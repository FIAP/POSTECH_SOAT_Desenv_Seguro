import requests
from unittest.mock import Mock, patch
from src.app.migration_repo import create_webhook


@patch('render.payload_as_json')
def test_should_be_create_webhook_successfully(payload_as_json_mock):
    payload_as_json_mock.return_value = {'config': {}}

    mock_http_client = Mock()
    response = requests.Response
    response.status_code = 201
    mock_http_client.post.return_value = response
    repository = "ms-fake-service"

    response = create_webhook(mock_http_client, repository)
    mock_http_client.assert_called
    mock_http_client.post.assert_called_with(
        'https://api.github.com/repos/picpay/ms-fake-service/hooks',
        json={'config': {'url': 'https://moonlight-pipeline-webhook.tekton.ppay.me/microservices'}},
        timeout=20
    )
    assert response is True


@patch('render.payload_as_json')
def test_should_be_create_webhook_unprocessable_entity(payload_as_json_mock):
    payload_as_json_mock.return_value = {'config': {}}

    mock_http_client = Mock()
    response = requests.Response
    response.status_code = 422
    mock_http_client.post.return_value = response
    repository = "ms-fake-service"

    response = create_webhook(mock_http_client, repository)
    mock_http_client.assert_called
    mock_http_client.post.assert_called_with(
        'https://api.github.com/repos/picpay/ms-fake-service/hooks',
        json={'config': {'url': 'https://moonlight-pipeline-webhook.tekton.ppay.me/microservices'}},
        timeout=20
    )
    assert response is True


@patch('render.payload_as_json')
def test_should_not_create_webhook(payload_as_json_mock):
    repository = "ms-fake-service"
    payload_as_json_mock.return_value = {'config': {}}

    mock_http_client = Mock()
    response = requests.Response
    response.status_code = 404
    mock_http_client.post.return_value = response

    response = create_webhook(mock_http_client, repository)
    mock_http_client.assert_called
    mock_http_client.post.assert_called_with(
        'https://api.github.com/repos/picpay/ms-fake-service/hooks',
        json={'config': {'url': 'https://moonlight-pipeline-webhook.tekton.ppay.me/microservices'}},
        timeout=20
    )
    assert response is False


@patch('render.payload_as_json')
def test_should_not_throw_exception(payload_as_json_mock):
    repository = "ms-fake-service"
    payload_as_json_mock.return_value = {'config': {}}

    mock_http_client = Mock()
    mock_http_client.post.side_effect = Exception('mocked Error')

    response = create_webhook(mock_http_client, repository)

    mock_http_client.assert_called
    mock_http_client.post.assert_called_with(
        'https://api.github.com/repos/picpay/ms-fake-service/hooks',
        json={'config': {'url': 'https://moonlight-pipeline-webhook.tekton.ppay.me/microservices'}},
        timeout=20
    )
    assert response is False
