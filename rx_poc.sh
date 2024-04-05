#! /bin/bash
#
# set $city
city=casablanca
#
# set time zone according to $city
TZ='Morocco/Casablanca'
#
# store city's date informations in shell variables
year=$(TZ=$(echo $TZ) date -u +%Y)
month=$(TZ=$(echo $TZ) date -u +%b)
day=$(TZ=$(echo $TZ) date -u +%d)
hour=$(TZ=$(echo $TZ) date -u +%H)
#
# gather raw data and store it timestamped in a txt file
echo -e "************************$(date)************************\n$(curl wttr.in/$city)" > raw_data_$(date +%Y%m%d).txt
#
# parse data to get temperatures out
#
  # observed_temperature: current temperature in $city
  obs_tmp=$(cat raw_data.txt | grep °C | cut -d "C" -f1 | head -1 | xargs | rev |  cut -d " " -f2 | rev)
  #
  # forecast_temperature: temperature forecasted for $city at 12:00 AM
  fc_temp=$(cat raw_data.txt | grep °C -n | head -n 3 | tail -n 1 | cut -d ":" -f2 | cut -d C -f2 | xargs | rev | cut -d " " -f2 | rev)
  #
# log temperature data in rx_poc.log
echo -e "$(echo $year)\t$(echo $month)\t$(echo $day)\t$(echo $hour)\t$obs_tmp\t$fc_temp" >> rx_poc.log
