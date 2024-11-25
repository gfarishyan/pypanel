#check des user exists ?
import sys
import subprocess


def rand_password(length):
  pwd=""
  char_list = string.ascii_letters + string.digits + string.punctuation
  
  for i in range(length):
    pwd +=  random.choice(char_list)
  
  return pwd
  

cmd_list = sys.argv[1::]

if cmd_list[0] == "--help":
  print("To add user run")
  print("pypanel add username --home=/home/somedir to override home directory --quota=500MB --password=your_password")
  exit

username=cmd_list[0]
home=f"/home/{username}"
quota="unlmited"
pwd=""

for i in cmd_list[1::]:
  c = i.split("=")
  match c[0]:
    case "--home":
      c[1] = c[1].strip()
      home=c[1]
    case "--quota":
      quota = c[1]
    case "--password":
      pwd=c[1]

user_add_cmd=["useradd", username, "-m", "-d", home]

subprocess.run(user_add_cmd, check=True)

if quota != "unlmited":
  subprocess.run(["setquota", "-u", username, quota, quota, 0, 0, home], check=True)
  
"""
  setup password
"""



if pwd == "":
  pwd=rand_password(8)
  
subprocess.run(["usermod", "--password", pwd, username])