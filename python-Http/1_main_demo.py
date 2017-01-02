# -*- coding: utf-8 -*-

import json
import requests
##################################

# 0 the github api
url = 'https://api.github.com'

def build_uri(endpoint):
    return '/'.join([url, endpoint])

def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)


def request_method():
    '''1.get response from api with no param
    '''
    response = requests.get(build_uri('users/Sebeeven'))
    print(better_print(response.text))

def params_request():
    '''2.get response from api with params
    '''
    response = requests.get(build_uri('users'),params={'since':11})
    print(better_print(response.text))
    print(response.request.headers)
    print(response.url)

def hard_request():
    '''3.use session to sent validation info to server 
    '''
    from requests import Request, Session
    s = Session()
    headers = {'User-Agent': 'fake1.3.4'}
    req = Request('GET', build_uri('user/emails'), auth=('username','password'),headers=headers)
    prepped = req.prepare()
    print('before-------------')
    print(prepped.body)
    print(prepped.headers)
    resp = s.send(prepped, timeout=5)
    print('after--------------')
    print(resp.status_code)
    print(resp.request.body)
    print(resp.request.headers)
    
######################################
if __name__ == '__main__':
    request_method()
#    params_request()
#    hard_request()

