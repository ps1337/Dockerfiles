# Create a directory in /var/backups called "borg" in order to put the repository (server side)
# Will be the base to the server and the client version of the container

FROM debian:latest

# Prepare environment, create user, etc...
ENV LANG C.UTF-8
RUN ln -sf /usr/share/zoneinfo/Europe/Berlin /etc/localtime

RUN adduser --disabled-password --gecos "Borg Backup" --quiet borg && \
    mkdir -p /var/run/sshd && \
    mkdir -p /var/backups/borg && \
    mkdir -p /home/borg/.ssh && \
    mkdir -p /home/borg/data

RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update -y \
    && apt-get install -y \
        build-essential \
        fuse \
        libacl1-dev \
        libfuse-dev \
        liblz4-dev \
        liblzma-dev \
        libssl-dev \
        openssh-server \
        pkg-config \
        python3-virtualenv \
        python3-dev \
        python3-pip \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# Some more clean
RUN rm -f /etc/ssh/ssh_host_*

# Remove Password authentication and disable root login from ssh configuration
RUN sed -i -e 's/^#PasswordAuthentication yes$/PasswordAuthentication no/g' \
           -e 's/^PermitRootLogin without-password$/PermitRootLogin no/g' \
          /etc/ssh/sshd_config


# Install Borg
RUN pip3 -v --log=/var/log/pip-install.log install borgbackup && \
    apt-get remove -y --purge build-essential libssl-dev libacl1-dev && \
    apt-get autoremove -y --purge

COPY entrypoint.sh /borg-server.sh
RUN chmod +x /borg-server.sh

ENTRYPOINT ["/borg-server.sh"]
CMD ["start"]
