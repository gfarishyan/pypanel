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
  
  answer = input("Please specify which databases you would like to install [mysql, mariadb, postgresql,mongodb no] ?")
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
    v = input("Please specify which version to install for {0}. Possible versions: {1} ? ".format(db, ' '.join(database_list[db])))
    v = re.sub(r"\s+", " ", v)
    v = v.strip().lower()
    
    if v not in database_list[db]:
      print("Not valid version selected.")
    else:
      selected_dbs_with_versions[db] = v
  print(selected_dbs_with_versions)
  for db, version in selected_dbs_with_versions:
    caller="install_{0}".format(db)
    print(caller)
    #caller(version)
  
  
  
def install_mysql(version):
  print("Called install mysql with {0} version.".format(version))
  return
  
def install_mongodb(version):
  print("Called install mongodb with {0} version.".format(version))
  return
  
def install_posgresql(version):
  print("Called install posgresql with {0} version.".format(version))
  return
  
def install_mariadb(version):
  print("Called install mariadb with {0} version.".format(version))
  return

  