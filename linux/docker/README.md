<div id="toc" />

## Table of content

1. [Install docker-cli for Fedora Linux distribution](#install)
2. [Run a Docker container](#run)
3. [Manage Docker](#manage)
4. [Build a Docker image](#build)
5. [Docker Volume](#docker-volume)

<div id="install" />

## Install docker-cli for Fedora Linux distribution

### Pre-installation

-   Requirement: Fedora >= 40
-   Uninstall old versions

```bash
sudo dnf remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-selinux \
                  docker-engine-selinux \
                  docker-engine
```

### Step-by-step installation

1. Install the dnf-plugins-core package (which provides the commands to manage your DNF repositories) and set up the repository.

```bash
sudo dnf -y install dnf-plugins-core
sudo dnf-3 config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
```

2. Install the latest version

```bash
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

3. Start docker engine

```bash
sudo systemctl enable --now docker
```

### Post-installation

1. Add `docker` group

```bash
sudo groupadd docker
```

2. Add `$USER` to `docker` group

```bash
sudo usermod -aG docker $USER
```

3. Config docker to start on boot with systemd

```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

Reference: [Install - Docker Docs](https://docs.docker.com/engine/install/)

<div id="run" />

## Run a docker

### Directly from the Docker's repo

```bash
docker run [ options ] image [ arg0 arg1...]
```

Run the hello-world container from the same name image.

```bash
docker run -it --name hello-world hello-world
```

Note:

-   `-d` for detached mode
-   `-it` for interactive mode

<div id="manage" />

## Manage Docker

-   List all containers. -a for a list includes stopped containers

```bash
docker container ls
```

-   List all images

```
docker image ls
```

<div id="build" />

## Build a Docker image

```bash
docker build -t username/image_name:tag path
```

For example (`.` for the current path)

```bash
docker build -t vy.tien/project:dev .
```

Building Docker image requires a Dockerfile

Example Dockerfile

```Dockerfile
FROM tomcat:7.0.105

ADD ROOT.war /usr/local/tomcat/webapps

EXPOSE 8080

CMD ["catalina.sh", "run"]
```

Common Dockerfile command list

| FROM   | Specifies the parent image from which this image is built.                                              | FROM ubuntu                      |
| ------ | ------------------------------------------------------------------------------------------------------- | -------------------------------- |
| COPY   | Copies multiple source files from the context to the file system of the container at the specified path | COPY .bash_profile /home         |
| ENV    | Sets the environment variable                                                                           | ENV HOSTNAME=test                |
| RUN    | Executes a command                                                                                      | RUN apt-get update               |
| CMD    | Defaults for an executing container                                                                     | CMD ["/bin/echo", "hello world"] |
| EXPOSE | Informs the network ports that the container will listen on                                             | EXPOSE 9999                      |

## Docker volume

### Using Volume

Store in a part of the host filesystem (`/var/lib/docker/volumes/` on Linux)
Created and managed by Docker

Use cases:

-   Sharing data among multiple running containers
-   Storing a container’s data on remote hosts or cloud providers
-   Need to backup, restore, or migrate data from one Docker host to another
-   When the Docker host is not guaranteed to have a given directory or file structure

```sh
## create and manage a volume
docker volume create myvol         ## created at /var/lib/docker/volumes/myvol
docker volume ls
docker volume rm myvol
```

Run a Docker container with a volume using `-v` or `--volume`

```bash
docker run -v myvol:/app hello-world
```

Or

```bash
docker run --mount source=myvol,target=/app hello-world
```

### Using BIND MOUNT

A file or directory on the host machine is mounted into a container

Use cases:

-   Sharing configuration files from the host machine to containers
-   Sharing source code or build artifacts between a development environment on the host machine and a container
-   When the file or directory structure of the Docker host is guaranteed to be consistent with the bind mounts the containers require

Using -v or --volume

```bash
docker run -it -v "$(pwd)"/target:/app hello-world
```

Using --mount

```bash
docker run -it --mount type=bind,source="$(pwd)"/target,target=/app hello-world
```

## Networking

Docker networking subsystem is pluggable, using drivers

Provide core networking functionality:

-   bridge: the default network driver, usually used in standalone containers to communicate
-   host: remove isolation between containers and the Docker host, use host’s networking directly
-   overlay: connect containers running on different Docker hosts together; communicate swarm services together
-   macvlan: allow to assign MAC address to a container → as a physical device
-   none: disable all networking
-   Network plugins: install and use third-party network plugins for Docker

### Using bridge

Apply to containers running on the same Docker host

Allow containers on the same bridge network to communicate --> isolate from containers on different bridge networks

A default bridge network (called `bridge`):

-   Created automatically when starting Docker → newly-started containers connect to it
-   Linked containers on the default bridge network share environment variables

User-defined custom bridge networks can also be created

**User-defined bridges:**

-   Provide better isolation and interoperability between containerized applications → expose all ports on the same user-defined bridge and no ports to the outside world
-   Provide automatic DNS resolution between containers → allow to connect via name or alias
-   Allow to attach and detach containers from user-defined networks on the fly
-   Each user-defined network creates a configurable bridge

Create and remove a user-defined bridge network

```bash
docker network create my-net
```

```bash
docker network rm my-net
```

Connect a container to a user-defined bridge network

```bash
docker run --name my_nginx --network my-net nginx
```

```bash
docker network connect my-net my-centos
```

Disconnect a container from a user-defined bridge network

```bash
docker network disconnect my-net my-nginx
```

### HOST network and NONE network

Host networking

-   Only works on Linux hosts
-   Not isolate from the Docker host when using host networking
-   Run a container with host network

```bash
docker run --rm -d --network host --name my_nginx nginx
```

None networking

-   Disable networking for a container

```bash
docker run --rm -dit --network none --name no-net-alpine alpine:latest ash
```

### Publishing port

Using `--publish` or `-p`

|          Flag value           |                                                                   Description                                                                   |
| :---------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------: |
|          -p 8080:80           |                                        Map TCP port 80 in the container to port 8080 on the Docker host.                                        |
|   -p 192.168.1.100:8080:80    |                   Map TCP port 80 in the container to port 8080 on the Docker host for connections to host IP 192.168.1.100.                    |
|        -p 8080:80/udp         |                                        Map UDP port 80 in the container to port 8080 on the Docker host.                                        |
| -p 8080:80/tcp -p 8080:80/udp | Map TCP port 80 in the container to TCP port 8080 on the Docker host, and map UDP port 80 in the container to UDP port 8080 on the Docker host. |

### IP address, hostname and DNS

|     Flag      |                                         Description                                          |
| :-----------: | :------------------------------------------------------------------------------------------: |
| --ip or --ip6 |                           To specify an IP address for a container                           |
|  --hostname   | The hostname a container uses for itself. Defaults to the container’s name if not specified. |
|    --alisa    |                            To specify an additional network alias                            |
|     --dns     |                               To specify multiple DNS servers                                |
| --dns-search  |                           To specify multiple DNS search prefixes                            |
|   --dns-opt   |                   A key-value pair representing a DNS option and its value                   |

## Docker Compose

A tool for defining and running multi-container Docker applications. Ideal for managing multiple container

Use a YAML file to configure your application’s services → create and start all the services with a single command

Work in all environments: production, staging, development, testing, as well as CI workflows.

Using Compose is basically a three-step process:

-   Define your app’s environment with a Dockerfile
-   Define the services that make up your app in docker-compose.yml
-   Run docker-compose up and Compose starts and runs your entire app.

### Sample file

```yaml
version: "3.3"
services:
    db:
        container_name: db
        image: mysql:8
        environment:
            MYSQL_DATABASE: employees
            MYSQL_USER: mysql
            MYSQL_PASSWORD: mysql
            MYSQL_ROOT_PASSWORD: supersecret
        ports:
            - 3306:3306
    web:
        image: arungupta/docker-javaee:dockerconeu17
        ports:
            - 8080:8080
            - 9990:9990
        depends_on:
            - db
```

## References

-   https://docs.docker.com/
-   http://domino.research.ibm.com/library/cyberdig.nsf/papers/0929052195DD819C85257D2300681E7B/$File/rc25482.pdf
