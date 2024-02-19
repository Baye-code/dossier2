from getpass import getpass
from netmiko import ConnectHandler

username = input("Veuillez entrer votre nom d'utilisateur: ")
password = getpass.getpass("Veuillez entrer votre mot de passe")

HOST = {
	"ip": "192.168.10.10",
	"device_type": "cisco",
	"username": username,
	"password": password
}

connect = ConnectHandler(**HOST)

connect.send_command("sh vlan brief")
