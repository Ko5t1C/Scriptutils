#!/bin/bash
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# script a développer pour lancer des #
#       machines docker et gérer ses  #
#       modules propulsé par KoS_     #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
entrechat () {
  docker run -it -p 80:80/tcp -p 443:443/tcp -p 3333-3334:3333-3334/tcp -p 5000:5000 \
	-p 5568:5568/tcp -p 6667:6667/tcp -p 6697:6697/tcp -p 8008:8008 -p 8448:8448 -p 8080:8081/tcp \
	-p 8081:8081/tcp -p 7000:7000/tcp -p 7001:7001 -p 22110:22110/tcp mam3n/entrechat
}
#load loopback
if [ "$1" = "entrechat" ] ; then
	entrechat
#unload loopback
elif [ "$1" = "sfm" ] ; then
	echo "nope now"
#list modules
elif [ "$1" = "couturiere" ] ; then
	echo "nope now"
else
	echo "Usage: $0 load|unload|list"
fi
