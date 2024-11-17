#!/bin/bash
echo "!!!Welcome HSP installer!!!"

# Function to prompt the user for input
prompt() {
    local prompt_text="$1"
    local default_value="$2"
    local user_input

    read -p "$prompt_text ($default_value): " user_input
    echo "${user_input:-$default_value}"
}

in_array() {
  ar="$1"
  check="$2"
  exists=true
  for str in $check
   do
    if [[ "${ar[@]}" =~ "$str" ]]
	  then
	    exists=$($exists && true)
	  else
	    exists=$($exists && false)
	  fi
  done
  echo "$exists"
}

db_prompt() {
   ask="Which database you want to install (mariadb,mysql,postgresql,mongodb, all, none) ?"
   answer=$(prompt "$ask")
   all_dbs=("mysql" "mariadb" "postgresql" "mongodb")

   if [ "$answer" == "all" ]
    then
      echo "${all_dbs[*]}"
	  return
   elif [ "$answer" == "none" ]
     then
       selected_dbs=""
	   return
	else
	  selected_dbs=$(in_array "$all_dbs" "$answer")
   fi
   
   if [ $selected_dbs ] 
     then
	   echo "$answer"
	 else
	   echo "$answer not found."
	fi
}

mailserver_prompt() {
   ask="Please specify which email server would you like install ? (exim, postfix, none) ?"
   echo $(prompt "$ask")
}

webserver_prompt() {
  ask="Please specify which webserver you would like to install ? (apache, nginx, apache_nginx_reverse, none)"
  echo $(prompt "$ask")
}

development_prompt() {
  ask="Please specify which development languages you would like to install ? (php, python, nodejs, none, all) ?"
  echo $(prompt "$ask")
}

dns_prompt() {
  ask="Please specify which dns server you would like to install ? (bind, none) ?"
  echo $(prompt "$ask")
}

ftp_prompt() {
  ask="Please specify which ftp server you would like to install ? (pureFtpd, proFtpd, none) ?"
  echo $(prompt "$ask")
}


#webserver=$(webserver_prompt)
#smtp_server=$(mailserver_prompt)
#development=$(development_prompt)
#dns=$(dns_prompt)
#ftp=$(ftp_prompt)
#sys_webserver="apache2"

#check do we have a python installed



check_python() {
  pythoncmd=''

  if command -v python3 &> /dev/null
	then
		pythoncmd=python3
	fi

  echo $pythoncmd
}

pythoncmd=$(check_python)
yesno=false

if [ "$pythoncmd" == "" ]
then
   yesno=$(prompt "There is no python installed in the system, you need to install python 3 to continue. contnue ?")
   if ["$yesno" == "yes"]
    then
	  dnf install python3 --yes
	else
	  exit
	fi
fi

pythoncmd=$(check_python)
if [ "$pythoncmd" == "" ]
then
  echo "Python not installed. we can not continue."
  exit
fi

