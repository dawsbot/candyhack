"""
  Author: Dawson Botsford
  Date: 7/19/2014
  Purpose: Take inputted URL and return lat/long
  Creds: github help from @mossberg
    Haversine folmula: http://www.johndcook.com/python_longitude_latitude.html
"""
import sys
import socket
#import os
import subprocess
#import json

def main():
  #User inputted one URL 
  if len(sys.argv) != 2:
       print "ERROR: please input 1 URL"
       return
 
  url = sys.argv[1]
  ip = socket.gethostbyname(url)
  cmd = 'curl -s ipinfo.io/' + ip + '/loc'

  proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
  (out, err) = proc.communicate()
  print "lat/long of host server:", out

main()
