def addToData(information):
    data = open('data.txt', 'a')
    data.write(information)
    data.close()

def SearchData(ser):
    data = open('data.txt', 'r')
    list = data.readlines()
    res = []
    for i in list:
        if ser in i:
            res.append(i)
            print (i)

def takeData(str):
    dataList = []
    f = open('data.txt', 'r')
    fullList = f.readlines()
    for i in fullList:
        if str in i:
            dataList.append(i)
    print(*dataList)
    return dataList,fullList

def deleteData(full_List,data_List,num):
    R = open('data.txt', 'w')
    for i in full_List:
        if data_List[num-1] != i:
            R.write(i)
        else:
            R.write ("")
            print("готово")

def deleting(full_List,data_List,num):
    R = open('data.txt', 'w')
    for i in full_List:
        if data_List[num-1] != i:
            R.write(i)
        else:
            R.write ("")
            print("готово \n")

def changeData(full_List,data_List,num,new):
    R = open('data.txt', 'w')
    for i in full_List:
        if data_List[num-1] != i:
            R.write(i)
        else:
            R.write (new)
            print("готово")