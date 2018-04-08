str1 = input("Enter the entire data string to be sent: ")
L=[]
L.append(str1[0:8])
L.append(str1[8:16])
L.append(str1[16:24])
L.append(str1[24:32])

#Sender Side
chk = 0
sum1 = ''
while(chk<4):
    if(chk==0):
        chk+=2
        sum1 = str(bin(int(L[0],2)+int(L[1],2)))[2:]
        if(len(sum1)>8):
            sum1 = str(bin(int(sum1[1:],2)+int(sum1[0],2)))[2:]
    else:
        sum1 = str(bin(int(sum1,2)+int(L[chk],2)))[2:]
        chk+=1
        if(len(sum1)>8):
            sum1 = str(bin(int(sum1[1:],2)+int(sum1[0],2)))[2:]
    print(sum1)

temp = ''
for i in range(8-len(sum1)):
    temp = sum1
    sum1 = '0'
    sum1 = sum1+temp

checksum = ''
for i in range(len(sum1)):
    if(sum1[i]=='0'):
        checksum += "1"
    else:
        checksum += "0"

#Receiver Side
str1 = input("Enter the received data string: ")
L=[]
L.append(str1[0:8])
L.append(str1[8:16])
L.append(str1[16:24])
L.append(str1[24:32])

chk = 0
sum1 = ''
while(chk<4):
    if(chk==0):
        chk+=2
        sum1 = str(bin(int(L[0],2)+int(L[1],2)))[2:]
        if(len(sum1)>8):
            sum1 = str(bin(int(sum1[1:],2)+int(sum1[0],2)))[2:]
    else:
        sum1 = str(bin(int(sum1,2)+int(L[chk],2)))[2:]
        chk+=1
        if(len(sum1)>8):
            sum1 = str(bin(int(sum1[1:],2)+int(sum1[0],2)))[2:]
    print(sum1)

temp = ''
for i in range(8-len(sum1)):
    temp = sum1
    sum1 = '0'
    sum1 = sum1+temp
print(sum1,checksum)
res = str(bin(int(sum1,2)+int(checksum,2)))[2:]
print(res)
success=True
for i in res:
    if i!="1":
        print("Transmission Failed, Error Detected")
        success=False
        break
if(success):
     print("No errors Detected")
