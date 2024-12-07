---
title: Daily report
order: 10
nav:
  title: Daily report
  order: 10

---

## 2024-12

### 12-7


`marimo 一个替代 python notebook jupyter的项目`

```shell
pip install marimo
```

```shell
marimo edit --host 0.0.0.0 --no-token
```

![alt text](./python-marimo.png)

## 2024-3

### 3-6

Golang调用cloudflare设置子域名

```go
import (
    "context"
    "github.com/cloudflare/cloudflare-go"
)

func CreateDnsRecord(CLOUDFLARE_API_TOKEN string, zoneId string, domain string, content string, proxiable bool, proxied bool) (cloudflare.DNSRecord, error) {
   
    api, err := cloudflare.NewWithAPIToken(CLOUDFLARE_API_TOKEN)
    if err != nil {
        log.Fatal(err)
    }

    params := cloudflare.CreateDNSRecordParams{
        Type: "A",
        Name: domain,
        // TTL:     120,
        Content:   content, // ip address
        Proxiable: proxiable,
        Proxied:   &proxied,
    }

    // Most API calls require a Context
    ctx := context.Background()
    record, err := api.CreateDNSRecord(ctx, cloudflare.ZoneIdentifier(zoneId), params)
    if err != nil {
        log.Fatal(err)
    }

    return record, err
}
```

## 2024-2

### 2-29

Golang调用AWS启动EC2

```go
import (
    "context"
    "fmt"
    "time"

    "github.com/aws/aws-sdk-go-v2/aws"
    "github.com/aws/aws-sdk-go-v2/config"
    "github.com/aws/aws-sdk-go-v2/credentials"
    "github.com/aws/aws-sdk-go-v2/service/ec2"
    "github.com/aws/aws-sdk-go-v2/service/ec2/types"
)

func GetEC2Client(AWSAccessKeyID string, SecretAccessKey string, region string) (*ec2.Client, error) {
    cfg, err := config.LoadDefaultConfig(
        context.TODO(),
        config.WithDefaultRegion(region),
        config.WithCredentialsProvider(credentials.NewStaticCredentialsProvider(AccessKeyID, SecretAccessKey, "")),
    )
    if err != nil {
        return nil, err
    }

    ec2Client := ec2.NewFromConfig(cfg)
    return ec2Client, nil
}

func CreateAWSEC2(ec2Client *ec2.Client, instanceName string, count int32) (types.Instance, error) {
    ctx := context.Background()

    imageId := "" // Amazon Linux AMI
    KeyName := ""    // key pairs name
    securityGroupId := ""
    subnetId := ""

    input := &ec2.RunInstancesInput{
        MaxCount:       aws.Int32(count),
        MinCount:       aws.Int32(count),
        DisableApiStop: aws.Bool(false),
        ImageId:        &imageId,
        InstanceType:   types.InstanceTypeT2Small,
        KeyName:        &KeyName,
        NetworkInterfaces: []types.InstanceNetworkInterfaceSpecification{
            {
                AssociatePublicIpAddress: aws.Bool(true),
                DeleteOnTermination:      aws.Bool(true),
                DeviceIndex:              aws.Int32(0),
                Groups: []string{
                    securityGroupId,
                },
                InterfaceType:    aws.String("interface"),
                NetworkCardIndex: aws.Int32(0),
                SubnetId:         &subnetId,
            },
        },
        TagSpecifications: []types.TagSpecification{
            {
                ResourceType: types.ResourceTypeInstance,
                Tags: []types.Tag{
                    {
                        Key:   aws.String("Name"),
                        Value: aws.String(instanceName),
                    },
                },
            },
        },
    }

    output, err := ec2Client.RunInstances(ctx, input)
    if err != nil {
        return types.Instance{}, err
    }

    waiter := ec2.NewInstanceRunningWaiter(ec2Client)
    describeInput := &ec2.DescribeInstancesInput{
        InstanceIds: []string{aws.ToString(output.Instances[0].InstanceId)},
    }
    maxWaitDur := 360 * time.Second
    describeOutput, err := waiter.WaitForOutput(ctx, describeInput, maxWaitDur)
    if err != nil {
        return types.Instance{}, err
    }

    instance := describeOutput.Reservations[0].Instances[0]
    fmt.Println(*instance.InstanceId)
    fmt.Println(*instance.SubnetId)
    fmt.Println(*instance.NetworkInterfaces[0].NetworkInterfaceId)
    fmt.Println(*instance.PublicIpAddress)
    fmt.Println(*instance.PrivateIpAddress)

    return instance, nil
}
```


## 2023-12

- git 免输入用户名密码

```bash
cd ~
touch .git-credentials
vim .git-credentials
https://{username}:{password}@github.com
```

