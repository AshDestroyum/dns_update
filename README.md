# dns_update
A simple Python script that allows you to change DNS with ease, only for Windows. Requires admin privileges.

# How to use

- Make sure the program is running with elevated priveleges, it won't have access to the network adpater for changes since it's Powershell
- When prompted it will list the current connection, the adapter's name, and it's listed DNS server
<p align="center"> <img src="https://i.imgur.com/IWhivJ2.png" height="80%" width="80%" alt="DNS window"/> </p>

- Enter the specified primary DNS
<p align="center"> <img src="https://i.imgur.com/yeguiFV.png" height="80%" width="80%" alt="DNS window"/> </p>

- The program will confirm that primary DNS has been changed

<p align="center"> <img src="https://i.imgur.com/IjCeHEo.png" height="80%" width="80%" alt="DNS window"/> </p>

- You can confirm the DNS change from either Powershell or the control panel

<p align="center"> Powershell w/ ipconfig /all </br> <img src="https://i.imgur.com/Xf9ZegJ.png" height="80%" width="80%" alt="DNS window"/> </p>

<p align="center"> Control Center confirming updated DNS </br> <img src="https://i.imgur.com/1LzZ2pp.png" height="80%" width="80%" alt="DNS window"/> </p>

At the moment the progam is able to change only the primary DNS 
