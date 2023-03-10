---
title: Systemd 实战
order: 10
nav:
  title: Practices
  order: 10
group:
  title: 实战
  order: 1
---

`如何列出Linux Systemd服务`

```bash
systemctl --type=service
```

`Init script`


```python
# InitTestBootClient.py

# Write your init script code here
```


`Edit service file`



```bash
# cd /usr/lib/systemd/system

# sudo vim /usr/lib/systemd/system/InitTestBootClient.service

# InitTestBootClient.service
[Unit]
Description=InitTestBootClient
After=network-online.target

[Service]
Type=oneshot
KillMode=process


WorkingDirectory=/home/ubuntu/setup
PIDFile=/run/InitTestBootClient.pid

ExecStart=python3 /home/ubuntu/setup/InitTestBootClient.py
Restart=no

[Install]
WantedBy=multi-user.target
```


## Start service

```bash
sudo systemctl start InitTestBootClient.service
```

## Enable service

`开机启动`

```bash
systemctl enable <your service>
```


## Demon reload systemd service

```bash
# show status
sudo systemctl status InitTestBootClient.service

sudo systemctl daemon-reload
```