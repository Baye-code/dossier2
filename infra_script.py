from getpass import getpass
from netmiko import ConnectHandler

username = input("Veuillez entrer votre nom d'utilisateur: ")
password = getpass.getpass("Veuillez entrer votre mot de passe")

HOST = {

}

connect = ConnectHandler(**HOST)
