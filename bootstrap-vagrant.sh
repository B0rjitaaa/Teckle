#!/bin/bash

# Get selected task
if [ "$#" -ne 1 ]; then
    task=""
else
    task=$1
fi

# Update system and install necessary packages
prepare_system() {
    apt-get update
    apt-get dist-upgrade -y
    apt-get install -y python3 python3-pip vim dos2unix postgresql-9.3 postgresql-server-dev-9.3 postgresql-contrib-9.3 gettext libjpeg-dev
}

# Install necessary python packages
install_python_packages() {
    pip3 install -r /vagrant/requirements.txt
}

# Create PostgreSQL config
set_postgresql() {
    sudo su -l postgres -c "createuser developer -w -s"
    sudo su -l postgres -c "dropdb teckle"
    sudo su -l postgres -c "createdb teckle"
    sudo su -l postgres -c "psql -c \"ALTER USER developer WITH PASSWORD 'developer';\""
    sudo su -l postgres -c "psql -c \"GRANT ALL PRIVILEGES ON DATABASE teckle TO developer;\""
}

# Resets db with minimal initial data
prepare_db() {
    set_postgresql
    python3 manage.py migrate
    # python3 manage.py loaddata initial_shop
    # python3 manage.py loaddata initial_admins
    python3 manage.py runserver 0.0.0.0:8000
}


case ${task} in
    1) prepare_system
    ;;
    2) install_python_packages
    ;;
    3) set_postgresql
    ;;
    4) prepare_db
    ;;
    "") prepare_system
        install_python_packages
        set_postgresql
    ;;
esac
