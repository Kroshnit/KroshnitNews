# KroshnitNews

UPDATE 21 February 2023

In recognition of Russia's continued assault on Ukraine nearly one year on, I have updated the next iteration of KroshnitNews as a Pyhton script that can be run in the background on your desktop.

Fight back against Putin's war propaganda in Russia by sharing real stories about what's been happening in Ukraine with Russian citizens. As before, this project is made possible thanks to PravdaMail www.pravdamail.com, which provides the curated messages and a large database of Russian civilian email addresses.

The script as written will work in Python 3.10 and 3.11 vis Windows command prompt or Mac Terminal. To run in version 3.9 only a minor change is necessary and this is given in the comments. I have not tested in Linux, but assume it's the same; tried several distributions in iOS but these are very limited and was unsuccessful. Planning to develop a full-on iOS/iPadOS app next, and would be interested to see if anyone can adapt for Android devices.

Prior to running, you will need to have Beautiful Soup (bs4) and the Yagmail package installed for Python:

https://www.crummy.com/software/BeautifulSoup/

https://github.com/kootenpv/yagmail

You will also need to provide a Gmail account (creating a new, dedicated account is recommended) and configure it with an app-specific password for this service. To do this go to https://myaccount.google.com/security, scroll to "Signing in with Google" and click on "App Passwords."

When you run the script, you'll be prompted to enter how many messages you want to send (this can be any number, but don't overdo it - more than a few hundred at a time may run the risk of your email being blacklisted by Russian domains). Hit enter, sit back, and watch the messages fly. Take that, Channel One...

Slava Ukraini!



KroshnitNews Automator Script for MacOS (archived)

Setup in 2 steps:

1) Ensure default mail reader is set to Apple Mail.

2) Change placeholder in the third script (line 6, "NameOfAccount") to the name of your preferred outgoing account (leave in quotes), or remove line if not needed.

Unfortunately this doesn't work as a background process, so launch only when you can walk away from your Mac for a while. Have the bot do your war correspondence for you while you sleep, perhaps.

Default loop duration is set to 30 minutes but feel free to change it to your preference. The pauses are set to accomodate my specific setup (2020 intel MacBook Air running Big Sur) but you may have better performance with other adjustments. Current settings result in one new message every 10 seconds.

Comments or suggestions: kroshnit@yahoo.com

Summary:
Automator app for macOS that generates and sends a new PravdaMail message every 10 seconds (www.pravdamail.com). Supporting the anti-war effort inside Russia.

About PravdaMail:

"Email a random Russian about the war in Ukraine

Many in Russia continue to support dictator Putin because they only know the “facts” from state propaganda.

Use this site to let them know what's really going on . We've collected more than a million Russian email addresses just for that."

Messages link to Telegram channel https://t.me/meduzalive posting accurate information on the war in Ukraine to counter Kremlin propaganda.
