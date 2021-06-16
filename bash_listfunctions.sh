#!/bin/bash
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# script a développer pour lister des #
# fonctions bash propulsé par KoS_    #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#load loopback
if [ "$1" == "" ] ; then
	echo " <script> est null"
  echo "Usage: $0 <script>"
else
  # list functions in script
  echo "Scanning $1 ..."
  grep -E '^[[:space:]]*([[:alnum:]_]+[[:space:]]*\(\)|function[[:space:]]+[[:alnum:]_]+)' $1
fi
