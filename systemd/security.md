# About sandboxing

manually create /etc/systemd/system/{service_name}.service.d/security.conf

then, put there all options related to protection i.e.:

```
[Service]
ProtectSystem=strict
ProtectHome=yes
PrivateDevices=yes
ProtectKernelTunables=yes
ProtectKernelModules=yes
ProtectControlGroups=yes
SystemCallFilter=@system-service
SystemCallErrorNumber=EPERM
NoNewPrivileges=yes
PrivateTmp=yes
```

See: https://www.redhat.com/en/blog/mastering-systemd
