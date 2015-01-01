# Cachet Notification System
### Supports Pushover, Twitter, IRC, and XMPP!

# Install

#### Requirements

* Python 2.7
* pip

#### Instalation

First, you need to clone this repo:

```git clone https://github.com/SamuelMoraesF/CachetNotifier.git```

Now, change to the folder and install the requirements:

```cd CachetNotifier```
```pip install -r requirements.txt --allow-all-external```

Copy the config file example and start editing:

```cp bot.cfg.example bot.cfg```
```nano bot.cfg```

# Basic Configuration

* Change the ```url``` to the RSS URL of your Cachet Instalation
* Change ```interval``` to the interval of checks in seconds(if you have an good connection, it can be ```5```)

Now, you need to configure the protocols to receive notifications

#### XMPP

You can create your own XMPP server or use an [Public Server](http://xmpp.org/xmpp-software/servers/). You need to create an User for the bot(and for you if you not have one) and change the bot profile(optional, you can do it with an [XMPP client](http://xmpp.org/xmpp-software/clients/), change the bot nick/photo/info and add he as your friend)

Now, change the ```xmpp``` option on the config file to ```true``` and modify the following settings:

- ```to```:  The JID of the receivers separated by comma
- ```user```: The JID of the bot
- ```password```: Password of the bot JID

![Notification on XMPP](http://i.imgur.com/ewg44pY.png)

#### Pushover

![Notification on Pushover](http://i.imgur.com/InBC9Bx.png)

#### Twitter

![Notification on Twitter](http://i.imgur.com/XHNhQT6.png)

#### IRC

![Notification on IRC](http://i.imgur.com/MmwH4kN.png)

