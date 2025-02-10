# John Vogel 10/22/2024
# john.vogel123@gmail.com
# script to extract page names and last modified dates from sitemap.xml file
# working directory is /home/jvogel/MaryCycleWisdom

# JPV:sample execution
#python3 argParseFileIoSample.py -h
#python3 ../scripts/argParseFileIoSample.py \
#../data/raw-house-data.csv \
#./sitemap.results \

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
print("Data input file: ",args.inFile1)
print("Results ouput file: ",args.outFile1)
print("Current working directory: ",args.workDir)
print(parser.parse_args())

os.chdir(args.workDir)

with open(args.inFile1, "r") as sourceDataFile:
    stringList = sourceDataFile.readlines( )
    #print(stringList)
print("List length is: ",len(stringList))
exit(999)

inputDataFileName = "./sitemap.xml"
outputDataFileName = "./mungedData.txt"
workingDir = "/home/jvogel/Documents/MaryCycleWisdom"

os.chdir(workingDir)

with open(inputDataFileName, "r") as sourceDataFile:
    stringList = sourceDataFile.readlines( )
    #print(stringList)
print("List length is: ",len(stringList))
print("Debug: ",stringList[5])
#sourceDataFile = open(inputDataFileName, "r")
#tempReadLine = sourceDataFile.readline()
outputDataFile = open(outputDataFileName, "w")

#print(tempReadLine)

#print(sourceDataFile.readlines())
#tempReadLines = sourceDataFile.readlines()
print("Test")
#print(tempReadLines)

sourceDataFile.close()
outputDataFile.close()
#print(sourceDataFile.read())
#print("Opening ./sitemap.xml file for processing")
#print("Current working directory is now:", os.getcwd(),"\n")
#sourceDataFile = open(r"./sitemap.xml","r") # r prefix means ignore special chars in file name
#outputDataFile = open("./mungedData.txt", "w")
#cwd = os.getcwd()
#print("Current working directory is:", cwd,"\n")
#print("\nhello my friends")
#name = input("Please, enter your name: \n")
#print(f"Hello, {name}!")
