import os
import subprocess
import re

def install_php():
  answer = input("Would you like to install php ? (yes, no)")
  if answer == "no":
    return
    
  php_versions = ["55", "56", "70", "71", "72", "73", "74", "80", "81", "82", "83"]
  versions = input("Please specify which versions you would like to install ? {}".format(php_versions.join(' '))).strip().lower()
  versions = versions.replace(',', ' ')
  versions = re.sub(r"\s+", " ", versions)
  versions_arr = versions.split('')
  versions_missmatch = list(set(versions_arr) - set(php_versions))
  
  if (len(versions_missmatch) > 0):
    print "Unsupported php version selected {}".format(php_versions.join(' '))
    return install_php()
    
  php_version_extensions = {
    "55": {
      "default": [
        "bcmath", "bz2", "calendar", "core", "ctype", "curl", 
        "date", "dom", "ereg", "exif", "fileinfo", "filter", "ftp", 
        "gd", "gettext", "gmp", "hash", "iconv", "imap", "intl", "json",
        "libxml", "mbstring", "mhash", "mysqlnd", "nd_mysqli", "openssl",
        "pcntl", "pcre", "pdo", "pdo_mysql", "pdo_pgsql", "pdo_sqlite",
        "pgsql", "phar", "posix", "pspell", "readline", "redis", "reflection",
        "session", "shmop", "simplexml", "snmp", "soap", "sockets", "sourceguardian",
        "spl", "sqlite3", "standard", "tidy", "tokenizer", "xml", "xmlreader", "xmlrpc",
        "xmlwriter", "xsl", "zip", "zlib"
       ],
      "extdended": [],
    },
    "56": {
       "default": [
         "bcmath", "bz2", "calendar", "core", "ctype", "curl", 
         "date", "dom", "ereg", "exif", "fileinfo", "filter", "ftp", 
         "gd", "gettext", "gmp", "hash", "iconv", "imap", "intl", "json",
         "libxml", "mbstring", "mhash", "mysqlnd", "nd_mysqli", "openssl",
         "pcntl", "pcre", "pdo", "pdo_mysql", "pdo_pgsql", "pdo_sqlite",
         "pgsql", "phar", "posix", "pspell", "readline", "redis", "reflection",
         "session", "shmop", "simplexml", "snmp", "soap", "sockets", "sourceguardian",
         "spl", "sqlite3", "standard", "tidy", "tokenizer", "xml", "xmlreader", "xmlrpc",
         "xmlwriter", "xsl", "zip", "zlib"
       ],
      "extdended": [],
    },
    "70": {
       "default": [
         "bcmath", "bz2", "calendar", "core", "ctype", "curl", 
         "date", "dom", "ereg", "exif", "fileinfo", "filter", "ftp", 
         "gd", "gettext", "gmp", "hash", "iconv", "imap", "intl", "json",
         "libxml", "mbstring", "mhash", "mysqlnd", "nd_mysqli", "openssl",
         "pcntl", "pcre", "pdo", "pdo_mysql", "pdo_pgsql", "pdo_sqlite",
         "pgsql", "phar", "posix", "pspell", "readline", "redis", "reflection",
         "session", "shmop", "simplexml", "snmp", "soap", "sockets", "sourceguardian",
         "spl", "sqlite3", "standard", "tidy", "tokenizer", "xml", "xmlreader", "xmlrpc",
         "xmlwriter", "xsl", "zip", "zlib"
       ],
      "extdended": [],
    },
    "71": {
       "default": [
         "bcmath", "bz2", "calendar", "core", "ctype", "curl", 
         "date", "dom", "ereg", "exif", "fileinfo", "filter", "ftp", 
         "gd", "gettext", "gmp", "hash", "iconv", "imap", "intl", "json",
         "libxml", "mbstring", "mhash", "mysqlnd", "nd_mysqli", "openssl",
         "pcntl", "pcre", "pdo", "pdo_mysql", "pdo_pgsql", "pdo_sqlite",
         "pgsql", "phar", "posix", "pspell", "readline", "redis", "reflection",
         "session", "shmop", "simplexml", "snmp", "soap", "sockets", "sourceguardian",
         "spl", "sqlite3", "standard", "tidy", "tokenizer", "xml", "xmlreader", "xmlrpc",
         "xmlwriter", "xsl", "zip", "zlib"
       ],
      "extdended": [],
    },
    "72": {
       "default": [
         "bcmath", "bz2", "calendar", "core", "ctype", "curl", 
         "date", "dom", "ereg", "exif", "fileinfo", "filter", "ftp", 
         "gd", "gettext", "gmp", "hash", "iconv", "imap", "intl", "json",
         "libxml", "mbstring", "mhash", "mysqlnd", "nd_mysqli", "openssl",
         "pcntl", "pcre", "pdo", "pdo_mysql", "pdo_pgsql", "pdo_sqlite",
         "pgsql", "phar", "posix", "pspell", "readline", "redis", "reflection",
         "session", "shmop", "simplexml", "snmp", "soap", "sockets", "sourceguardian",
         "spl", "sqlite3", "standard", "tidy", "tokenizer", "xml", "xmlreader", "xmlrpc",
         "xmlwriter", "xsl", "zip", "zlib"
       ],
      "extdended": [],
    },
    "73": {
       "default": [
         "bcmath", "bz2", "calendar", "core", "ctype", "curl", 
         "date", "dom", "ereg", "exif", "fileinfo", "filter", "ftp", 
         "gd", "gettext", "gmp", "hash", "iconv", "imap", "intl", "json",
         "libxml", "mbstring", "mhash", "mysqlnd", "nd_mysqli", "openssl",
         "pcntl", "pcre", "pdo", "pdo_mysql", "pdo_pgsql", "pdo_sqlite",
         "pgsql", "phar", "posix", "pspell", "readline", "redis", "reflection",
         "session", "shmop", "simplexml", "snmp", "soap", "sockets", "sourceguardian",
         "spl", "sqlite3", "standard", "tidy", "tokenizer", "xml", "xmlreader", "xmlrpc",
         "xmlwriter", "xsl", "zip", "zlib"
       ],
      "extdended": [],
    },
    "74": {
       "default": [
         "bcmath", "bz2", "calendar", "core", "ctype", "curl", 
         "date", "dom", "ereg", "exif", "fileinfo", "filter", "ftp", 
         "gd", "gettext", "gmp", "hash", "iconv", "imap", "intl", "json",
         "libxml", "mbstring", "mhash", "mysqlnd", "nd_mysqli", "openssl",
         "pcntl", "pcre", "pdo", "pdo_mysql", "pdo_pgsql", "pdo_sqlite",
         "pgsql", "phar", "posix", "pspell", "readline", "redis", "reflection",
         "session", "shmop", "simplexml", "snmp", "soap", "sockets", "sourceguardian",
         "spl", "sqlite3", "standard", "tidy", "tokenizer", "xml", "xmlreader", "xmlrpc",
         "xmlwriter", "xsl", "zip", "zlib"
       ],
      "extdended": [],
    },
    "80": {
       "default": [
         "bcmath", "bz2", "calendar", "core", "ctype", "curl", 
         "date", "dom", "ereg", "exif", "fileinfo", "filter", "ftp", 
         "gd", "gettext", "gmp", "hash", "iconv", "imap", "intl", "json",
         "libxml", "mbstring", "mhash", "mysqlnd", "nd_mysqli", "openssl",
         "pcntl", "pcre", "pdo", "pdo_mysql", "pdo_pgsql", "pdo_sqlite",
         "pgsql", "phar", "posix", "pspell", "readline", "redis", "reflection",
         "session", "shmop", "simplexml", "snmp", "soap", "sockets", "sourceguardian",
         "spl", "sqlite3", "standard", "tidy", "tokenizer", "xml", "xmlreader", "xmlrpc",
         "xmlwriter", "xsl", "zip", "zlib"
       ],
      "extdended": [],
    },
    "81": {
       "default": [
         "bcmath", "bz2", "calendar", "core", "ctype", "curl", 
         "date", "dom", "ereg", "exif", "fileinfo", "filter", "ftp", 
         "gd", "gettext", "gmp", "hash", "iconv", "imap", "intl", "json",
         "libxml", "mbstring", "mhash", "mysqlnd", "nd_mysqli", "openssl",
         "pcntl", "pcre", "pdo", "pdo_mysql", "pdo_pgsql", "pdo_sqlite",
         "pgsql", "phar", "posix", "pspell", "readline", "redis", "reflection",
         "session", "shmop", "simplexml", "snmp", "soap", "sockets", "sourceguardian",
         "spl", "sqlite3", "standard", "tidy", "tokenizer", "xml", "xmlreader", "xmlrpc",
         "xmlwriter", "xsl", "zip", "zlib"
       ],
      "extdended": [],
    },
    "82": {
       "default": [
         "bcmath", "bz2", "calendar", "core", "ctype", "curl", 
         "date", "dom", "ereg", "exif", "fileinfo", "filter", "ftp", 
         "gd", "gettext", "gmp", "hash", "iconv", "imap", "intl", "json",
         "libxml", "mbstring", "mhash", "mysqlnd", "nd_mysqli", "openssl",
         "pcntl", "pcre", "pdo", "pdo_mysql", "pdo_pgsql", "pdo_sqlite",
         "pgsql", "phar", "posix", "pspell", "readline", "redis", "reflection",
         "session", "shmop", "simplexml", "snmp", "soap", "sockets", "sourceguardian",
         "spl", "sqlite3", "standard", "tidy", "tokenizer", "xml", "xmlreader", "xmlrpc",
         "xmlwriter", "xsl", "zip", "zlib"
       ],
      "extdended": [],
    },
    "83": {
       "default": [
         "bcmath", "bz2", "calendar", "core", "ctype", "curl", 
         "date", "dom", "ereg", "exif", "fileinfo", "filter", "ftp", 
         "gd", "gettext", "gmp", "hash", "iconv", "imap", "intl", "json",
         "libxml", "mbstring", "mhash", "mysqlnd", "nd_mysqli", "openssl",
         "pcntl", "pcre", "pdo", "pdo_mysql", "pdo_pgsql", "pdo_sqlite",
         "pgsql", "phar", "posix", "pspell", "readline", "redis", "reflection",
         "session", "shmop", "simplexml", "snmp", "soap", "sockets", "sourceguardian",
         "spl", "sqlite3", "standard", "tidy", "tokenizer", "xml", "xmlreader", "xmlrpc",
         "xmlwriter", "xsl", "zip", "zlib"
       ],
      "extdended": [],
    }}
    
    for selected_php_version in versions_arr:
      default_v = "php{}-php".format(selected_php_version)
      cli = "default_v{}".format("cli")
      install_list = [default_v, cli]
      
      for ext_list in php_version_extensions[selected_php_version]["default"]:
        install_list.append("{0}-{1}".format(default_v, ext_list))
    
    subprocess.run(["dnf", "install", " ".join(install_list), "--yes"], check=True)
    