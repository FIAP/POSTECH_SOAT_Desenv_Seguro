from asyncio.log import logger
from pathlib import Path
import jwt
from cryptography.hazmat.primitives import serialization
import time
import sys


def generate_jwt():
    try:
        payload ={
            'iss': ('206724'),
            'iat': int(time.time() - 60),
            'exp': int(time.time() + 10 * 60) ,
        }
        private_key_text = Path('keys/github_key.pem').read_text()
        private_key = serialization.load_pem_private_key(
            private_key_text.encode(),
            password=None
        )
        return jwt.encode(payload=payload, key=private_key, algorithm="RS256")

    except Exception as error_message:
        logger.fatal("error while generating jwt: ", error_message)
        sys.exit(1)
