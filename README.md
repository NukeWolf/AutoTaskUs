# AutoTaskUs

> Hello, thanks for visiting my project. This project was built because I really wanted to leave my desk when I was playing among us, and theres often not a lot of downtime while playing the game, as even if you're dead, you still have to do tasks. This project plays the game for me.

## General

This project runs off 2 main dependencies, Open CV2 to take input from the screen, and pyautogui to control your character. The code is broken down into 4 different modules that handle Computer Vision, Player Input, Task management/Actions, and navigating the map.


## Limitations

The code only currently works on one map, Skald and also only supports one resolution, 1920x1080p in fullscreen. The code is highly configurable however, as you can edit all of the pixel checks and mouse click locations in the .yaml file in ref. If you wanted to spenda bit of time creating your own custom config file, go for it, but I don't have enough time to support other resolutions currently or maps.

## Dependencies

- OpenCV2
- Pyautogui
- Yaml
- Pillow

## Setup

Download source code, install requirements.txt, and run the bot.py file.

## Demo 

[![AutoTaskUsDemo](http://img.youtube.com/vi/YLdDvTg6-W4/0.jpg)](https://youtu.be/YLdDvTg6-W4 "AutoTaskUs demo")