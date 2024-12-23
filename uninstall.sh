#!/bin/bash
set -euo pipefail

git clone https://github.com/juba0x00/Lenovo-Legion-Battery-Guardian
cd "Lenovo-Legion-Battery-Guardian"
sudo systemctl disable lenovo-battery-guardian.service --now
sudo rm /usr/bin/lenovo-battery-guardian.py
sudo rm /etc/systemd/system/lenovo-battery-guardian.service
echo "Uninstalled Sucessfully :)"
