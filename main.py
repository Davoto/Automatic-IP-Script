import os


def get_ip():
    host = os.system('hostname -I')
    return str(host)[:-2]


def cloudflare_update(ip):
    test = 0


if __name__ == '__main__':
    print(get_ip())
