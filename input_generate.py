import random as rn

file  = open("6-round_DES\input.txt", "w")
fi = open("6-round_DES\ptext.txt", "w")

fi.write("3-Musketeers\n" + "ThreeMusketeers\n" + "4\n" + "read\n")

## INITIAL PERMUTATION (IP) 

IP = [
  58,50,42, 34,26,18,10,2,
  60,52,44,36,28,20,12,4,
  62,54, 46, 38, 30, 22, 14,6,
  64, 56, 48, 40,32,24, 16, 8,
  57, 49, 41, 33,25,17, 9,1,
  59, 51,43,35,27,19,11,3,
  61,53,45,37,29,21,13, 5,
  63,55, 47,39,31,23,15,7
]

## REVERSE PERMUTATION (RFP) 

RFP = [
  8,40,16,48,24,56,32,64,
  7, 39,15,47,23,55,31,63,
  6,38,14,46,22,54,30,62,
  5,37,13,45, 21,53,29,61,
  4,36,12,44,20,52,28,60,
  3, 35, 11,43,19,51,27,59,
  2, 34, 10, 42,18, 50,26,58,
  1,33,9,41, 17, 49, 25,57,
]


LR = [0,1,0,0, 0,0,0,0, 0,1,0,1, 1,1,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0,
      0,0,0,0, 0,1,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0 ]

fun = {}

for i in range(0,16):
  fun.setdefault(i, chr(ord('f')+i))

#print(fun)

LR_1, LR_2, L1, L2 = [None]*64, [None]*64, [None]*64, [None]*64
i, j = 0, 0

rn.seed(0)

for i in range(0,60000):
  for j in range(0,64):
    L1[j] = LR_1[j] = rn.randint(0,1)
    L2[j] = LR_2[j] = LR[j] ^ LR_1[j]
  file.write(''.join(list(map(str, LR_1))) + "\n" + ''.join(list(map(str, LR_2))) + "\n")

  for j in range(0,64):
    LR_1[IP[j]-1] = L1[j] 
    LR_2[IP[j]-1] = L2[j]
  #print(''.join(list(map(str, LR_1))) + "\n" + ''.join(list(map(str, LR_2))) + "\n")

  s1, s2 = str(), str()
  n = 8
  m1 = m2 = 0

  for i in range(0,64):
    if i%4==0 and i!=0:
      n = 8
      s1 = s1 + fun[m1]
      s2 = s2 + fun[m2]
      #print(m1, m2)
      m1 = m2 = 0
    
    m1 = m1 + LR_1[i]*n
    m2 = m2 + LR_2[i]*n
    n = n//2
  
  fi.write(s1 + "\nc\n" + s2 + "\nc\n")

fi.write("back\n" + "quit\n")
