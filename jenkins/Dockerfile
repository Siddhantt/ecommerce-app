# ~/Ecom/jenkins/Dockerfile
FROM jenkins/jenkins:lts

USER root

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    ssh \
    ansible \
    docker.io

# Optional: install docker-compose if you plan to use it from Jenkins
RUN curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" \
    -o /usr/local/bin/docker-compose && chmod +x /usr/local/bin/docker-compose

USER jenkins

