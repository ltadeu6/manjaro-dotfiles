#!/usr/bin/env sh

## Add this to your wm startup file.

# Terminate already running bar instances
killall -q polybar &&

# Wait until the processes have been shut down
# while pgrep -u $UID -x polybar >/dev/null; do sleep 2; done
while pgrep -u $UID -x polybar >/dev/null; do sleep 2; done

# polybar dummy -c ~/.config/polybar/qtile.ini &

polybar main --reload -c ~/.config/polybar/qtile.ini &

# Launch bar1 and bar2
# polybar full -c ~/.config/polybar/config.ini &
