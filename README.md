# Lenovo-Legion-Battery-Guardian
Optimize your Legion laptop's battery life with this tool that automatically manages battery charging to prevent overcharging and extend battery lifespan.


## install
```bash
curl https://raw.githubusercontent.com/juba0x00/Lenovo-Legion-Battery-Guardian/main/install.sh | bash
```

## uninstall
```bash
curl https://raw.githubusercontent.com/juba0x00/Lenovo-Legion-Battery-Guardian/main/uninstall.sh | bash
```

You can check the status of this service with:
```bash
systemctl status lenovo-battery-guardian.service
```

To follow its log:

```bash
journalctl -f -u lenovo-battery-guardian.service
```