```bash
git config --global credential.helper store

# 打开~/.gitconfig文件，会发现多了一项:
# [credential]
# helper = store
```
-其实直接执行“git config --global credential.helper store”，然后调用一次“git push xxx”操作，输入一次账户和密码之后，git就会自动生
成一个.git-credentials文件，然后将本次的账号密码信息保存进文件中。

## 2023-11

- [Rust web实践](/practice/rust_web)

基于 ntex + sea-orm 实现rust web demo

- https://ntex.rs/
- https://github.com/SeaQL/sea-orm


## 2023-10

- install script

```bash
#!/usr/bin/env bash
set -e

echo Installing ioboard...

BASE_DIR=${XDG_CONFIG_HOME:-$HOME}
IOBOARD_DIR=${IOBOARD_DIR-"$BASE_DIR/.ioboard"}

IOBOARD_BIN_DIR="$IOBOARD_DIR/bin"
IOBOARD_MAN_DIR="$IOBOARD_DIR/share/man/man1"

echo ${BASE_DIR}

BIN_URL="https://raw.githubusercontent.com/istommao/ioboard/main/ioboard"
BIN_PATH="$IOBOARD_BIN_DIR/ioboard"


# Create the .ioboard bin directory and ioboard binary if it doesn't exist.
mkdir -p $IOBOARD_BIN_DIR
curl -# -L $BIN_URL -o $BIN_PATH
chmod +x $BIN_PATH

# Create the man directory for future man files if it doesn't exist.
mkdir -p $IOBOARD_MAN_DIR


# Store the correct profile file (i.e. .profile for bash or .zshenv for ZSH).
case $SHELL in
*/zsh)
    PROFILE=${ZDOTDIR-"$HOME"}/.zshenv
    PREF_SHELL=zsh
    ;;
*/bash)
    PROFILE=$HOME/.bashrc
    PREF_SHELL=bash
    ;;
*/fish)
    PROFILE=$HOME/.config/fish/config.fish
    PREF_SHELL=fish
    ;;
*/ash)
    PROFILE=$HOME/.profile
    PREF_SHELL=ash
    ;;
*)
    echo "ioboard: could not detect shell, manually add ${IOBOARD_BIN_DIR} to your PATH."
    exit 1
esac


# Only add ioboard if it isn't already in PATH.
if [[ ":$PATH:" != *":${IOBOARD_BIN_DIR}:"* ]]; then
    # Add the ioboard directory to the path and ensure the old PATH variables remain.
    echo >> $PROFILE && echo "export PATH=\"\$PATH:$IOBOARD_BIN_DIR\"" >> $PROFILE
fi

echo && echo "Detected your preferred shell is ${PREF_SHELL} and added ioboard to PATH. Run 'source ${PROFILE}' or start a new terminal session to use ioboard."
echo "Then, simply run 'ioboard' to install ioboard."

```

## 2023-07

### 7-11

- `Git clone 指定使用ssh private key`

```bash
git -c core.sshCommand="ssh -i ~/.ssh/<your_ssh_private_key>" clone git@github.com:<YourProject>
```

## 2023-05

### 5-19

- `Python Project Wizard`

*cookiecutter*

https://github.com/cookiecutter/cookiecutter

[使用cookiecutter来创建新项目]

https://note.qidong.name/2018/10/cookiecutter/

## 2023-04

### 4-7

`磁盘挂载`

```bash
# 新建dir
sudo mkdir /data

# 查看磁盘分区表
sudo fdisk -l

# blkid - locate/print block device attributes
sudo blkid

# 编辑 fstab file
sudo vim /etc/fstab
# UUID=<blkid 查看对应设备的id>       /data   ext4    defaults        0 0

# 挂载
sudo mount -a
```

### 4-6

`Copy data from one talbe to another`

```bash
INSERT INTO Destination SELECT * FROM Source;
```


## 2023-03


### 3-23 Python poetry


`Poetry`

> 是一个Python虚拟环境和依赖管理工具，另外它还提供了包管理功能，比如打包和发布。可以用来管理python库和python程序。


- [Python poetry实践](/python/poetry)


### 3-22 Telegram bot

`Python`

- [Telegram bot最小demo](/python/telegram_bot)


### 3-16 K8s minikube

`Install minikube`

Website: https://minikube.sigs.k8s.io/docs/start/


- [minikube实战](/practice/k8s_minikube)


### 3-15 PostgreSQL

`Install`

```bash
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

sudo apt-get update

sudo apt-get -y install postgresql
```

`Start`

```bash
sudo /etc/init.d/postgresql start  
sudo /etc/init.d/postgresql stop   
sudo /etc/init.d/postgresql restart
```

