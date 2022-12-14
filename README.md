# Simple python port scanner

pyscan is an extremely simple port scanner. I mainly wrote this program for just messing around and to get familiar with argparse and sockets. I do plan on adding to this later on to create a more robust port scanner, however, I currently do not have the time. Also, this program only supports ipv4 and can only scan one port at a time.

Example of usuage: 

```bash
pyscan.py -h
usage: pyscan.py [-h] -i  -p

Simple Python Port Scanner

options:
  -h, --help    show this help message and exit
  -i , --ip     ip address to scan
  -p , --port   port to scan on the host
```
Example of scanning Google on 443:

```bash
[+] IP = 8.8.8.8
[+] Port = 443
[+] Continue? yes
[+] Starting scan...

Port 443 is open
```