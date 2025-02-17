# HOW-To

* [unit file specifiers](https://www.freedesktop.org/software/systemd/man/latest/systemd.unit.html#Specifiers)

## 1. user service

### installation
   ```
   cp your.service ~/.config/systemd/user/
   systemctl --user enable your.service
   systemctl --user daemon-reload
   systemctl --user start your.service
   ```

> note: use %h specifier for %HOME dir

## 2. system service

### installation
```
cp your.service /etc/systemd/system/
systemctl enable your.service
systemctl start your.service
```

### run as User (example)
```
[Service]
User=you
WorkingDirectory=/home/you/.service
```
