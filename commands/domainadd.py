import sys
import subprocess


cmd_list = sys.argv[1::]

if cmd_list[0] == "--help":
  print("To add a new domain please run command with arguments --username=username --domain=fulldomain --dns=local --docroot")
  exit
  
username=""
domain=""
dns=""
docroot=""

for i in cmd_list[1::]:
  c = i.split("=")
  match c[0]:
    case "--username":
      c[1] = c[1].strip()
      username=c[1]
    case "--domain":
      domain = c[1]
    case "--dns":
      dns=c[1]
    case "--docroot":
      docroot = c[1]

