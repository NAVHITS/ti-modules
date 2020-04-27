# This module uses the DirectConnect API of AlienVault OTX
# It checks an IP against the endpoint
# To get various information for an IP

from pip._vendor import requests
import json
from configparser import SafeConfigParser

parser = SafeConfigParser()
parser.read('conf/config.ini')

def otx_ip_check(ip):
    endpoint = parser.get('ALIENVAULT-OTX', 'url')
    key = parser.get('ALIENVAULT-OTX', 'api')
    try:
        response = requests.get(endpoint+ip,headers={'X-OTX-API-KEY':key})
        if ((response.status_code == 200) & (response.json() != None)):
            result = response.json()
            pass
        else:
            result = {"error":"No information available."} 
            pass
        pass
    except:
        result = {"error":"No information available."}
        pass

    return result