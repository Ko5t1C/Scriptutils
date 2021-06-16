#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket, threading, time, traceback, re
#recup les locales fr pour formater la date
import locale
#système de logs
#import Colorer
#import coloredlogs
import logging

from queue import Queue

from flask import Flask




class Webpanel:
	_send_queue = Queue()
	_recv_queue = Queue()
	_connected = False
	_running = False

	def __init__( self, port):

		self._port = port

	def run( self ):
		self._running = True

		app = Flask(__name__)


		@app.route('/')
		def hello():
		    return 'Hello, World!'
