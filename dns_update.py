# This script was to made to change your DNS in a more efficient manner, always rememmber to run this script under
# admin privileges for it to work, only for Windows.


import subprocess
import sys
import ctypes
import os

# Checking for elevated privileges
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    pass
else:
    sys.exit("Not running with elevated privileges.")


# To display current adapter
def current_conn():

	rule = "Get-NetConnectionProfile | Select-Object -ExpandProperty InterfaceAlias"

	command = subprocess.check_output(["Powershell", "-Command", rule], encoding='utf-8')

	adapter = str(command).replace("\n", "")

	return adapter

# To display current DNS
def current_dns(connection_name):

	rule2 = f"Get-NetIPInterface -AddressFamily IPv4 -InterfaceAlias '{connection_name}' | Select-Object -ExpandProperty ifIndex"

	command2 = subprocess.check_output(["Powershell", "-Command", rule2], encoding='utf-8')

	index = str(command2).replace("\n", "")

	index_int = int(index)

	rule3 = f"Get-DnsClientServerAddress -InterfaceIndex {index_int} -AddressFamily IPv4 | Select-Object -ExpandProperty ServerAddresses"

	command3 = subprocess.check_output(["Powershell", "-Command", rule3], encoding='utf-8')

	now_dns = str(command3).replace("\n", "")

	return now_dns

print(f"Current connection: {current_conn()}")

print(f"Current DNS: {current_dns(current_conn())}")


# DNS input
dns = input("Enter the DNS for the adapter:\n")
text = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j',
'k','l','m','n','o','p','q',
'r','s','t','u','v','w','x','y',
'z','!','@','#','$','%','^','&','*','(',')','_','+','{','}','|',':','<','>','?','`','~']

# Checking conidtions for DNS
if len(dns) > 15:
	sys.exit("This is not a real DNS...")

for char in dns:

	if char in text:
		sys.exit("This is not a real DNS...There is text.")



# Setting the DNS
rule3 = f"Set-DnsClientServerAddress -InterfaceAlias '{current_conn()}' -ServerAddresses ('{dns}')"

result = subprocess.run(["Powershell", "-Command", rule3])

print("DNS change complete!")

