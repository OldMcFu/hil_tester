FROM debian

RUN apt update -y
RUN apt upgrade -y

RUN apt install curl python3 python3-pytest python3-fabric iproute2 openssh-server openssh-client rsync -y

RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Authorize SSH Host
RUN mkdir -p /root/.ssh && \
    chmod 0700 /root/.ssh

COPY  id_rsa /root/.ssh/id_rsa
COPY  id_rsa.pub /root/.ssh/id_rsa.pub
RUN cat ~/.ssh/id_rsa.pub  >> ~/.ssh/authorized_keys

RUN touch /etc/ssh/ssh_config
RUN echo 'Host 20.0.0.*' >> /etc/ssh/ssh_config
RUN echo '   StrictHostKeyChecking no' >> /etc/ssh/ssh_config
RUN echo '  UserKnownHostsFile=/dev/null' >> /etc/ssh/ssh_config

COPY container_start_script.sh /root/container_start_script.sh