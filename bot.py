#!/usr/bin/python
import hashlib
import feedparser
import logging
import sys
import os
import ConfigParser
import time
import html2text
import irc
from apscheduler.schedulers.blocking import BlockingScheduler

# Reading Config Files
global config
config = ConfigParser.ConfigParser()
config.read('bot.cfg')

# If XMPP is enabled
if config.getboolean('xmpp', 'xmpp'):
	import xmpp
	
# If Pushover is enabled
if config.getboolean('pushover', 'pushover'):
	import requests

# If Twitter is enabled
if config.getboolean('twitter', 'twitter'):
	from twython import Twython

# Starting Block Scheduler
sched = BlockingScheduler()

# Logger
root = logging.getLogger()
root.setLevel(config.get('logs', 'level'))

# To stdout or file
if config.getboolean('logs', 'stdout'):
	log = logging.StreamHandler(sys.stdout)
else:
	log = logging.FileHandler(config.get('logs', 'filename'))
	
# Log Level
log.setLevel(config.get('logs', 'level'))

# Log format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log.setFormatter(formatter)

# Add handler
root.addHandler(log)
logging.getLogger('apscheduler').setLevel(logging.DEBUG)

# Create the cache file if this not exist
if not os.path.exists(config.get('cachet', 'cache')):
	open(config.get('cachet', 'cache'), 'w').close()

try:
	
	# Function when feed has new item
	def newitem(title, itemhash, content, status, updated):
		
		# Content HTML2Text
		content=html2text.html2text(content).strip('\n')
		
		# Log
		root.info('New item: %s - %s' %(title, itemhash))
		
		# If XMPP is enabled
		if config.getboolean('xmpp', 'xmpp'):

			# Separate reveivers into a list
			xmppreceivers = config.get('xmpp', 'to').split(",")
			
			# Format of the message
			text="New Issue: %s (%s)"%(title,status)
			desc="%s - %s"%(content, updated)

			# Get JID from config file
			jid = config.get('xmpp', 'user')

			# Connect
			jid=xmpp.protocol.JID(jid)
			cl=xmpp.Client(jid.getDomain(),debug=[])
			con=cl.connect()
			
			# Error in connection
			if not con:
				root.error('Could not connect to the XMPP Server')
				sys.exit(1)
			
			# Connected sucessfully
			root.info('Conected to XMPP with %s'%con)
			
			# Auth
			auth=cl.auth(jid.getNode(),config.get('xmpp', 'password'),resource=jid.getResource())
			
			# Cannot Auth
			if not auth:
				root.error('Could not authenticate on the XMPP Server')
				sys.exit(1)
				
			# Authenticated
			root.info('Authenticated on the XMPP server using %s'%auth)

			# Send message to receivers
			for receiver in xmppreceivers:
				id=cl.send(xmpp.protocol.Message(receiver,text))
				root.info('First message sent to %s with id %s'%(receiver, id))
				
				id=cl.send(xmpp.protocol.Message(receiver,desc))
				root.info('Second message sent to %s with id %s'%(receiver, id))

			# Some older servers will not send the message if you disconnect immediately after sending
			time.sleep(1)

			cl.disconnect()

		# If Pushover is enabled
		if config.getboolean('pushover', 'pushover'):
			
			# Title and message to send
			title="New Issue: %s (%s)"%(title,status)
			message="%s - %s"%(content, updated)
			
			# POST args
			args = {'token': config.get('pushover', 'token'), 'user': config.get('pushover', 'user'), 'title': title, 'message': message, 'priority': config.getint('pushover', 'priority'), 'sound': config.get('pushover', 'sound')}
			
			# Run POST
			responsepush = requests.post("https://api.pushover.net/1/messages.json", params=args)
			
			# DEBUG output
			root.debug('Pushover Response: %s'%responsepush)
			
		# If Twitter is enabled
		if config.getboolean('twitter', 'twitter'):
			
			# Twitter keys
			twitter = Twython(config.get('twitter', 'app_key'), config.get('twitter', 'app_secret'), config.get('twitter', 'oauth_token'), config.get('twitter', 'oauth_token_secret'))
			
			# Tweet to publish
			text="New Issue: %s (%s), %s %s"%(title,status,content,config.get('twitter', 'after'))
			
			# Publish Tweet
			twitter.update_status(status=text)

	# Function to check new feed itens
	@sched.scheduled_job('interval', seconds=4, timezone=0)
	def check():
		feed = feedparser.parse(config.get('cachet', 'url'))
		for item in feed.entries:
			itemhash = hashlib.md5(item.title + item.updated_at).hexdigest()
			if not itemhash in open(config.get('cachet', 'cache')).read():
				newitem(item.title, itemhash, item.message, item.status, item.updated_at)
				with open(config.get('cachet', 'cache'), "ab") as myfile:
					myfile.write(itemhash + "\n")
	sched.start()

# Application Killed
except KeyboardInterrupt:

	root.info('Stopping Application')
	logging.shutdown()
