# docker build --tag hythz/monaserver:1.0 .
# docker run -d -p 1935:1935 -p 1935:1935/udp -p 80:80 --name mona hythz/monaserver:1.0
# docker run -it -p 1935:1935 -p 1935:1935/udp -p 80:80 --name mona hythz/monaserver:1.0 /bin/bash
FROM centos:centos7
MAINTAINER Yiting Huang <hyt1981@gmail.com>

RUN yum -y install gcc-c++ openssl-devel make wget tar unzip && \
  yum clean packages && yum clean headers && yum clean metadata && yum clean all && \
  cd /root && \
  # MonaServer requires Luajit 
  wget http://luajit.org/download/LuaJIT-2.0.3.tar.gz && tar -zxvf LuaJIT-2.0.3.tar.gz && \
  cd LuaJIT-2.0.3 && make && make install && cd .. && rm -rf LuaJIT-2.0.3 && rm -f LuaJIT-2.0.3.tar.gz && \
  # download and build MonaServer 1.0
  wget https://github.com/MonaSolutions/MonaServer/archive/1.0.zip && unzip 1.0.zip && rm -f 1.0.zip && \
  cd MonaServer-1.0/ && make && cd ..
  
WORKDIR /root/MonaServer-1.0/MonaServer
EXPOSE 1935 1935/udp 80
CMD ./MonaServer
