# Automatic IP Script (for Cloudflare DNS)

This little script updates your cloudflare DNS settings of a domain to your local IP, this script is for people that 
have issues with networks that require DHCP and want to keep using the same domain for a local server.

## Requirements

- Debian-based linux (May work with other linux flavors but haven't tested.)
- Python 3 (Tested on 3.10)
- Pip package 'python-dotenv'
- Cron
- A single network connection.

## Setup domain

1. Get a domain compatible with Cloudflare, add it to a cloudflare account and add a dns A record with a random ip 
(you'll automatically change it anyway.).

2. After you've done that you should go to the main dashboard on Cloudflare look at manage account and then Audit log.
You'll see an action called create or update on top where you need to get two ID's the ID of your domain and your zone-ID. 
These two in this screenshot:

3. Now you're only going to need an API key by going to your profile and going to API Tokens, making one using the template 
Edit zone DNS and selecting either all zones at Zone Resources or selecting the domain, next click on continue and create token.
Tip: Save this API Token somewhere since you can't see it again after leaving this page.

4. With this data you should be able to go to Setup script.

## Setup script

1. Download the repository using git:
   
   `git clone https://github.com/Davoto/Automatic-IP-Script.git`

2. Install python 3, pip and cron like this:

    `sudo apt install python3 python3-pip cron`

3. Use pip to install 'python-dotenv'

    `sudo pip install python-dotenv`

4. Make a file called `.env` in the folder where the script is located and fill it in like `env_example.txt` but with 
the information acquired in Setup domain.

5. Test the script by running like this:
   
   `python3 ./main.py`
   
   You will probably get a message like this:
   
   ```
   This is the local IP: *local IP*
   {Bunch of ugly json}
   ```
   Important is to look for one thing in the json that says `"succes":true` if its true you're good to go. if it's false
you should check your .env file for the correct ID's and remove the line that says LOCAL_IP="*Insert IP*" and try again.

6. Last step add the script to a crontab:

   `crontab -e`
   
   Then add to this file that opens (change the path if you downloaded the script in a different folder.):

   `0 * * * * python3 /home/"Username"/Automatic-IP-Script/main.py`
   
