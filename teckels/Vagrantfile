# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
# VAGRANTFILE_API_VERSION = "2"

Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/trusty32"
  config.vm.provision :shell, path: "bootstrap-vagrant.sh"

  config.vm.network :forwarded_port, host: 8000, guest: 8000
  config.vm.network "private_network", ip: "192.168.33.12"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = 1024
  end

end
