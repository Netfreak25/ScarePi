#!/bin/bash
echo "starting scarepi"
echo "####################################################"
echo

cooldown="5"
file_cooldown="1"

pigs r 18

echo "initial start sleep 30s"
sleep 30

while true
do
  echo "Cooldown: "$cooldown"s"
  echo "Reading Variables"
  echo
  playmode=`cat /opt/scarepi/Options/playmode`
  selected_playlist="/opt/scarepi/Playlists/"`cat /opt/scarepi/Options/playlist`"/"
  soundmode=`cat /opt/scarepi/Options/sound`
  echo "Playmode: "$playmode
  echo "Selected Playlist: "$selected_playlist
  echo "Sound Mode: "$soundmode

  omxcommand="omxplayer"
  if [ $soundmode == "HDMI" ]
  then
    omxcommand="omxplayer -o hdmi "
  elif [ $soundmode == "Bluetooth" ]
  then
    omxcommand="omxplayer -o alsa "
  elif [ $soundmode == "Jack" ]
  then
    omxcommand="omxplayer -o local "
  fi

  echo "OMX Command: "$omxcommand
  echo "Files in Playlist:"
  for i in `ls $selected_playlist`
  do
    echo $i
  done

  echo
  echo
  if [ $playmode == "Loop" ]
  then
    echo "Loop through Playlist and repeat"
    for i in `ls $selected_playlist`
    do
      echo $omxcommand$selected_playlist$i
      $omxcommand$selected_playlist$i
      sleep $file_cooldown
    done
    sleep $cooldown
  elif [ $playmode == "API-Trigger" ]
  then
    echo "Waiting for API-Trigger"
    if test -f "/opt/scarepi/Trigger/API-Trigger"; then
        echo "API-Trigger detected"
        for i in `ls $selected_playlist`
        do
          echo $omxcommand$selected_playlist$i
          $omxcommand$selected_playlist$i
          sleep $file_cooldown
        done
        rm "/opt/scarepi/Trigger/API-Trigger"
    else
        echo "No API Trigger - Skipping"
    fi
    sleep $cooldown
  elif [ $playmode == "GPIO-Trigger" ]
  then
    echo "Waiting for GPIO-Trigger"
    if [ `pigs r 18` == "1"]; then
        echo "GPIO-Trigger detected"
        for i in `ls $selected_playlist`
        do
          echo $omxcommand$selected_playlist$i
          $omxcommand$selected_playlist$i
          sleep $file_cooldown
        done
    else
        echo "No GPIO Trigger - Skipping"
    fi
  fi
  if [ `ls /opt/scarepi/Playlists/ | wc -l` -eq 1 ]
  then
    if [ `ls /opt/scarepi/Playlists/Default/ | wc -l` -eq 0 ]
      then
        echo "Only default playlist without files"
        sleep 30
    fi
  fi
  clear
done
