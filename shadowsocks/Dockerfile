# docker build --tag hythz/shadowsocks:1.0 .
# docker run -d -p 9090:9090 --name ssserver --restart=always hythz/shadowsocks:1.0

FROM centos:centos7
MAINTAINER Yiting Huang <hyt1981@gmail.com>

# install gcc gdb and more
RUN yum -y install epel-release python-gevent && \
  yum -y install python-pip && \
  yum clean packages && yum clean headers && yum clean metadata && yum clean all && \
  pip install shadowsocks && \
  echo '{"server":"0.0.0.0", "server_port":9090,' > /root/sss.json && \
  echo '"local_port":1080, "password":"hyt_hz",' >> /root/sss.json && \
  echo '"timeout":600, "method":"aes-256-cfb"}' >> /root/sss.json

WORKDIR /root
EXPOSE 9090
CMD ssserver -c /root/sss.json
