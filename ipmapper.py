"""
  Take inputted URL and return lat/long
"""
import sys
import socket
import os

def main():
  #User inputted one URL 
  if len(sys.argv) != 2:
       print "ERROR: please input 1 URL"
       return
 
  url = sys.argv[1]
  ip = socket.gethostbyname(url)
  print ip 
  cmd = 'curl ipinfo.io/' + ip
  os.system(cmd)
  print cmd 

main()
