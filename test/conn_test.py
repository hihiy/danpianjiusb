import serial
import binascii
import csv
import numpy as np
import matplotlib.pyplot as plt

write_name = 'test.csv'
ser = serial.Serial('com6',4000000)
collecttime = 17000
n_channel = 10



bin_ori = ''
writecache=[]
drawcache = []
for i in range(n_channel):
    writecache.append([])
    drawcache.append([])

for i in range(collecttime):
    n = ser.inWaiting()
    ori = ser.read(n)
    bin_ori += str(binascii.b2a_hex(ori))[2:-1]
    # print(ori)

lenthbin=len(bin_ori)
iii=0

for i in range(0,len(bin_ori),4*n_channel):
    for j in range(n_channel):
        temp = int(bin_ori[i+4*j:i+4*(j+1)],16)
        drawcache[j].append(temp)
        writecache[j].append(str(temp))
    iii = i
# bin_ori = bin_ori[len(bin_ori)//4*4:]


# with open("test.csv", "r", encoding="utf-8") as csvfile:
#     # 读取csv文件，返回的是迭代类型
#     read = csv.reader(csvfile)
#     for i in read:
#         drawcache.append(int(i[0]))
# print(drawcache)
print(lenthbin)
print(iii)

fig = plt.figure()
for i in range(n_channel):
    ax = fig.add_subplot('2','5',i+1)
    ax.set_title("channel " + str(i))
    nlen = len(drawcache[i])
    x = np.arange(nlen)
    pltdraw = np.array(drawcache[i])
    ax.plot(x,pltdraw,'-')
plt.tight_layout()
'''
ax = fig.add_subplot('2','1',1)
ax.set_title("channel " + str(7))
nlen = len(drawcache[6])
x = np.arange(nlen)
pltdraw = np.array(drawcache[6])
ax.plot(x,pltdraw,'-')

ax = fig.add_subplot('2','1',2)
ax.set_title("channel " + str(8))
nlen = len(drawcache[7])
x = np.arange(nlen)
pltdraw = np.array(drawcache[7])
ax.plot(x,pltdraw,'o')
'''





with open(write_name, 'w', newline='') as csvfile:
    file_writer = csv.writer(csvfile, dialect='excel')
    for i in range(len(writecache[0])):
        temp = []
        for j in range(n_channel):
            temp.append(writecache[j][i])
        file_writer.writerow(temp)


plt.show()
