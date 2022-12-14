#!/usr/bin/python3
import argparse
import socket


def scan(ip, ports):
    # Does the magic
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        # Prints the results
        result = s.connect_ex((ip,port))
        if result ==0:
            print("Port {} is open".format(port))
        s.close()


def main():
    # Arguments for the program
    parser = argparse.ArgumentParser(description='Simple Python Port Scanner')
    parser.add_argument('-i', '--ip', action="store", dest="ip", help='ip address to scan', metavar='', required=True)
    parser.add_argument('-p', '--port', action="store", dest="port", type=int, help='port to scan on the host', 
                            metavar='', required=True, nargs='+')

    # Args to Vars
    args = parser.parse_args()
    ip = args.ip
    port = args.port

    # Verification Checks
    info = input("[+] IP = {}\n[+] Port = {}\n[+] Continue? ".format(ip, port))
    
    # If input is correct then the program will start the scan. Otherwise, the program will stop.
    if info == "y" or info == 'yes':
        print("[+] Initializing scan...\n")
        scan(ip, port)
    else:
        print("[-] Aborting... ")


if __name__ == "__main__":
    main()