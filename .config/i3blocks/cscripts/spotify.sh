#!/bin/bash

# Fetch currently playing song information
output=$(playerctl -p spotify metadata --format '{{ artist }} - {{ title }}')

# Check if there's a song playing
if [[ -z "$output" ]]; then
  echo "No song playing"
else
  echo "$output"
fi
