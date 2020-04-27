# This module uses the Pulsedive free API endpoint
# Most of it is part of OSINT data
# This module has 3 endpoints

from pip._vendor import requests
import json
from configparser import SafeConfigParser

parser = SafeConfigParser()
parser.read('conf/config.ini')

# This endpoint will get information for an indicator
def info(ip):
    endpoint = parser.get('PULSEDIVE', 'get_info_url')
    key = parser.get('PULSEDIVE', 'api')
    
    parameters = {
        "ioc": ip,
        "probe": "1",
        "pretty": "1",
        "key": key
    }

    response = requests.get(endpoint, params=parameters) 

    result = response.json()
    return result

def search(ip, val_type, risk, attribute, properties, threat, feed, limit):
    endpoint = parser.get('PULSEDIVE', 'search_info_url')
    key = parser.get('PULSEDIVE', 'api')
    
    # Refer https://pulsedive.com/api/?q=search to find how to set these parameters

    parameters = {
        "value": ip,
        "type": val_type,
        "risk": risk,
        "attribute": attribute,
        "property": properties,
        "threat": threat,
        "feed": feed,
        "limit": limit,
        "pretty": "1",
        "key": key
    }

    response = requests.get(endpoint, params=parameters)
    
    result = response.json()
    return result

def analyze(ip):
    endpoint = parser.get('PULSEDIVE', 'analyze_url')
    key = parser.get('PULSEDIVE', 'api')

    parameters = {
        "ioc": ip,
        "probe": "1",
        "pretty": "1",
        "key": key
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }

    response = requests.post(endpoint, data=parameters, headers=headers)
    
    result = response.json()
    return result