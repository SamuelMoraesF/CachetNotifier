#!/usr/bin/env python

import sys
import irc.client
import irc.logging

# If SSL is enabled, import the module
if sys.argv[6] == "true":
	import ssl

# Commands to run when the bot is connected to the server
def on_connect(connection, event):
	
	# For all receivers
	for receiver in target:
		
		# Verify if is channel
		if irc.client.is_channel(receiver):
			
			# Join channel and send message
			connection.join(receiver)
			for message in messages:
				connection.privmsg(receiver, message)
			
		# Else, is an nick
		else:
			
			# Send the message
			for message in messages:
				connection.privmsg(receiver, message)
	
	# Quit of the server
	connection.quit("Cachet Notify")
	
# Exit application when disconnect
def on_disconnect(connection, event):
	raise SystemExit()

# Define receivers var as global
global target

# Split all receivers by comma
target = sys.argv[4].split(',')

# Defining messages separated by comma
messages = sys.argv[5].split(',')

# If SSL is enabled
if sys.argv[6] == "true":
	
	# Set SSL Factory with SSL
	ssl_factory = irc.connection.Factory(wrapper=ssl.wrap_socket)
	
	# Requirement of the IRC module
	reactor = irc.client.Reactor()
	
	# Connect with SSL
	c = reactor.server().connect(sys.argv[1], int(sys.argv[2]), sys.argv[3], connect_factory=ssl_factory)
	
# Else, SSL is disabled
else:

	# Requirement of the IRC module
	reactor = irc.client.Reactor()

	# Connect to the server
	c = reactor.server().connect(sys.argv[1], int(sys.argv[2]), sys.argv[3])

# Define handlers
c.add_global_handler("welcome", on_connect)
c.add_global_handler("disconnect", on_disconnect)

# Define as forever process
reactor.process_forever()
