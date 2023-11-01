'''This file should be an adapter'''
import json
from os import path


def payload_as_json(name: str) -> json:
    abs_filename = path.join('payloads', f'{name}.json')
    with open(abs_filename, 'r', encoding='utf-8') as content:
        return json.load(content)
