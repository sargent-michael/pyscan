# Simple python port scanner

pyscan is an extremely simple port scanner. I mainly wrote this program for just messing around and to get familiar with argparse and sockets. I do plan on adding to this later on to create a more robust port scanner, however, I currently do not have the time. 

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
Example of scanning Google on 53, 80, 443:

```bash
./pyscan.py -i 8.8.8.8 -p 53 80 443
[+] IP = 8.8.8.8
[+] Port = [53, 80, 443]
[+] Continue? y
[+] Initializing scan...

Port 53 is open
Port 443 is open
```