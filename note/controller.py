import menu
import functions

def menuchoice():
    while True:
        menuChoice = menu.choice()
        if menuChoice==1:
            info = menu.writeRequest()
            functions.addToData(info)
        elif menuChoice==2:
            searchStr = menu.searching()
            functions.SearchData(searchStr)
        elif menuChoice==3:
            deleteStr = menu.searching()
            dataList,fullList = functions.takeData(deleteStr)
            choiceDNum = menu.choseNum()
            functions.deleteData(fullList,dataList,choiceDNum)
        elif menuChoice==4:
            redactStr = menu.searching()
            dataList,fullList = functions.takeData(redactStr)
            choiceDNum = menu.choseNum()
            newStr = menu.writeRequest()
            functions.changeData(fullList,dataList,choiceDNum,newStr)
        else:
            break

if __name__ == "__main__":
    menuchoice()