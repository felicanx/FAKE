#!/usr/bin/python3
import argparse
import os
import requests
import subprocess

print("+++++++++++++++++++++++++++++++++")
print("+ FAKE is a easy recon tool +++++")
print("+++++++++++++++++++++++++++++++++")
print("Automation In Progress WAIT!!!!!!")

parser = argparse.ArgumentParser(description="FAKE is a recon automation tool for a particular domain you can use this as TYPE as  [ python3 fake.py -d domain.com ]")
parser.add_argument("-d",type=str,help="Domain",required=True)

x=parser.parse_args()

os.system('touch subdomain.txt')

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

print("+++++++++++++++++++++++++++++++++")
print("        ||        ")
print("        VV        ")
print('Checking status code ')

os.system('touch url_status.txt')

port = open('subdomain.txt','r')
port0 = port.read()

port1 = port0.splitlines()

for p in port1:
	status = requests.get(p).status_code
	status=str(status)

	file5 = open('url_status.txt','a')
	file5.writelines(p+" = "+status+"\n")

print("+++++++++++++++++++++++++++++++++")
print("        ||        ")
print("        VV        ")
print('status code is done wait for nmap scan results')


subprocess.check_output("mkdir nmapp",shell=True)

subprocess.check_output("cd nmapp",shell=True)

subprocess.call("nmap -sC -sV -oA ./nmapp/output {}".format(x.d), shell=True)
