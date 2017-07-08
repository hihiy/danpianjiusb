import serial
import binascii
import csv
import numpy as np
import matplotlib.pyplot as plt
import time



write_name = 'test.csv'
ser = serial.Serial('com3',4500000)
collecttime = 20000
n_channel = 10
two = []
MAXRANGE = 65535
AMPL = 6


bin_ori = ''
writecache=[]
drawcache = []
for i in range(n_channel):
    writecache.append([])
    drawcache.append([])
ccc=[]
nnn=[]
for i in range(collecttime):
    n = ser.inWaiting()
    # if n !=0:
    #     ccc.append(i)
    #     nnn.append(n)
    ori = ser.read(n)
    bin_ori += str(binascii.b2a_hex(ori))[2:-1]
    # print(ori)

# time.sleep(1)
# n = ser.inWaiting()
# print(n)
# ori = ser.read(n)
# bin_ori += str(binascii.b2a_hex(ori))[2:-1]
# print(ccc)
# print(nnn)
# print(len(bin_ori))
ffff_list = bin_ori.split('fffffffe')
# print(ffff_list)


wrong_no =0
for i in range(1,len(ffff_list)):
    if len(ffff_list[i]) != 4 * n_channel:
        print(i)
        print('receive wrong')
        wrong_no +=1
        print(ffff_list[i])
        continue

    for j in range(n_channel):
        temp = int(ffff_list[i][4*j:4*(j+1)],16)
        drawcache[j].append((temp - MAXRANGE / 2) / (MAXRANGE / 2) * AMPL)
        writecache[j].append(str(temp))

print(wrong_no)
print(wrong_no/len(ffff_list))
fig = plt.figure()

if n_channel == 10 and len(two) == 0:
    for i in range(n_channel):
        ax = fig.add_subplot('2','5',i+1)
        ax.set_title("channel " + str(i))
        nlen = len(drawcache[i])
        x = np.arange(nlen)
        pltdraw = np.array(drawcache[i])
        ax.plot(x,pltdraw,'-')

if n_channel != 10 and len(two) == 0:
    for i in range(n_channel):
        ax = fig.add_subplot('4', '4', i + 1)
        ax.set_title("channel " + str(i))
        nlen = len(drawcache[i])
        x = np.arange(nlen)
        pltdraw = np.array(drawcache[i])
        ax.plot(x, pltdraw, '-')
#plt.tight_layout()

if len(two) == 2:
    ax = fig.add_subplot('2','1',1)
    ax.set_title("channel " + str(two[0]))
    nlen = len(drawcache[two[0]])
    x = np.arange(nlen)
    pltdraw = np.array(drawcache[two[0]])
    ax.plot(x,pltdraw,'-')

    ax = fig.add_subplot('2','1',2)
    ax.set_title("channel " + str(two[1]))
    nlen = len(drawcache[two[1]])
    x = np.arange(nlen)
    pltdraw = np.array(drawcache[two[1]])
    ax.plot(x,pltdraw,'-')






with open(write_name, 'w', newline='') as csvfile:
    file_writer = csv.writer(csvfile, dialect='excel')
    for i in range(len(writecache[0])):
        temp = []
        for j in range(n_channel):
            temp.append(writecache[j][i])
        file_writer.writerow(temp)


plt.show()
