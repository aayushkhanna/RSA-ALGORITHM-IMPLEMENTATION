import random as rn
import numpy as np		
	
def gcd(phi_n,i):
        
        x=np.gcd(phi_n,i)

        if(x==1):
            return 1
        else:
            return 0
            



print()
print("************************* |||||  RIVEST SHAMIR ADLEMAN  ||||| *************************")

print("[ * ENCRYPTION * ]")
print()

prime_l1=[13,17,19,37,43,53,61]
prime_l2=[23,29,31,41,47,59,67]

i1=rn.randint(0,2);
i2=rn.randint(0,2);

p=prime_l1[i1]
q=prime_l2[i2]

n=int(p*q)

phi_n=int((p-1)*(q-1))


for i in range(2,phi_n):
	e=gcd(phi_n,i)
	if(e==1):
		e=i
		break	



alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

message=input("Enter Message: ")

message=message.upper()

mess_list=[]

for i in message:
	mess_list.append(int(ord(i))-48)


print("|||||||||||||||||||||")
print("----------Public Key: {}".format(e))
print()

cipher_text=[]

for i in mess_list:
        cipher_text.append((i**e)%n)

print("----------Cipher Text: ",end="")

for i in cipher_text:
        print(i,end="")

print()
print()


print("[ * DECRYPTION * ]")
print()



d=1

while 1:
	v=(e*d)%phi_n
	if(v==1):
		break
	d=d+1

d=int(d)
print("---------- Private Key: {}".format(d))
print()

decrpt_message=[]



for i in cipher_text:
	
	value=((i**d)%n)
	if(value>9):
		value=value-17
		decrpt_message.append(alpha[value])
	else:
                decrpt_message.append(value)


    

print("---------- Decrpted Message: ",end="")
for i in decrpt_message:
        print(i,end="")
print()

print("************************* |||||  *******************  ||||| *************************")
print()





