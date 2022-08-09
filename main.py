#!/usr/bin/python3 

#Author: Andy Garcia

import parser_utils
import sys

#Main function will call functions from parser_utils.py file
def main():

    if len(sys.argv) == 2: 
        templist = []
        source, dest, time, length = (parser_utils.parse_data(sys.argv[1])) #Parses data
        templist = parser_utils.combine_data(source, dest, time, length)    #Combines the data
        x = parser_utils.sort_packets(templist) #Organizes the data by user input
        parser_utils.print_packets(x)   #Outputs packet to screen

    elif len(sys.argv) == 3:
        if parser_utils.check_ips(sys.argv[2]): #Checks if IP entered is valid
            templist = []
            source, dest, time, length = (parser_utils.parse_data(sys.argv[1])) #Parses data from log file
            templist = parser_utils.combine_data(source, dest, time, length)    #Combines data
            Results = parser_utils.filter_packets(templist, len(sys.argv), sys.argv[2]) #Filters unwanted data via user input
            x = parser_utils.sort_packets(Results) #Organizes the packets in descending order
            parser_utils.print_packets(x) #Outputs packets to screen

    elif len(sys.argv) == 4:
         if parser_utils.check_ips(sys.argv[2]) and parser_utils.check_ips(sys.argv[3]): #Checks for both IP's entered if they're valid
            templist = []
            source, dest, time, length = (parser_utils.parse_data(sys.argv[1])) #Parses data from logfile
            templist = parser_utils.combine_data(source, dest, time, length)    #Combines data
            Results = parser_utils.filter_packets(templist, len(sys.argv), sys.argv[2], sys.argv[3])    #Filters unwanted data via user input
            parser_utils.sort_packets(Results)  #Organizes packets in descending order
            x = parser_utils.sort_packets(Results)  #Stores the result in a variable
            parser_utils.print_packets(x)   #Outputs the results to the screen

    else:
        print("Usage:",sys.argv[0], "<file_name>  <source_IP>  <dest_IP>") #Error message

main()