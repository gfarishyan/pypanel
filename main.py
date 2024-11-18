import subprocess
import os
from utils.named import install_named
from utils.php import install_php
from utils.db import install_databases
from utils.nodejs import install_nodejs
from utils.mailserver import install_mailserver
from utils.httpd import install_httpd
from utils.ftpd import install_ftpd


panelBaseDir="/var/pypanel"


def prompt(question):
    answer = input(question)
    return answer
    
"""
def check_system_apache():
    is_installed=False
    try:
        result = subprocess.run(['apache2', '-v'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        is_installed=True
    except subprocess.CalledProcessError:
        echo "Could not find apache2"
    except FileNotFoundError:
        echo "Could not find apache2"

    return is_installed
"""
  
def create_panel_dirs():
    global panelBaseDir
    
    #check does exists diretory or not ?
    
    if not os.path.exists(panelBaseDir):
      print ("Pypanel base directoy {} couldn't found.".format(panelBaseDir))
      os.makedirs(panelBaseDir)
      print ("Created Pypanel base directoy at {}.".format(panelBaseDir))
    else:
      print ("Found Pypanel base directoy at {}.".format(panelBaseDir))
    
create_panel_dirs()
install_named()
#prompt_bind()
install_databases()
#install_php()
#install_nodejs()
#install_httpd()
#install_ftpd()
        