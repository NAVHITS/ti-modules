# Based on AbuseIPDB Docs
# This module will check an IP against the endpoint
# The API response will contain IP info and blacklist confidence

from pip._vendor import requests
import json
from configparser import SafeConfigParser

parser = SafeConfigParser()
parser.read('conf/config.ini')

def abuse_ip_check(ip):
    endpoint = parser.get('ABUSEIP-DB', 'url')
    key = parser.get('ABUSEIP-DB', 'api')
    x = parser.get('ABUSEIP-DB', 'noOfDays')

    querystring = {
        'ipAddress': ip,
        # MaxAgeInDays set to x
        # This will fetch results from past x days
        # You can make changes to this x in the config file
        # If not set will fetch details for last 30 days
        'maxAgeInDays': x
    }

    headers = {
        'Accept': 'application/json',
        'Key': key
    }

    response = requests.get(url=endpoint, headers=headers, params=querystring)

    # Formatted output
    decodedResponse = json.loads(response.text)
    return decodedResponse