`Create`

```bash
sudo -i -u postgres

$ psql
postgres=#

现在位于数据库提示符下。

2、创建数据库新用户，如 dbuser：

postgres=# CREATE USER dbuser WITH PASSWORD '*****';
注意：

语句要以分号结尾。
密码要用单引号括起来。
3、创建用户数据库，如exampledb：

postgres=# CREATE DATABASE exampledb OWNER dbuser;
4、将exampledb数据库的所有权限都赋予dbuser：

postgres=# GRANT ALL PRIVILEGES ON DATABASE exampledb TO dbuser;
5、使用命令 \q 退出psql：

postgres=# \q
```


### 3-13 MongoDB

`Install`

```bash
brew tap mongodb/brew

brew install mongodb-community@6.0
```

### 3-12 Linux Command

`Get my ip`

```bash
curl ifconfig.me

# or
curl ifconfig.me/all
```


### 3-11 Linux Command

`netstat`

tcp 统计

```bash
# install
apt install net-tools
```

`TCP stats 1`

```bash
netstat -s -t | sed -e '/Tcp:/!d;:l;n;/^\ /!d;bl'

# output
Tcp:
    103728 active connection openings
    101462 passive connection openings
    141 failed connection attempts
    106936 connection resets received
    3 connections established
    353276068 segments received
    353175097 segments sent out
    77587 segments retransmitted
    14 bad segments received
    75744 resets sent
```

`TCP stats 2`

```bash
netstat -na | awk '/^tcp/ {++S[$NF]} END {for(a in S) print a, S[a]}'

# output
LISTEN 29
LAST_ACK 1
CLOSE_WAIT 7
TIME_WAIT 16
ESTABLISHED 72
```

### 3-10 systemd

`systemd` 简单实践


- [systemd实战](/practice/systemd)


### 3-9 locust + boomer

> 基于 locust + boomer 实现高并发压力测试

https://github.com/myzhan/boomer

- [locust + boomer 压测实战](/practice/locust_boomer)

### 3-8 Astro 2.0 正式发布


> Astro 是一个现代化的轻量级静态站点生成器，用于构建以内容为中心的高性能网站

[Astro 2.0正式发布](https://mp.weixin.qq.com/s/Z3YA9dp5p3PkLm3sePfFJA)

#### Bun


> Bun is a modern JavaScript runtime, built from scratch to serve the modern JavaScript focus on three main things:

`Install bun`

```bash
curl -fsSL https://bun.sh/install | bash
```

`Demo`

```js
// http.js
export default {
  port: 3000,
  fetch(request) {
    return new Response("Welcome to Bun!");
  },
};
```

`Run`

```bash
bun run http.js
```


### 3-3 Python

`asyncio queue`

- [asyncio queue](/python/async_queue)


### 3-2 Go

`sync & atomic`

- [sync & atomic](/golang/sync_mutex)

### 3-1 `TestFramework locust`

`TestFramework`

- [locust](/practice/locust)

## 2023-02

### 2-28 Python

`Python`

- [Async Websocket Client Demo](/python/async_websocket)

### 2-27 Algo & Python

`Python`
- [Discord bot最小demo](/python/discord_bot)

`Algo`
- [最小栈 - 使用两个栈实现](/algo/min_stack)


### 2-26 Algo

`pypi`
- https://github.com/istommao/algolibs

`Algo 循环链表`

- [反转链表](/algo/reverse_linked_list)
- [循环链表](/algo/linked_list)
  - 如何判断链表有环
      - 快慢指针（类似操场跑步，跑的快的人最终会套圈（两个指针指向相同节点）
  - 如何找出循环链表的入环点
      - 先使用快慢指针，当两个节点指向相同节点后，fast节点从根节点开始
      - fast与slow节点同时一步一步向下一个节点走，下次两个节点相遇时，就是入环点

`https://leetcode.cn/problems/linked-list-cycle-ii/`

### 2-24 Go

`Go`

- [MPG模型](/golang/mpg)
- [GC](/golang/gc)

`Algo`

- [双链表](/algo/linked_list)
- [循环链表](/algo/linked_list)

### 2-23 Algo


`算法`

- [单链表](/algo/linked_list)
  - 删除倒数第K个节点 (快慢指针)

### 2-22 kuma


>  A fancy self-hosted monitoring tool

- Github: https://github.com/louislam/uptime-kuma
- Website: uptime.kuma.pet

```bash
# Run
docker run -d --restart=always -p 3001:3001 -v uptime-kuma:/app/data --name uptime-kuma louislam/uptime-kuma:1
```

![daily-report-2023-2-22](./daily-report-2023-2-22.jpeg)
