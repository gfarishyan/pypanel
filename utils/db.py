import os
import subprocess
import re

def install_databases():
  
  database_list = {
    "mysql": ["8.0"],
    "mariadb": ["10.1", "10.2", "10.3", "10.4", "10.5", "10.6", "10.7", "10.8", "10.9", "10.10", "10.11", "11.0", "11.1", "11.2", "11.3", "11.4", "11.5", "11.6", "11.7"],
    "postgresql": ["13", "14", "15", "16", "17"],
    "mongodb": ["5", "6", "7", "8"]
  }
  
  answer = input("Please specify which databases you would like to install [mysql, mariadb, postgresql, no] ?")
  answer = answer.replace(",", " ").strip().lower()
  answer = re.sub(r"\s+", " ", answer)
  if "no" in answer:
    return
  
  selected_dbs = answer.split(' ')
  
  if "mysql" in selected_dbs and "mariadb" in selected_dbs:
    print("mysql and mariadb can not be installed in same time")
    return install_databases()
    
  selected_dbs_with_versions = {}
  
  for db in selected_dbs:
    v = input("Please specify which version to install for {0}. Possible versions: {1}", db, database_list[db].join(" "))
    v = re.sub(r"\s+", " ", v)
    v = v.strip().lower()
    
    if v not in database_list[v]:
      print "Not valid version selected."
    else
      selected_dbs_with_versions[db] = v
  
def install_mysql(version):
  return
  
def install_mongodb(version):
  return
  
def install_posgresql(version):
  return
  
def install_mariadb(version):
  return

  