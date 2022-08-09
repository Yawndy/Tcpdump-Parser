#!/usr/bin/python3

#Author: Andy Garcia


import sys        
import re
from collections import defaultdict
import datetime

#Function will check if the IP entered is a valid IP address
def check_ips(source_IP):  
    regex = r'^([0-9]|[0-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[0-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[0-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[0-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$'
    if(re.match(regex,source_IP)):
        return True

#Function will parse source, destination, timestamp, and length from valid lines
def parse_data(filename):
    source_IP = []
    dest_IP = []
    packet_time = []
    packet_length = []
    regexvalid = r'(^\d{2}:\d{2}:\d{2}).*IP.*(length.*\d{1,6}$)'
    regextime = r'\d{2}:\d{2}:\d{2}'
    regexIP = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    regexlength = r'\d{1,6}$'

    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    for line in lines: #Loops through every line looking for source, dest, time, and length of packet
        if (re.findall(regexvalid, line)):
            for string in line.split():
                if(re.match(regextime, string)):
                    packet_time.append(string)
                    break
            for string in line.split("IP "):
                if(re.match(regexIP, string)):
                    source_IP.append(remove_ports(string))
                    break
            for string in line.split("> "):
                if(re.match(regexIP, string)):
                    dest_IP.append(remove_ports(string))
                    break
            for string in line.split("length "):
                if(re.match(regexlength, string)):
                    packet_length.append(string.strip())
                    break 
    return source_IP, dest_IP, packet_time, packet_length

#Removes any port numbers attached to an IP address
def remove_ports(string):
    regexIP = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    NoPortIP = []
    tempString = (string.split()[0]) 
    NoPortIP.append(tempString.rsplit(".",1)[0])
    return NoPortIP

#Combines the data into a new list with source, destination, first timestamp, last timestamp, and total packet size
def combine_data(source, dest, time, length):
    CombinePacket = [(source[i], dest[i], time[i], length[i]) for i in range(len(source))]
    result = []
    data = defaultdict(list)

    for package in CombinePacket: #Loops through the packet and creates a dictionary
        data[(package[0][0],package[1][0])].append((package[2],package[3])) 
       
    for key, value in data.items(): #Loops through the dictionary for source+destination matches
        value = sorted(value,key = lambda x : x[0])
        first_time = value[0][0]
        last_time = value[-1][0]
        sum_length = sum(int(v[1]) for v in value)
        result.append([key[0],key[1],first_time,last_time,sum_length])
    return result

#Filters packets based on user's input for source and destination IP addresses
def filter_packets(Data, TotalArg, *args):
    result = []
    if(TotalArg == 3): #Checks for just source address input
        for line in Data:
            if(line[0] == args[0]):
                result.append(line)
        return result

    elif(TotalArg == 4):  #Checks for both source and destination address input
        for line in Data:
            if(line[0] == args[0] and line[1] == args[1]):
                result.append(line)
        return result

#Sorts packets based on total packet size in descending order
def sort_packets(FilteredData):    
    SortedList = []
    NewList = []
    for line in FilteredData: #Loops through the data and sorts it in descending order
        SortedList.append(sorted(FilteredData,key = lambda x : x[4], reverse = True))
    for i in range(len(FilteredData)):
        NewList.append(SortedList[0][i])
    return NewList

#Outputs the packets to the terminal in a visually appealing way
def print_packets(sortedpackets):
    for line in sortedpackets: #Loops through each element in the data and outputs a message
        print("Source:",line[0],"\t","Destination",line[1],"\t","Total:",line[4],"\t")
   