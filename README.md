This tool is used for manage remote server via telegram.
First you need to get api credentials from here: https://my.telegram.org
And create new bot here: https://t.me/BotFather
Installation

Install package installer for python

apt-get install python3-pip -y

Download libraries for our script

pip3 install telethon

Download python script and make the file executable

wget https://raw.githubusercontent.com/bobu4/manage_bot/main/manage_bot.py ; chmod +x manage_bot.py

Edit script with your credentials

nano manage_bot.py

![image](https://user-images.githubusercontent.com/48527047/214265079-37d765c8-ee43-43d9-88c0-c68206ec160e.png)

Save our script by press Ctrl+X then y

Run new tmux session and run our script in new window

tmux
python3 manage_bot.py

Detach from our secondary window by pressing Ctrl+b then D

Start our bot by click or type /start

![image](https://user-images.githubusercontent.com/48527047/214266500-5e56819b-ba4e-4ad5-9d8c-0cebf9fe1110.png)

For sending command to the remote server press button Send command and then type command. For example, withdraw rewards from vote account in solana testnet

![image](https://user-images.githubusercontent.com/48527047/214266893-fb10ee41-50ae-4e42-b475-1f59b72f247f.png)

We got output to our bot. That's all.
