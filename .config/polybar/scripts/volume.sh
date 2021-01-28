#!/bin/sh

player_volume=$(playerctl volume)

$(playerctl volume $($player_volume + 0.1))
