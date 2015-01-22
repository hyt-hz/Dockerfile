# docker build --tag hythz/shadowsocks .
# docker run -d -p 9090:9090 --name ssserver hythz/shadowsocks

FROM centos:centos7
MAINTAINER Yiting Huang <hyt1981@gmail.com>

# install gcc gdb and more
RUN yum -y install gcc python-devel epel-release && \
  yum -y install python-pip && \
  pip install gevent shadowsocks && \
  echo '{"server":"0.0.0.0", "server_port":9090,' > /root/sss.json && \
  echo '"local_port":1080, "password":"hyt_hz",' >> /root/sss.json && \
  echo '"timeout":600, "method":"aes-256-cfb"}' >> /root/sss.json && \
  yum -y remove gcc python-devel

WORKDIR /root
EXPOSE 9090
CMD ssserver -c /root/sss.json
