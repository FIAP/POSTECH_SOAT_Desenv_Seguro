import requests
import json
import settings
import render
from os import path
from http import HTTPStatus
from asyncio.log import logger
from storage import TokenStorage
from generate_jwt import generate_jwt


storage = TokenStorage()

def payload(payload):
    with open('payloads/'+payload+'.json') as json_body:
        data = json.load(json_body)
        body = json.dumps(data)
    return body

def authToken():    
    if storage.isTokenValid(0):
        return storage.getToken(0)["token"]
    
    try:
        jwt_token = generate_jwt()
        r = requests.post(
            f"{settings.DEVEX_GITHUB_HOST}/app/installations/{settings.DEVEX_INSTALLATION_ID}/access_tokens",
            headers={'Authorization': ('Bearer ' + jwt_token )},
            timeout=settings.DEVEX_REQUEST_TIMEOUT_DEFAULT,
        )

        if r.status_code == HTTPStatus.CREATED:
            storage.addToken(0, r.json()["token"], r.json()["expires_at"])
            return storage.getToken(0)["token"]
        else:
            raise Exception("error while getting token, details", r.content, r.status_code)

    except Exception as error_message:
        raise error_message


def disable_webhook(repositorio):
    try: 
        token = authToken()

        r = requests.get(
            f'{settings.DEVEX_GITHUB_HOST}/repos/PicPay/{repositorio}/hooks',
            headers={'Authorization': ('token ' + token)},
            timeout=settings.DEVEX_REQUEST_TIMEOUT_DEFAULT,
        )
        if r.status_code == HTTPStatus.OK or r.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
            data = r.json()
            for i in range(len(data)):
                if data[i]['active'] == True and data[i]['config']['url'] != settings.DEVEX_WEBHOOK_HOST:
                    id = data[i]['id']
                    if id != None:
                        r = requests.patch(
                        f'{settings.DEVEX_GITHUB_HOST}/repos/PicPay/{repositorio}/hooks/{str(id)}',
                        data=payload('desative_webhook'),
                        headers={'Authorization': ('token ' + token)},
                        timeout=settings.DEVEX_REQUEST_TIMEOUT_DEFAULT,
                        )
            print(token)
            return True
        else:
            logger.error("error while disable webhook, details", r.content, r.status_code)
            return False

    except Exception as error_message:
        logger.error("error while disable webhook, details", error_message)
        return False


def create_webhook(http_client: requests.Session, repositorio: str) -> bool:
    try:
        webhook_endpoint = f"{settings.DEVEX_GITHUB_HOST}/repos/picpay/{repositorio}/hooks"
        request_body = render.payload_as_json('webhook')
        request_body['config']['url'] = settings.DEVEX_WEBHOOK_HOST

        if settings.DEVEX_WEBHOOK_SECRET:
            request_body['config']['secret'] = settings.DEVEX_WEBHOOK_SECRET

        logger.info(request_body)

        r = http_client.post(
            webhook_endpoint,
            json=request_body,
            timeout=settings.DEVEX_REQUEST_TIMEOUT_DEFAULT,
        )
        if (
            r.status_code == HTTPStatus.CREATED or
            r.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
        ):
            return True
        else:
            logger.error(
                "error while creating webhook, details %s with status %s",
                r.content,
                r.status_code,
            )
            return False

    except Exception as err:
        logger.error("didn't create webhook %s", err)
        return False

def create_label(repositorio):
    try:  
        token = authToken()

        r = requests.post(
            f'{settings.DEVEX_GITHUB_HOST}/repos/PicPay/{repositorio}/labels',
            data=payload('label'),
            headers={'Authorization': ('token ' + token)},
            timeout=settings.DEVEX_REQUEST_TIMEOUT_DEFAULT,
        )

        if r.status_code == HTTPStatus.CREATED or r.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
            return True 
        else:
            logger.error("error while creating label, details", r.content, r.status_code)
            return False

    except Exception as error_message:
        logger.error("error while creating webhook, details", error_message)
        return False

def create_branch_protection(repositorio,branch):
    try:  
        token = authToken()

        r = requests.put(
            f'{settings.DEVEX_GITHUB_HOST}/repos/PicPay/{repositorio}/branches/{branch}/protection',
            data=payload('protection'),
            headers={'Authorization': ('token ' + token)},
            timeout=settings.DEVEX_REQUEST_TIMEOUT_DEFAULT,
        )

        if r.status_code == HTTPStatus.OK or r.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
            return True
        else:
            logger.error("error while creating branch protection, details", r.content, r.status_code)
            return False
             
    except Exception as error_message:
        logger.error("error while creating branch protection, details", error_message)
        return False

def add_user_deploy(repositorio):
    try:  
        token = authToken()

        r = requests.put(
            f'{settings.DEVEX_GITHUB_HOST}/orgs/PicPay/teams/deploy-pipeline/repos/PicPay/{repositorio}',
            data=payload('user_deploy_pipeline'),
            headers={'Authorization': ('token ' + token)},
            timeout=settings.DEVEX_REQUEST_TIMEOUT_DEFAULT
        )

        if r.status_code == HTTPStatus.NO_CONTENT or r.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
            return True
        else:
            logger.error("error while creating user, details", r.content, r.status_code)
            return False
             
    except Exception as error_message:
        logger.error("error while creating user, details", error_message)
        return False
