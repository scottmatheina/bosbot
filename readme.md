*Initial Setup*
Install dependency

$ sudo apt-get install python-requests

If you get a SSL_ST_INIT error

    do the following
        $ apt-get --auto-remove --yes remove python-openssl
        $ python -m pip install --user --upgrade cryptography
        $ python -m pip install pyOpenSSL --user
    this should fix the requests error

Install python-telegram-bot
    https://github.com/python-telegram-bot/python-telegram-bot

    The code can be ran from local or remote server, but once you have a working
    script, you'll want to run it on a server to keep it active all the time.
    Doesn't matter where, but I use Ubuntu 18.04 LTS for this project, so probably
    want to stick to that, so all the instruction work out for you.


Add systemd service

Create bot.service

$ cat <<EOT >> /root/systemd/system/bot.service
[Unit]
Description=Telegram Bot
After=multi-user.target

[Service]
Type=simple
Environment="TOKEN=<token>"
ExecStart=/usr/bin/python /root/bosbot/bot.py
Restart=on-abort

[Install]
WantedBy=multi-user.target
EOT

$ sudo chmod 644 /etc/systemd/system/bot.service
$ chmod +x /root/bosbot/bot.py
$ sudo systemctl daemon-reload
$ sudo systemctl enable bot.service
$ sudo systemctl start bot.service

*Check the service is running*
    $ service --status-all

*only for webHook  (optional)*
Setup SSL Cert & nginx
    https://certbot.eff.org/lets-encrypt/ubuntubionic-nginx

start nginx
    $ sudo nginx -t

UFW Firewall
    For security reasons, I also enabled ufw firewall by doing the following:

    $ sudo ufw enable
    $ sudo ufw allow 'OpenSSH'
    $ sudo ufw allow 'Nginx Full'
    $ sudo ufw delete allow 'Nginx HTTP'

ufw status
    It should look something like this in sudo ufw status

    To                         Action      From
    --                         ------      ----
    Nginx Full                 ALLOW       Anywhere
    OpenSSH                    ALLOW       Anywhere
    Nginx Full (v6)            ALLOW       Anywhere (v6)
    OpenSSH (v6)               ALLOW       Anywhere (v6)
    And its done; to start Nginx, all that’s left is to $ sudo nginx -t

Sending Telegram the SSL Cert
    Telegram will need the other side of the cert.

$ curl -F "url=https://bosbot.cyiber.com" -F \
"certificate=@/etc/letsencrypt/live/bosbot.cyiber.com/cert.pem" \
https://api.telegram.org/bot<token>/setWebhook


## BOT Current features

- Post announcement and welcome when new user joins
- Delete harsh language focused on attacking others. See bot.py for list.
- Delete spam post with links, based on keywords.
- Delete all /commands no used in chat, yet.



