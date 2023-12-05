git clone https://github.com/juba0x00/Lenovo-Legion-Battery-Guardian
cd "Lenovo-Legion-Battery-Guardian"
sudo cp lenovo-battery-guardian.py /usr/bin
sudo chmod +x /usr/bin/lenovo-battery-guardian.py
sudo cp lenovo-battery-guardian.service /etc/systemd/system/
echo "Installed Sucessfully :)"