FROM alpine

RUN apk update
RUN apk add rsync openssh

ADD entrypoint.sh /
ADD ssh /root/.ssh
RUN chmod 600 /root/.ssh/id_rsa

CMD /entrypoint.sh
