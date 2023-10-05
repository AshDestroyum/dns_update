# This script was to made to change your DNS in a more efficient manner, always rememmber to run this script under
# admin privileges for it to work, only for Windows.


import subprocess
import sys
import ctypes
import os
import re
from time import sleep

# Checking for elevated privileges
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


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



def validate_dns(dns):
	# Validating  DNS input
	valid = re.compile("\b(?:(?:2(?:[0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9])\.){3}(?:(?:2([0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9]))\b")

	if valid.match(dns) is None:
		sys.exit("This is not a valid IPv4 DNS...")
		sleep(3)

	# Checking conidtions for DNS

	# To reset DNS settings
	if dns == "":
		reset = f"Set-DnsClientServerAddress -InterfaceAlias '{current_conn()}' -ResetServerAddresses"
		subprocess.run(["Powershell", "-Command", reset])
		print("DNS reset complete!")
		sleep(3)
		sys.exit()
	else:
		pass


def set_dns(dns):
# Setting the DNS
	rule3 = f"Set-DnsClientServerAddress -InterfaceAlias '{current_conn()}' -ServerAddresses ('{dns}')"

	result = subprocess.run(["Powershell", "-Command", rule3])

	print("DNS change complete!")

	sleep(3)

def main():
	if is_admin():
		pass
	else:
		print("Not running with elevated privileges.")
		sleep(3)
		sys.exit()

	print(f"Current connection: {current_conn()}")

	print(f"Current DNS: {current_dns(current_conn())}")

	dns = input("Enter the DNS for the adapter, leave empty then press enter to reset:\n")

	validate_dns(dns)

	set_dns(dns)



if __name__ == "__main__":
	main()