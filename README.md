# i3blocks-sonos

## About
i3blocks-sonos is an i3blocks blocklet script to:
* Output the status (playing/stopped) of your Sonos
* Current song playing if any on your Sonos
* Toggle playing/stopped on your Sonos
* Skip to next song on your Sonos


## Dependencies
fonts-font-awesome, soco, python3

## Look
Paused / Playing:
![](https://raw.githubusercontent.com/Lilleengen/i3blocks-sonos/master/images/paused.png) / ![](https://raw.githubusercontent.com/Lilleengen/i3blocks-sonos/master/images/playing.png)

## Getting started
Install [font-awesome](https://fortawesome.github.io/Font-Awesome/)

Install soco using `pip install soco`

Copy the blocklet configuration in the given `i3blocks.conf` (or below) into your i3blocks configuration file
```INI
[sonos]
command=$SCRIPT_DIR/i3blocks-sonos.py $BLOCK_BUTTON
markup=pango
interval=5
```

## Usage
Left-click it to toggle playing

Right-click to skip to next song
