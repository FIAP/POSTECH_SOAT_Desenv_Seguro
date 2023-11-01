'''This file should be an repository'''
import requests


def create_request_session(token_generator: callable) -> requests.Session:
    token = token_generator()
    session = requests.Session()
    session.headers.update({'authorization': f'token {token}'})

    return session
