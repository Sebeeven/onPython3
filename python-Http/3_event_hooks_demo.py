# -*- coding: utf-8 -*-
import requests
######################

#url = 'http://www.baidu.com'
url = 'https://api.github.com'
def get_key_info(response, *args, **kwargs):
    ## the callback function
    print(response.headers['Content-Type'])

def main():
    ## the main function
    requests.get(url, hooks=dict(response=get_key_info))

main()
