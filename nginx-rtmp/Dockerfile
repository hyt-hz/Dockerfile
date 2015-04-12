# docker build --tag hythz/nginx-rtmp:1.1.7 .
# docker run -d -p 1935:1935 -p 80:80 --name nginx-rtmp hythz/nginx-rtmp:1.1.7
# docker run -it -p 1935:1935 -p 80:80 --name nginx-rtmp -v /home/core/flv:/root/flv hythz/nginx-rtmp:1.1.7 /bin/bash
FROM centos:centos7
MAINTAINER Yiting Huang <hyt1981@gmail.com>

RUN yum -y install gcc make wget tar unzip pcre-devel openssl-devel && \
  yum clean packages && yum clean headers && yum clean metadata && yum clean all && \
  cd /root && \
  wget https://github.com/arut/nginx-rtmp-module/archive/v1.1.7.zip && unzip v1.1.7.zip && rm -f v1.1.7.zip && \
  wget http://nginx.org/download/nginx-1.6.3.tar.gz && tar zxvf nginx-1.6.3.tar.gz && rm -f nginx-1.6.3.tar.gz && \
  cd nginx-1.6.3 && ./configure --prefix=/root/nginx --add-module=/root/nginx-rtmp-module-1.1.7/ && \
  make && make install && \
  cd .. && rm -rf nginx-rtmp-module-1.1.7 nginx-1.6.3.tar.gz nginx-1.6.3
  
WORKDIR /root/nginx
EXPOSE 1935 1935 80
CMD sbin/nginx
