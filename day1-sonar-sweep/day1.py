#!/usr/bin/python

import sys

def main(argv):
    #get the input file
    inputFile = open('test.txt','r')

    #read tthe input file
    content = inputFile.readlines() 

    #array of depths
    depths = []

    #counter for the number of increases  
    increases = 0
    decreases = 0

    # Iterating through the depths
    for line in content: 
        depths.append(int(line.strip('\n')))

    print(len(depths))
    #iteratte through the array and count increases
    for indx in range(1, len(depths)):
        if depths[indx] > depths[indx-1]:
           # print(str(depths[indx]) + '>' + str(depths[indx-1]))
            increases += 1
           # print('up: ' + str(increases))
        else: 
           # print(str(depths[indx]) + '<' + str(depths[indx-1]))
            decreases +=1
           # print('down: ' + str(decreases))


    print('total:')
    print(increases)
   # print(decreases)
    inputFile.close()

if __name__ == "__main__":
   main(sys.argv[1:])