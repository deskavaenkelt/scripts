#!/bin/bash
# Verify password


invalid_input=true

while [ $invalid_input ];
do
  read -sp 'Password: ' passvar1
  echo
  read -sp 'Retype Password: ' passvar2
  echo

  if [[ $passvar1 == $passvar2  ]]
  then
    invalid_input=$false
  else
    echo 'Passwords dont match, retype passwords!'
    echo
  fi

done

echo $passvar1
