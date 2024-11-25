import sys
import subprocess
import re
from string import Template

cmd_list = sys.argv[1::]

username=""
domain=""
zonefile_path="/var/named/zones"



def create_zone(domain):
  zone = Template("""zone "$domain" {
    type master;
    file "$domain.db";
    notify yes;
    };
    """)

  return zone.substitute(domain=domain)
  

def read_zone_file(filename):
  zone_content = []
  f = open(filename, 'rt')
  for line in file:
    s = line.strip()
    s = re.sub(r'\s+', ' ', s)
    zone_content.append(line.split(''))
  close(f)
  
  return zone_content
  
def write_zone_file(filename, contents)
  f = fopen(filename, 'wrt')
  f.truncate(0)
  for i in contents:
    f.write(i.join('') + "\n")

  close(f)  
  
  
def create_zone_file(domain):
  zone = ""
  

def add_Record(domain, rtype, name, value, ttl):
  return
  
  
def delete_Record(domain, record):
  return
  
def modify_Record(domain, record):
  return
  
