import netmiko
import time
from netmiko import ConnectHandler
import File_compare as FC
from colorama import Fore


"""
Please enter your credentials to log in to the router
"""

username = input("Please Enter Your User Name: ")
password = input("Please Enter Your Password: ")


"""
node_list.txt: contains the list of the MGT IPs/Hostnames
"""

with open("node_list.txt") as f1:
    node_list=f1.readlines()
with open("command_list.txt") as f2:
    commands1=f2.readlines()

"""
The list of commands as a list
"""

for hostname1 in node_list:

    cisco_router = {
        'device_type': 'cisco_ios',
        'host': hostname1,
        'username': username,
        'password': password,
        'secret': password,
        'port': 22,
    }
    pre = hostname1.strip('\n') + "_PRE"+ ".txt"
    post = hostname1.strip('\n') + "_POST" + ".txt"

    try:
        ssh=ConnectHandler(**cisco_router)
        ssh.enable()

    except Exception as e:
        print(e)
        print("****************************************************************")
        print(Fore.WHITE,f"Please check the issue in {hostname1.strip()}")
        print("****************************************************************")
        pass
    else:
        with open (pre,'w')as f1:
            result1=ssh.send_command("show run")
            f1.write(result1)
        print(Fore.WHITE,f"++++++++++++++++Started Configuring {hostname1} ++++++++++++++++ ")
        result = ssh.send_config_set(commands1)
        ssh.exit_config_mode()

        with open (post,'w') as f2:
            result2=ssh.send_command("show run")
            f2.write(result2)

        FC.pre_post_comp(post,pre)








