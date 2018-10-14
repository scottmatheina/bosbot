readme file

Setup SSL Cert & nginx
https://certbot.eff.org/lets-encrypt/ubuntubionic-nginx

start nginx
$ sudo nginx -t

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
Telegram will need the other side of the cert.

curl -F "url=https://bosbot.cyiber.com" -F "certificate=@/etc/letsencrypt/live/bosbot.cyiber.com/cert.pem" https://api.telegram.org/bot672249649:AAEbolWMT35jPdrdKyJEe6Qxq_44bwiqk8o/setWebhook
