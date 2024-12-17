<div id="toc" />

## Table of content

1. [Install docker-cli for Fedora Linux distribution](#install)
2. [Run a Docker container](#run)
3. [Manage Docker](#manage)
4. [Build a Docker image](#build)

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
- `-d` for detached mode
- `-it` for interactive mode

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