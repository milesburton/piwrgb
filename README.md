# piwrgb
Experimentation only


# Preinstall
* Download Raspbien lite for Pi Zero W (Either 2 or 3)
* Preconfigure the OS template with your SSH key, WiFi Creds etc
* On first boot install deps
```
 sudo apt update --fix-missing && sudo apt -y install
 sudo apt install -y python3-pip git
 sudo python3 -m venv .venv
 sudo source .venv/bin/activate
 sudo pip3 install --break-system-packages rpi_ws281x adafruit-circuitpython-neopixel
 sudo python3 -m pip install --force-reinstall adafruit-blinka

 sudo apt update
 sudo apt install -y nodejs npm # You may need to uncomment the additional repos in /etc/apt/sources.list as node may be removed in the legacy repos in this distro


 git clone https://github.com/milesburton/piwrgb
```
