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

![Notification on XMPP](http://i.imgur.com/ewg44pY.png)

#### Pushover

![Notification on Pushover](http://i.imgur.com/InBC9Bx.png)

#### Twitter

![Notification on Twitter](http://i.imgur.com/XHNhQT6.png)

#### IRC

![Notification on IRC](http://i.imgur.com/MmwH4kN.png)

