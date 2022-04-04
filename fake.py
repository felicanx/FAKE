#!/usr/bin/python3
import argparse
import os
import requests
from termcolor import colored 
import subprocess


parser = argparse.ArgumentParser(description="FAKE is a recon automation tool for a particular domain you can use this as TYPE as  [ python3 fake.py -d domain.com ]")
parser.add_argument("-d",type=str,help="Domain",required=True)

x=parser.parse_args()



print(colored(" ++++++++++++++++++++++++++++++++++++++++++++++++++++++++","red",attrs=['bold']))
print(colored("+ _ ________      ____            _           _ _________+","blue",attrs=['bold']))
print(colored("+| |________|    /    \          | |   / /   | |_________+","blue",attrs=['bold']))
print(colored("+| |            / /  \_\         | |  / /    | |         +","blue",attrs=['bold']))
print(colored("+| |------     / /    \_\        | | / /     | |         +","blue",attrs=['bold']))
print(colored("+| |______|   / /      \_\       | |/ /      | |------   +","blue",attrs=['bold']))
print(colored("+| |         / / ====== \_\      | |\ \      | |------   +","blue",attrs=['bold']))
print(colored("+| |        / /          \_\     | | \ \     | |         +","blue",attrs=['bold']))
print(colored("+| |       / /            \_\    | |  \ \    | |---------+","blue",attrs=['bold']))
print(colored("+|_|      /_/              \_\   |_|   \ \   |_|---------+","blue",attrs=['bold']))
print(colored(" ++++++++++++++++++++++++++++++++++++++++++++++++++++++++","red",attrs=['bold']))
print("\n")
print("+++++ FAKE is a easy recon tool +++++")
print("+++++++++++++++++++++++++++++++++")
print(colored("Automation In Progress WAIT!!!!!!","red",attrs=['bold']))





file=open('subdomain.txt','w+')
file0=open('wordlist.txt','r')
content = file0.read()

subdomains = content.splitlines()
for subdomain in subdomains:
	d1=f"http://{subdomain}.{x.d}"
	d2=f"https://{subdomain}.{x.d}"

	try:
		requests.get(d1)
		file1 = open('subdomain.txt','a')
		file1.writelines(d1 + "\n")

		requests.get(d2)
		file2 = open('subdomain.txt','a')
		file2.writelines(d2 + "\n")


	except requests.ConnectionError:
		pass 
	finally:
		file0.close()

print("\n")
print(colored("+++++++++++++++++++++++++++++++++++++","blue",attrs=['bold']))
print(colored("        ||     ||    ||    ||   ","blue",attrs=['bold']))
print(colored("        VV     vv    vv    vv    ","blue",attrs=['bold']))
print(colored("~~~~~~~~CHECKING STATUS CODE~~~~~~~~~","red",attrs=['bold']))

filex=open('url_status.txt','w+')

port = open('subdomain.txt','r')
port0 = port.read()

port1 = port0.splitlines()

for p in port1:
	status = requests.get(p).status_code
	status=str(status)

	file5 = open('url_status.txt','a')
	file5.writelines(p+" = "+status+"\n")

print("\n")
print(colored("+++++++++++++++++++++++++++++++++++++","blue",attrs=['bold']))
print(colored("        ||     ||    ||    ||   ","blue",attrs=['bold']))
print(colored("        VV     vv    vv    vv    ","blue",attrs=['bold']))
print(colored("~~~~~~~~STATUS CODE IS DONE WORKING ON NSLOOKUP~~~~~~~~~","red",attrs=['bold']))


subprocess.call("nslookup -type=any > nslookup.txt {}".format(x.d), shell=True)

print("\n")
print(colored("+++++++++++++++++++++++++++++++++++++","blue",attrs=['bold']))
print(colored("        ||     ||    ||    ||   ","blue",attrs=['bold']))
print(colored("        VV     vv    vv    vv    ","blue",attrs=['bold']))
print(colored("~~~~~~~~NSLOOKUP DONE WORKING ON WHOIS~~~~~~~~~","red",attrs=['bold']))

subprocess.call("whois > whois.txt {}".format(x.d), shell=True)

print("\n")
print(colored("+++++++++++++++++++++++++++++++++++++","blue",attrs=['bold']))
print(colored("        ||     ||    ||    ||   ","blue",attrs=['bold']))
print(colored("        VV     vv    vv    vv    ","blue",attrs=['bold']))
print(colored("~~~~~~~~WHOIS DONE GO FORWARD WITH NMAP SCAN~~~~~~~~~","red",attrs=['bold']))

subprocess.check_output("mkdir nmap",shell=True)

subprocess.check_output("cd nmap",shell=True)

subprocess.call("nmap -sC -sV -oA ./nmap/output {}".format(x.d), shell=True)

print("\n")
print(colored("~~~~~~~~~~BASIC RECON IS COMPLETED~~~~~~~~~~","red",attrs=['bold']))
