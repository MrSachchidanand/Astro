import time
print("____________________________________WELCOME____________________________________")
print()
in_put = int(input("Enter the list :"))







def first():
 l= [500,500,500,'X']
 for i in range(0,1000000):
     l.pop()
     l.append(i)
     if l[0]+l[1]==l[1]+l[2]==l[2]+l[3]==l[0]+l[3]==l[1]+l[3]==l[0]+l[2]:
           print('True '+str(i))
#[8,1,6,3,5,7,4,9,'x']
#write the numbers in correct order
#[0,1,2,3,4,5,6,7,8]
#eg [2,7,6,1,8,3,4,9,'x'] ; [4,3,8,1,6,7,2,9,'x']
def second():
 l =[6,7,2,9,4,3,8,1,'x']
 for i in range(0,1000000):
  l.remove(l[1])
  print(l)
  l.insert(1,i)
  print(l)

  if l[0]+l[1]+l[2]==l[2]+l[3]+l[4]==l[4]+l[5]+l[6]==l[0]+l[7]+l[6]==l[6]+l[8]+l[2]==l[0]+l[8]+l[4]==l[8]+l[1]+l[5]==l[7]+l[8]+l[3]:
    print("True "+str(i))

















