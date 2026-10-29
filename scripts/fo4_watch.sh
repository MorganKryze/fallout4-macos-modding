#!/bin/zsh
# Record one play session: the Metal HUD frame log, CPU of the game and of
# wineserver, thermal warnings, and a screenshot every few minutes.
#
#   fo4_watch.sh LABEL [SHOT_MINUTES]     (start it before launching the game)
#
# Writes to ~/FO4-Bench/<date>-<time>-LABEL/. Stops by itself a minute after
# Fallout4.exe exits, or on Ctrl-C. Summarise with fo4_bench.py wine.log.
# Not Proton empties notproton-wine.log at each launch; tail -F follows it.
label=${1:?usage: fo4_watch.sh LABEL [SHOT_MINUTES]}
shot=$(( ${2:-5} * 60 ))
out=~/FO4-Bench/$(date +%F-%H%M)-$label
log=~/Library/Application\ Support/notproton/launchers/377160/notproton-wine.log
mkdir -p $out/shots
tail -n 0 -F $log > $out/wine.log 2>/dev/null &
tailpid=$!
trap 'kill $tailpid; exit' INT TERM
echo "time,game_cpu,game_rss_mb,wineserver_cpu,load1" > $out/stats.csv
seen=0 gone=0 t=0
while (( gone < 6 )); do
  pid=$(ps -A -o pid=,comm= | awk '/\\Fallout4\.exe$/{print $1; exit}')
  if [[ -n $pid ]]; then
    seen=1 gone=0
    read gcpu grss <<< "$(ps -o %cpu=,rss= -p $pid)"
    wcpu=$(ps -o %cpu= -p "$(pgrep -x wineserver | head -1)" 2>/dev/null)
    echo "$(date +%T),$gcpu,$(( grss / 1024 )),${wcpu// /},$(sysctl -n vm.loadavg | cut -d' ' -f2)" >> $out/stats.csv
    (( t % shot == 0 )) && screencapture -x -t jpg $out/shots/$(date +%H%M%S).jpg
    pmset -g therm | grep -v '^Note' | sed "s/^/$(date +%T) /" >> $out/therm.txt
  elif (( seen )); then
    (( gone++ ))
  fi
  sleep 10; (( t += 10 ))
done
kill $tailpid
echo "$out"
