#!/usr/bin/python

import sys

def main(argv):
    inputFile = open(argv[0],'r')

   # inputFile = open('C:\\Users\\Nastasia\\Documents\\src\\advent_of_code2021\\day2-dive\\test.txt','r')

    #read the input file
    content = inputFile.readlines() 
    inputFile.close()

    directions = []

    for line in content:
        directions.append(line.split(' '))

    yPos = 0 #depth
    xPos = 0 #horizontal position

    for command in directions:
        if command[0] == 'up':
            yPos -= int(command[1].strip('\n'))
        elif command[0] == 'down':
            yPos += int(command[1].strip('\n'))
        elif command[0] == 'forward':
            xPos += int(command[1].strip('\n'))

    print(str(xPos*yPos))


if __name__ == "__main__":
   main(sys.argv[1:])