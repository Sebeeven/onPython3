# -*- coding: utf-8 -*-
import requests
#######################

BASE_URL = 'https://api.github.com'
testDemo_token = 'd31edea1995d3d297c18839c1cf8e0804ff7f7cf'

def construct_url(end_point):
    return '/'.join([BASE_URL, end_point])

def basic_auth():
    '''1.the BASIC AUTH
    '''
    response = requests.get(construct_url('user'), auth=('username', 'password'))
    print(response.status_code)
    print(response.text)
    print(response.request.headers)

def basic_oauth():
    '''2.the OAUTH
    '''
    headers = {'Authorization': 'token ' + testDemo_token}
    response = requests.get(construct_url('user/emails'), headers=headers)
    print(response.status_code)
    print(response.text)
    print(response.request.headers)

'''3.the AuthBase from requests
'''
from requests.auth import AuthBase
class GithubAuth(AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers['Authorization'] = ' '.join(['token', self.token])
        return r

def oauth_advanced():
    auth = GithubAuth(testDemo_token)
    response = requests.get(construct_url('user/emails'), auth=auth)
    print(response.status_code)
    print(response.text)
    print(response.request.headers)

'''4.use the proxy to request
   pip3 install 'requests[socks]'
   but you should have signup a proxy server first,eg:Heroku
'''
proxies = {'http':'socks5://127.0.0.1:1080','https':'socks5://127.0.0.1:1080'}
url2 = 'https://www.facebook.com'

def proxies_request():
    response = requests.get(url2, proxies=proxies, timeout=10)
    print(response.status_code)
    print(response.text)
    print(response.request.headers)

########################
if __name__ == '__main__':
    #basic_auth()
    #basic_oauth()
    oauth_advanced()
    #proxies_request()
