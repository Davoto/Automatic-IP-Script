import datetime
import os
import requests
import subprocess
import sys
from json import loads, dumps
from dotenv import load_dotenv, set_key


def get_ip():
    host_ip = subprocess.check_output("hostname -I", shell=True).decode(sys.stdout.encoding).strip()
    return host_ip


def cloudflare_update(host_ip, domain, zone_id, dns_id, auth_key, auth_mail):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{dns_id}"

    payload = {
        "content": host_ip,
        "name": domain,
        "proxied": False,
        "type": "A",
        "comment": f'IP Update, {datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}',
        "ttl": 1
    }
    headers = {
        "Content-Type": "application/json",
        "X-Auth-Email": auth_mail,
        "Authorization": auth_key,
    }

    return loads(requests.request("PATCH", url, json=payload, headers=headers).text)


if __name__ == '__main__':
    path = os.path.dirname(__file__) + '/.env'
    load_dotenv(path, override=True)
    LOCAL_IP_NEW = get_ip()
    LOCAL_IP = os.getenv('LOCAL_IP')
    print(f"This is the local IP: \"{LOCAL_IP_NEW}\".")
    if LOCAL_IP_NEW != LOCAL_IP:
        AUTH_KEY = os.getenv('AUTH_KEY')
        AUTH_MAIL = os.getenv('AUTH_MAIL')
        DOMAIN = os.getenv('DOMAIN')
        ZONE_ID = os.getenv('ZONE_ID')
        DNS_ID = os.getenv('DNS_ID')

        json_result = cloudflare_update(LOCAL_IP_NEW, DOMAIN, ZONE_ID, DNS_ID, AUTH_KEY, AUTH_MAIL)
        if json_result['success']:
            os.environ['LOCAL_IP'] = LOCAL_IP_NEW
            set_key(path, 'LOCAL_IP', os.environ['LOCAL_IP'])

            print(f'API-CALL Successful.\n\"{json_result["result"]["name"]}\" has been updated.')
        else:
            print('API-CALL Unsuccessful.\nPlease check your .env file in the program\'s folder.\n'
                  'Here the JSON for further error-finding:')
            print(dumps(json_result, indent=2))
    else:
        print('IP has not changed.')
