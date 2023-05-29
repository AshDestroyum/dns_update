import subprocess
import sys


rule = "Get-NetConnectionProfile | Select-Object -ExpandProperty InterfaceAlias"

command = subprocess.check_output(["Powershell", "-Command", rule], encoding='utf-8')

print(f"Current connection: {command}")

adapter = str(command).replace("\n", "")

dns = input("Enter the DNS for the adapter:\n")
text = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j',
'k','l','m','n','o','p','q',
'r','s','t','u','v','w','x','y',
'z','!','@','#','$','%','^','&','*','(',')','_','+','{','}','|',':','<','>','?','`','~']

if len(dns) > 15:
	sys.exit("This is not a real DNS...")

for char in dns:

	if char in text:
		sys.exit("This is not a real DNS...There is text.")




rule2 = f"Set-DnsClientServerAddress -InterfaceAlias '{adapter}' -ServerAddresses ('{dns}')"

result = subprocess.run(["Powershell", "-Command", rule2])

