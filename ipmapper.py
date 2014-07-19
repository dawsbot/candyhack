"""
  Take inputted URL and return lat/long
"""
import sys
import socket

def main():
  #User inputted one URL 
  if len(sys.argv) != 2:
       print "ERROR: please input 1 URL"
       return
 
  url = sys.argv[1]
  print socket.gethostbyname(url)
  
  
main()
