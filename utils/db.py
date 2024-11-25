import os
import subprocess
import re
#import requests
import pathlib
import platform
import json

global os_version, installer_command, os_name
os_version=9
installer_command="dnf"
os_name="redhat"


def read_repo_file(fname):
  dirname = pathlib.Path(__file__).parent.resolve()
  remote_rpm = "{0}/../repo-list/{1}".format(dirname,fname)
  f = open(remote_rpm)
  data = json.load(f)
  return data


def install_mysql(version):
  maysql_repo=read_repo_file("mysql.repo")
  global os_version, installer_command,os_name
  vv =  int(float(version))
  repo_file_name = maysql_repo[installer_command][os_name]["{}".format(vv)]
  remote_filename = "https://dev.mysql.com/get/{0}".format(repo_file_name)
  subprocess.run([installer_command, "install", remote_filename],  text = True, check=False)
  subprocess.run([installer_command, "install", "mysql-server"],  text = True, check=False)
  subprocess.run(["systemctl", "enable", "mysqld"],  text = True, check=False)
  subprocess.run(["systemctl", "start", "mysqld"],  text = True, check=False)
  subprocess.run(["mysql_secure_installation"],  text = True, check=False)
  return
  
def install_mongodb(version):
  print("Called install mongodb with {0} version.".format(version))
  return
  
def install_postgresql(version):
  postgresql_repo=read_repo_file("postgresql.repo")
  print("Called install posgresql with {0} version.".format(version))
  return
  
def install_mariadb(version):
  mariadb_repo=read_repo_file("mariadb.repo")
  """  
   url="https://r.mariadb.com/downloads/mariadb_repo_setup"
   response = requests.get(url, stream=True)
  if response.status_code == 200:
    with open("mariadb_repo_setup.sh", "wb") as script_file:
      script_file.write(response.content)
  else:
    exit 1

  subprocess.run(["bash", "-s", "--", "--mariadb-server-version={0}".format(version)], check=False, text=True)
  """
  return

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

  for db in selected_dbs_with_versions:
    caller="install_{0}".format(db)
    v = selected_dbs_with_versions[db]
    globals()[caller](v)
  
