# unidimensional / onedimensional
from os import system

system("cls")

print("\n")

destinations = [
    [         #0
    "-Paris",    #0
    "-Rome",     #1
    "-London",   #2
    ],
    [         #1
    "-NY",       #0
    "-Toronto",  #1
    "-DC",       #2
      
    ]
]

print (
  "EU:", "\n", destinations[0][0], "\n",
  destinations [0][1], "\n",
  destinations [0][2]
  )
print (
  "US:", "\n", destinations[1][0], "\n",
  destinations [1][1], "\n",
  destinations [1][2]
  )



# destination NAME change
    #  destinations [0][2] = "Pisa"
    
    

# print(f"This is a list with {len(destinations)} elements")
##########################################
#   print( destinations[0])
#   destinations [1] = "Madrid"
#    print( destinations[1])

#############################################

#1. looping using index 
  # for i in range(len(destinations)):  # 0,1,2
  #    print(f" {i} {d})
  
# 2. looping using values#

# for d in destinations: 
#     print(d)


# HW1
# using for inside for print all destinations
# must look so:

# EU:
#   - Paris
#   - Rome
# ....
#  US:
#   - NY
#   ...