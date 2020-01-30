# PIiCamBot

This is a very basic Telegram bot firstly though to receive pictures from a 3D printer, but is editable to do anything. It is a remix from this [Telegram bot tutorial](https://www.hackster.io/Salmanfarisvp/telegram-bot-with-raspberry-pi-f373da) and the [PiCamera tutorial](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera) from Raspberry.

So for the setup stage, you can follow the [Telegram bot tutorial](https://www.hackster.io/Salmanfarisvp/telegram-bot-with-raspberry-pi-f373da) up to the **step 3.4**. Now we are going to download [`bot.py`](/bot.py) from GitHub. Insert this the SSH terminal (it copies this repo):

```
git clone https://github.com/eneriz-daniel/RPiCamBot.git
```

Then it's necessary to insert the bot token (the large alphanumeric code the Bot Father gave you on the step 1.6 of the Telegram bot tutorial) instead of the 'BotToken' string on the line 26 of [`bot.py`](/bot.py). You can access to the code using the terminal text editor nano:

```
sudo nano bot.py
```


So you must to replace this:
```
bot = telepot.Bot('BotToken')
```
into this:
```
bot = telepot.Bot('<your-alphanumeric-token>')
```

For exit you just used the `Ctrl-X` command, confirm with `Ctrl-Y` and the tap then `Entr` to save the changes.

Once this have been done, you have to launch the code inserting this in the Raspberry's SSH terminal:
```
python bot.py
```
Now, it is necessary to know the chat ID the bot assigns to you. For this, you have to add the bot to telegram and send a message to it. When this message is received, the bot will print the chat ID on the SSH terminal. Stop the run of `bot.py` using `Ctrl-C`. You have to copy it and insert it (as an `int`) in the `accepted_users` list of the line 8 of [`bot.py`](/bot.py). For this, use the nano editor:

```
sudo nano bot.py
```

You can have various accepted users adding more elements to this list like this:
```
accepted_users = [<chat-id-user1>,<chat-id-user2>]
```

To make the bot automatically start in the Raspberry's boot you can is possible to add a `crontab` task. For this type in the terminal the following command:
```
sudo crontab -e
```

Probably this would be the first time you use crontab, so it will show something like:
```
no crontab for root - using an empty one

Select an editor.  To change later, run 'select-editor'.
  1. /bin/nano        <---- easiest
  2. /usr/bin/vim.basic
  3. /usr/bin/vim.tiny

Choose 1-3 [1]:
```

Choose the first one, nano, typing `1`+`Entr`.

Add at the end of the file this:
```
@reboot python bot.py
```
Exit the crontab's file and reboot the RPi using:
```
sudo reboot
```
When the RPi will be rebooted, you will be able to talk to the bot and it will answer you. The default feature is to send a picture using he PiCamera, but you can add whatever you want using your desired command.
