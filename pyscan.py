#!/usr/bin/python3
import socket
import argparse


def scan(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
     
    result = s.connect_ex((ip,port))
    if result ==0:
        print("\nPort {} is open".format(port))
    s.close()


def main():
    # Arguments for the program
    parser = argparse.ArgumentParser(description='Simple Python Port Scanner')
    parser.add_argument('-i', '--ip', action="store", dest="ip", help='ip address to scan', metavar='', required=True)
    parser.add_argument('-p', '--port', action="store", dest="port", type=int, help='port to scan on the host', metavar='', required=True)

    # Args to Vars
    args = parser.parse_args()
    ip = args.ip
    port = args.port

    # Verification Checks
    info = input("[+] IP = {}\n[+] Port = {}\n[+] Continue? ".format(ip, port))
    
    # If input is correct then the program will start the scan. Otherwise, the program will stop.
    if info == "y" or info == 'yes':
        print("[+] Starting scan...")
        scan(ip, port)
    else:
        print("")


if __name__ == "__main__":
    main()