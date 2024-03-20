import subprocess
import sys
import requests
import datetime
from dotenv import load_dotenv
import os


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

    response = requests.request("PATCH", url, json=payload, headers=headers)

    print(response.text)


if __name__ == '__main__':
    load_dotenv()
    ip = get_ip()
    AUTH_KEY = os.getenv('AUTH_KEY')
    AUTH_MAIL = os.getenv('AUTH_MAIL')
    DOMAIN = os.getenv('DOMAIN')
    ZONE_ID = os.getenv('ZONE_ID')
    DNS_ID = os.getenv('DNS_ID')
    print(f"Dit is het lokale ip: {ip}")
    cloudflare_update(ip, DOMAIN, ZONE_ID, DNS_ID, AUTH_KEY, AUTH_MAIL)
