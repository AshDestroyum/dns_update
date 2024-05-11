# dns_update
A simple Python script that allows you to change the **primary** DNS with ease, only for **Windows**. Requires admin privileges.

# How to install

1. Clone the repo

`git clone https://github.com/AshDestroyum/dns_update.git`

2. Use pip to install required modules:

`pip install -r requirements.txt`

3. Use the following command to create the exe:

`pyinstaller dns_update.py --onefile -i dns_icon.ico`


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

<p align="center"> Control Center confirming updated DNS </br> <img src="https://i.imgur.com/1LzZ2pp.png" height="60%" width="60%" alt="DNS window"/> </p>

At the moment the progam is able to change only the **primary** DNS 
