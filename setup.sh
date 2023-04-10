#!/bin/bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt-get update -y
sudo apt-get install ./google-chrome-stable_current_amd64.deb -y
sudo apt-get install -y unzip xvfb libxi6 libgconf-2-4
wget https://chromedriver.storage.googleapis.com/92.0.4515.43/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
export PATH=$PATH:/usr/lib/chromium-browser/
