#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys, getopt, time
# from Discordbot import Discordbot
#from Webpanel import Webpanel


def writePidFile( folder ):
	pid = str(os.getpid())
	f = open(folder + '/docker.pid', 'w')
	#print('folder + /docker.pid = ' + folder + '/docker.pid')
	f.write(pid)
	f.close()

def createFolder(MYDIR):
	# You should change 'test' to your preferred folder.
	#MYDIR = ("log")
	CHECK_FOLDER = os.path.isdir(MYDIR)

	# If folder doesn't exist, then create it.
	if not CHECK_FOLDER:
		os.makedirs(MYDIR)
		print("folder : ", MYDIR, " not exist")
		print("created folder : ", MYDIR)
		writePidFile(MYDIR)
	else:
		print(MYDIR, "folder already exists.")
		writePidFile(MYDIR)


def start(argv):
	MYDIR = 'log'
	createFolder(MYDIR)
	dockerlog = MYDIR + '/docker'
	createFolder(dockerlog)
	writePidFile(dockerlog)
	# ircbot = IRCBot( "192.168.1.58", 6667, "Pooshy-Nu", "#socket.log" )
	# ircbot.run()
	#socketservice = IRCService( "172.17.0.1", 7000, "Pooshy-Mu", "#socket.log", argv )
	#socketservice.run()
	# discordb = Discordbot("8888")
	# discordb.run()
	# webp = Webpanel("8888")
	# webp.run()

def main(argv):
	debug = ''
	try:
		opts, args = getopt.getopt(argv,"hd:",["debug="])
	except getopt.GetoptError:
		print('Usage : python3 ' + sys.argv[0] +  ' [OPTION]...[PARAMETER]...')
		print('-d, --debug specify debug mode level [0-10]')
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			print('Usage : python3 ' + sys.argv[0] +  ' [OPTION]...[PARAMETER]...')
			print('-d, --result specify debug mode level [0-10]')
			sys.exit(arg)
		elif opt in ("-d", "--debug"):
			start(int(arg))

	if len(sys.argv) < 3:
		print('error missing argument!')
		sys.exit(1)

if __name__ == '__main__':
	main(sys.argv[1:])
