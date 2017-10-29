# pull base image
FROM debian:jessie
MAINTAINER haddadian.hamed@gmail.com
# install Java
RUN \
    apt-get update && \
    apt-get install wget -y && \
    wget --no-cookies --no-check-certificate --header "Cookie: oraclelicense=accept-securebackup-cookie"  http://download.oracle.com/otn-pub/java/jdk/9.0.1+11/jdk-9.0.1_linux-x64_bin.tar.gz -O jdk-9.0.1.tar.gz && \
    tar -xvzf jdk-9.0.1.tar.gz -C /opt/ && \
    update-alternatives --install /usr/bin/java java /opt/jdk-9.0.1/bin/java 100 && \
    update-alternatives --install /usr/bin/javac javac /opt/jdk-9.0.1/bin/javac 100
    

CMD ["java"]
