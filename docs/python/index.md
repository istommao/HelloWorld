---
title: 安装
order: 10
nav:
  title: Python
  order: 1
group:
  title: 基础
  order: 1
---

# 安装

### Pyenv Installation

`pyenv` 

[Raw article link](https://brain2life.hashnode.dev/how-to-install-pyenv-python-version-manager-on-ubuntu-2004)

1. Install all required prerequisite dependencies:

```bash
sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

2. Download and execute installation script:

```bash
curl https://pyenv.run | bash
```

3. Add the following entries into your ~/.bashrc file:


```bash
# pyenv
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
```

4. Restart your shell:

```bash
exec $SHELL
```

5. Validate installation:

```bash
pyenv --version
```

### Pyenv Uninstallation

1. Remove the ~/.pyenv folder

```bash
rm -fr ~/.pyenv
```

2. Delete the following entries from your ~/.bashrc file:

```bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
```

3. Restart your shell

```bash
exec $SHELL
```
