#!/usr/bin/env bash
 sudo apt-get update
 sudo apt-get install build-essential chrpath libssl-dev libxft-dev
 sudo apt-get install libfreetype6 libfreetype6-dev
 sudo apt-get install libfontconfig1 libfontconfig1-dev
 sudo apt autoremove
 sudo apt-get install libfreetype6 libfreetype6-dev
 sudo apt-get install libfontconfig1 libfontconfig1-dev
 cd ~
export PHANTOM_JS="phantomjs-1.9.8-linux-x86_64"
wget https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2
sudo tar xvjf $PHANTOM_JS.tar.bz2
sudo mv $PHANTOM_JS /usr/local/share
sudo ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin
FIREFOX_VERSION="47.0.1"
SELENIUM_VERSION="2.53/selenium-server-standalone-2.53.1.jar"
sudo apt-get -y install xvfb
chown root:root selenium-server-standalone.jar
chmod +x selenium-server-standalone.jar
CHROME_DRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`
SELENIUM_STANDALONE_VERSION=3.4.0
SELENIUM_SUBDIR=$(echo "$SELENIUM_STANDALONE_VERSION" | cut -d"." -f-2)
rm ~/google-chrome-stable_current_amd64.deb
rm ~/selenium-server-standalone-*.jar
rm ~/chromedriver_linux64.zip
sudo rm /usr/local/bin/chromedriver
sudo rm /usr/local/bin/selenium-server-standalone.jar
# Install dependencies.
sudo apt-get update
sudo apt-get install -y unzip openjdk-8-jre-headless xvfb libxi6 libgconf-2-4
apt install python-pip
pip install selenium
pip install --upgrade pip