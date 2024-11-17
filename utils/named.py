#main script to install or update named
import os
import subprocess


def install_named():
  subprocess.run(["dnf", "install", "bind bind-utils", "--yes"], check=True)
  subprocess.run(["setsebool -P named_write_master_zones on"], check=True)
  subprocess.run(["setsebool -P named_enable_zone_write on"], check=True)
  subprocess.run(["semanage fcontext -a -t named_zone_t \"/var/named(/.*)?\""], check=True)
  subprocess.run(["semanage fcontext -a -t named_conf_t \"/etc/named.conf\""], check=True)
  subprocess.run(["restorecon -Rv \"/var/named\" \"/etc/named.conf\" \"/var/named/data\""], check=True)
  subprocess.run(["systemctl start named"], check=True)
  subprocess.run(["systemctl enable named"], check=True)
  