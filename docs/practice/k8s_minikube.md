---
title: Kubernetes minikube
order: 10
nav:
  title: Practices
  order: 10
group:
  title: 实战
  order: 1
---

`minikube`

- Github: https://github.com/kubernetes/minikube
- Website: https://minikube.sigs.k8s.io/docs/start/


`Install`

```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64

sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

`Init`

1. Create the docker group.

    `sudo groupadd docker`

2. Add your user to the docker group.

    `sudo usermod -aG docker $USER`

    `newgrp docker`

3. Add your user to the 'docker' group
    `sudo usermod -aG docker $USER && newgrp docker`

```bash
minikube start
```