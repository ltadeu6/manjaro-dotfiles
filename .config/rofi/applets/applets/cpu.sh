#!/usr/bin/env bash

style="$($HOME/.config/rofi/applets/applets/style.sh)"

dir="$HOME/.config/rofi/applets/applets/configs/$style"
rofi_command="rofi -theme $dir/cpu.rasi"

## Get data
CPU="$(~/.config/rofi/bin/usedcpu)"
RAM="$(free -ht | grep "Total" | awk '{print $3/($2) * 100}' | xargs printf "%.*f\n" "$p")%"
SSD="$(df -hl | awk '/^\/dev\/sda2/ {print $5}')"
uptime=$(uptime -p | sed -e 's/up //g' -e 's/hours/horas/g' -e 's/minutes/minutos/g')

active=""
urgent=""

CPU_ICON=""
SSD_ICON=""
RAM_ICON=""

options="$CPU_ICON $CPU\n$RAM_ICON $RAM\n$SSD_ICON $SSD"

## Main
chosen="$(echo -e "$options" | $rofi_command -p "$uptime" -dmenu $active $urgent -selected-row 0)"
case $chosen in
    *%)
      kitty -o background_opacity=1 -o "font_family=Fira Code" --name "floating" -e gotop
    ;;
esac

