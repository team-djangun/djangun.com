#!/bin/bash

SHELL_PATH=`pwd -P`
name=`whoami`
appname=${1}
created_path=$SHELL_PATH/${appname}
NAME_OF_PWD=${PWD##*/}
destinaton_path=$SHELL_PATH/${NAME_OF_PWD}

echo -e ${appname}" app is will be created. starting...\n\n"

echo -e ${created_path}" is creating path. please check.\n"
read -r -p "Is it right? [Y/n] " response
case "$response" in
    [yY][eE][sS]|[yY])
        echo "docker-compose -f local.yml run --rm django python manage.py startapp ${appname}"
        docker-compose -f local.yml run --rm django python manage.py startapp ${appname}
        echo "sudo chown ${name}:${name} ${created_path}"
        sudo chown -R ${name}:${name} ${created_path}
        echo "mv ${created_path} ${destinaton_path}/${appname}"
        mv ${created_path} ${destinaton_path}/${appname}
        ;;
    *)
        echo "Interrupted."
        exit
        ;;
       
esac