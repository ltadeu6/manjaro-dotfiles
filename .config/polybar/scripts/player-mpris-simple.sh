#!/bin/sh

player_status=$(playerctl status 2> /dev/null)
player_artist=$(playerctl metadata artist 2> /dev/null)
player_title=$(playerctl metadata title 2> /dev/null)
player_shuffle=$(playerctl shuffle 2> /dev/null)

case "$player_shuffle" in
  "On") shuffle_icon="咽";;
  "Off") shuffle_icon="劣";;
esac

case "$player_status" in 
  "Playing") play_icon="ﱘ";;
  "Paused") play_icon="";;
  "Stopped") play_icon="栗";;
esac

if [[  ($player_artist != "" && $player_title != "")  ]]; then
    echo "$play_icon $player_artist - $player_title $shuffle_icon"
else echo
fi
