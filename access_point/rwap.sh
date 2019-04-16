#!/bin/bash

if [ "$EUID" -ne 0 ]
	then echo "Must be root"
	exit
fi

# stop and disable hostapd, it cannot run once we have set up wifi
# and would be re-enabled in wap.sh if necessary
systemctl stop hostapd
systemctl disable hostapd

cd /etc/hostapd/
cp hostapd.conf hostapd.conf.bak
sed -i '1,14d' hostapd.conf

rm -f /etc/network/interfaces.d/wlan-hostap
cp /etc/network/interfaces.d/wlan.client /etc/network/interfaces.d/wlan-client

#Empty port 5000
#Remove the server file from auto-boot
systemctl enable ss-startup-audio.service
systemctl enable ss-susi-linux.service
systemctl disable ss-python-flask.service
systemctl enable ss-susi-login.service

echo "Reboot in 10sec"
sleep 10;
reboot

