# Automatic IP Script (for Cloudflare DNS)
This little script updates your cloudflare DNS settings of a domain to your local IP, this script is for people that have issues with networks that require DHCP and want to keep using the same domain.

## Requirements
- Debian-based linux (May work with other linux flavors but haven't tested.)
- Python 3 (Tested on 3.10)
- Pip package 'python-dotenv'
- A single network connection.

## Setup
1. Install python 3 and python-dotenv
2. Fill in a .env file using the format used in 'env_example.txt'
3. Run the script.
4. (Optional but essential step for headless use) setup a automatic run in for example crontab
