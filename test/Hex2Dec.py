import csv,sys,getopt
import numpy as np
import matplotlib.pyplot as plt

try:
    options,args = getopt.getopt(sys.argv[1:],"hi:o:",["help","in=","out="])
except getopt.GetoptError:
    sys.exit()

def usage():
    print(u"""
    -h / --help :使用帮助
      -i / --in :输入文件
    -o / --out :输出文件
    """)



def trans(read_name,write_name):
    n_channel = 10
    file = open(read_name)
    file_text = file.read()
    ffff_list_split = file_text.split(' FF FF FF FE ')

    print(ffff_list_split)
    writecache = []
    drawcache = []
    for i in range(n_channel):
        writecache.append([])
        drawcache.append([])

    wrong_no = 0

    for i in range(1, len(ffff_list_split)):
        ffff_list = ffff_list_split[i].split(' ')

        if len(ffff_list) != 2 * n_channel:
            print(i)
            print('receive wrong')
            wrong_no += 1
            print(ffff_list)
            continue
        # print(ffff_list)


        for j in range(n_channel):
            temp = int(ffff_list[2*j]+ffff_list[2*j+1], 16)
            # print(temp)
            drawcache[j].append(temp)
            writecache[j].append(str(temp))
        # print(drawcache)
    print(wrong_no)
    print(wrong_no / len(ffff_list_split))
    fig = plt.figure()

    for i in range(n_channel):
        ax = fig.add_subplot('2', '5', i + 1)
        ax.set_title("channel " + str(i))
        nlen = len(drawcache[i])
        x = np.arange(nlen)
        pltdraw = np.array(drawcache[i])
        ax.plot(x, pltdraw, '-')
    plt.show()


    with open(write_name, 'w', newline='') as csvfile:
        file_writer = csv.writer(csvfile, dialect='excel')
        for i in range(len(writecache[0])):
            temp = []
            for j in range(n_channel):
                temp.append(writecache[j][i])
            file_writer.writerow(temp)



# def main():
#     trans('matlab.txt', 'matlab.csv')
#
#
# if __name__ == '__main__':
#     main()

read_n = 'ttt.txt'
write_n = 'ttt.csv'
for name,value in options:
    if not name:
        usage()
    if  name in ("-h","--help"):
        usage()
    if name in ("-i","--in"):
        read_n = value
    if name in ("-o","--out"):
        write_n = value

trans(read_n,write_n)

