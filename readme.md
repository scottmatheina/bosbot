readme file

Setup SSL Cert
https://certbot.eff.org/lets-encrypt/ubuntubionic-nginx

UFW Firewall
For security reasons, I also enabled ufw firewall by doing the following:

sudo ufw enable
sudo ufw allow 'OpenSSH'
sudo ufw allow 'Nginx Full'
sudo ufw delete allow 'Nginx HTTP'
It should look something like this in sudo ufw status

To                         Action      From
--                         ------      ----
Nginx Full                 ALLOW       Anywhere
OpenSSH                    ALLOW       Anywhere
Nginx Full (v6)            ALLOW       Anywhere (v6)
OpenSSH (v6)               ALLOW       Anywhere (v6)
And its done; to start Nginx, all that’s left is to sudo nginx -t

Sending Telegram the SSL Cert
Telegram will need the other side of the cert. Consulting their documentation, it seems that they need the PEM file. To get that, I had to convert the current CRT file into the PEM format.

openssl x509 -in /etc/ssl/certs/self-signed.crt -outform pem -out /etc/ssl/certs/bot.pem
To get the cert to Telegram’s hands, I sent it via their API using this: (Replace bot keys!)

curl -F "url=https://your.domain.or.ip.com" -F "certificate=@/etc/ssl/certs/bot.pem" https://api.telegram.org/bot12345:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/setWebhook
