deps:
	cd /vagrant/consul
	#wget -q -nc https://releases.hashicorp.com/consul/0.6.3/consul_0.6.3_linux_amd64.zip
	wget -q -nc https://releases.hashicorp.com/consul/1.0.0/consul_1.0.0_linux_amd64.zip
	#wget -q -nc https://releases.hashicorp.com/consul/0.6.3/consul_0.6.3_web_ui.zip
	#new consul comes with webui
	wget -q -nc https://github.com/cbednarski/hostess/releases/download/v0.1.0/hostess_linux_amd64
	apt-get update -qq
	apt-get install -y unzip
	#unzip -o consul_0.6.3_linux_amd64.zip
	#unzip -o consul_0.6.3_web_ui.zip -d dist
	unzip -o consul_1.0.0_linux_amd64.zip
install:
	cd /vagrant/consul
	# Install hostess so we can edit the hosts file
	cp hostess_linux_amd64 /usr/local/bin/hostess
	chmod +x /usr/local/bin/hostess

	# Get IP address of the current machine from eth1
	ifconfig enp0s8 | grep "inet addr" | awk 'BEGIN { FS = "[ :]+" }{print $$4}' > /tmp/self.ip
	#hostname -I | awk \'{print $1}\' > /tmp/self.ip
	hostess add consul `cat /tmp/self.ip`

	# Install consul binaries
	stop consul || true
	cp /vagrant/consul/consul /usr/local/bin/consul

	# Install consul UI
	#mkdir -p /opt/consul-ui
	#cp -R /vagrant/consul/dist/* /opt/consul-ui

	# Add consul configuration
	mkdir -p /etc/consul
	mkdir -p /var/lib/consul

install-server:
	cd /vagrant/consul
	sed 's/ADDR/'`cat /tmp/self.ip`'/g' /vagrant/consul/consul-server.json > /etc/consul/consul.json

	# Setup consul service and start it
	cp /vagrant/consul/consul.service /etc/systemd/system/consul.service
	systemctl start consul
	systemctl enable consul
	sleep 1

install-client:
	cd /vagrant/consul
	sed 's/ADDR/'`cat /tmp/self.ip`'/g' /vagrant/consul/consul-client.json > /etc/consul/consul.json

	# Setup consul service and start it
	cp /vagrant/consul/consul.service /etc/systemd/system/consul.service
	systemctl start consul
	systemctl enable consul
	sleep 1
