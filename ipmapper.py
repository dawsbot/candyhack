"""
  Author: Dawson Botsford
  Date: 7/19/2014
  Purpose: Take inputted URL and return lat/long
  Creds: github help from @mossberg
"""
import sys
import socket
import os
import subprocess
import json

def main():
  #User inputted one URL 
  if len(sys.argv) != 2:
       print "ERROR: please input 1 URL"
       return
 
  url = sys.argv[1]
  ip = socket.gethostbyname(url)
  cmd = 'curl -s ipinfo.io/' + ip + '/loc'
  os.system(cmd) 

main()
