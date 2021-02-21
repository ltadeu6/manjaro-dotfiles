#!/bin/bash

TEXT=$(~/.config/polybar/scripts/openweathermap-fullfeatured.sh)
notify-send "$TEXT" -i weather

