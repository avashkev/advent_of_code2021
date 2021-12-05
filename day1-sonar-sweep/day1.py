#!/usr/bin/python

import sys

def main(argv):
   #get the input file
 #  inputFile = open('C:\\Users\\Nastasia\\Documents\\src\\advent_of_code2021\\day1-sonar-sweep\\test.txt','r')
   inputFile = open(argv[0],'r')

   #read the input file
   content = inputFile.readlines() 
   inputFile.close()
   
   #array of depths
   depths = []

   #counter for the number of increases  
   increases = 0

   # Iterating through the depths
   for line in content: 
      depths.append(int(line.strip('\n')))
   
   #the number of depths that will be added together and compared
   window = 3

   #get the first set of depths
   prevDepth = 0
   for i in range(0, window):
         prevDepth += depths[i]

   #iteratte through the array and count increases
   for indx in range(window, len(depths)):
      currDepth = 0
      for i in range(0, window):
         currDepth += depths[indx-i]
         
      if prevDepth < currDepth:
         increases += 1

      prevDepth = currDepth

   print("Total Increases: " + str(increases))
# print(decreases)


if __name__ == "__main__":
   main(sys.argv[1:])