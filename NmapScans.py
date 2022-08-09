#!/usr/bin/python3 

import python
nm = nmap.PortScanner()

while True:

    print("1. List Scan")
    print("2. Ping Scan")
    print("3. Port Scan")   
    print("4. Complex Port Scan")
    print("5. Exit program")

    userInput = input("Select a scan: ")

    if userInput == "1": #List Scan
        nm.scan(hosts='172.16.11.0/24', arguments='-n -sL')
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
        for host, status in hosts_list:
            print('{0}'.host)

    elif userInput == "2": #Ping Scan
        nm.scan(hosts='172.16.11.0/24', arguments='-n -sP -PE -PA21,23,80,3389')
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
        for host, status in hosts_list:
            print('{0}:{1}'.host)
            
    elif userInput == "3": #Port Scan
        nm.scan(hosts='172.16.11.0/24', arguments='-n -p0- -v -A -T5')
        for host in nm.all_hosts())
            print('---------------------------------------------------')
            print('Host : %s (%s)' % (host, nm[host].hostname()))
            print('State : %s' % nm[host].state())

            for proto in nm[host].all_protocols():
                print('----------')
                print('Protocol : %s' % proto)
                lport = nm[host][proto].keys()
                lport.sort()

                for port in lport:
                    print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

    elif userInput == "4": #Complex Port Scan
        nm.scan(hosts='172.16.11.0/24', arguments='-n -p0- -v -A -T5')
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
        for host, status in hosts_list:
            print('{0}:{1}'.host)
            print(nm.csv())

        for host in nm.all_hosts())
            print('---------------------------------------------------')
            print('Host : %s (%s)' % (host, nm[host].hostname()))
            print('State : %s' % nm[host].state())

            for proto in nm[host].all_protocols():
                print('----------')
                print('Protocol : %s' % proto)
                lport = nm[host][proto].keys()
                lport.sort()

                for port in lport:
                    print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

    elif userInput == "5":
        break
        
