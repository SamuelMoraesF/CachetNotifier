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

* ```to```:  The JID of the receivers separated by comma
* ```user```: The JID of the bot
* ```password```: Password of the bot JID

![Notification on XMPP](http://i.imgur.com/ewg44pY.png)

#### Pushover

You can receive notifications on Android, iOS and Desktop with [Pushover](http://pushover.net).

First, create an account(if you not already do it) and install the [client](https://pushover.net/clients) on your devices.

To receive notifications, you need to [create an app](https://pushover.net/apps/build), the icon that you insert on this step will be used on the notifications.

Now, you only need to insert these infos in the config file and change the ```pushover``` option to ```true```:

* ```token```: The App Token
* ```user```: You User Key
* ```priority```: The priority of the notifications that you will receive([more info here](https://pushover.net/api#priority))
* ```sound```: The sound of the notifications([more info here](https://pushover.net/api#sounds))

![Notification on Pushover](http://i.imgur.com/InBC9Bx.png)

#### Twitter

To publish the notifications on Twitter you will need to [create an app](https://apps.twitter.com/app/new) and generate an Access Token.

Set the ```twitter``` option on the config file to ```true``` and insert these data on the config file:

* ```app_key```: App Consumer Key (API Key)
* ```app_secret```: App Consumer Secret (API Secret)
* ```oauth_token```: Twitter OAuth Access Token
* ```oauth_token_secret```: Twitter OAuth Access Token Secret
* ```after```: Text(or hashtag) to insert after the issue text(at the end of the tweet)

![Notification on Twitter](http://i.imgur.com/XHNhQT6.png)

#### IRC

To receive notifications on IRC you only need to modify the config file:

* ```server```: The IRC server address
* ```port```: The IRC server port
* ```nick```: Nick that the bot will use
* ```receivers```: Nicks and Channels to send the notification(separated by comma)
* ```ssl```: Enable or Disable SSL connection

![Notification on IRC](http://i.imgur.com/MmwH4kN.png)

# Running in background

You can keep this running with ```screen``` and ```crontab```.

Run ```crontab -e````and add this line:

```@reboot screen -d -S cachetbot -m /usr/bin/python2.7 /path/to/cachetnotify/bot.py```

You only need to change ```/path/to/cachetnotify/``` to the path where CachetNotify are.

I reccomend enable log to file if you will use this method.

To kill the bot, you need to run ```screen -r cachetbot``` and press CTRL+C.

# Running on Heroku

You need to create the file ```Procfile``` with the following content:

```worker: python bot.py```

Edit the configuration file(you will need to create manually the cache file and set the logging to STDOUT).

Remove the ```.gitignore``` file and deploy to heroku.

To read the logs you just need to run:

```heroku logs -t -p worker```

# More

* [CachetGnome3](https://github.com/SamuelMoraesF/CachetGnome3) - Receive Cachet notifications on Gnome3
