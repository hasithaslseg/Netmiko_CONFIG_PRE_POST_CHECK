# Netmiko_CONFIG_PRE_POST_CHECK
This is an end to end script to get the pre-checks, configure and get the post-checks and compared the changes at one go for multiple devices

node_list.txt: contains the list of the MGT IPs/Hostnames
command_list.txt: contains the list of the commands to execute

The program will generate the Pre and post backup files with file names in the format <hostname><PRE/POST>.txt
  
  Finally the program will compare the PRE and POST files and print the additions and deletions
