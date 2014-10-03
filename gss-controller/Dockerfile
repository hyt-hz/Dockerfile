FROM hythz/centos:gss-base0.1
MAINTAINER Yiting Huang <hyt1981@gmail.com>

ADD controller.yaml /etc/gss/
ADD logging.yaml /etc/gss/
VOLUME ["/root/src", "/var/log/gss"]
EXPOSE 9000
ENTRYPOINT ["/opt/python27/bin/gss_controller", "-fg"]

# launch it like
# docker run -ti -v /home/core/src/gss:/root/src -v /home/core/logs/gss:/var/log/gss --link redis-gss:redis --name gss-controller hythz/centos:gss-controller
