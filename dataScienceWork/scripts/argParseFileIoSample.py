# John Vogel 10/22/2024
# john.vogel123@gmail.com
# script to extract page names and last modified dates from sitemap.xml file
# working directory is /home/jvogel/MaryCycleWisdom

# JPV:sample execution
#python3 argParseFileIoSample.py -h
#python3 ../scripts/argParseFileIoSample.py \
#../data/sitemap.xml \
#./sitemap.results \
#. \

import os # running unix commands
import argparse # argument parsing

parser = argparse.ArgumentParser(
  prog='argParseFileIoSample.py',
  description='Program to show python basic capabilities',
  epilog='send feedback to john.vogel123@gmail.com')

parser.add_argument("inFile1")
parser.add_argument("outFile1")
parser.add_argument("workDir")
parser.parse_args()

args = parser.parse_args()

#print(args)
#print(parser.parse_args()) # does the same thing as print(args)
#print("Data input file: ",args.inFile1)
#print("Results ouput file: ",args.outFile1)
#print("Current working directory: ",args.workDir)

with open(args.inFile1, "r") as sourceDataFile:
    stringList = sourceDataFile.readlines( )
    #print(stringList)
print("List length is: ",len(stringList))
#print("Debug: ",stringList[20])
#print(sourceDataFile.readlines())

outputDataFile = open(args.outFile1, "w")

################  xml parsing code not written yet  #######
################  xml parsing code not written yet  #######
################  xml parsing code not written yet  #######
################  xml parsing code not written yet  #######

sourceDataFile.close()
outputDataFile.close()

#sourceDataFile = open(r"./sitemap.xml","r") # r prefix means ignore special chars in file name
#name = input("Please, enter your name: \n")
#print(f"Hello, {name}!")
