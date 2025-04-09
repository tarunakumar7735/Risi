from Menu import menu
from add import addstudent
from Delete import deletestudent
from Update import updatestudent
from Search import studentsearch
from SearchSingleStudent import viewsinglestudent
from SearchAllStudent import viewallstudent
while("xxy"):
    try:
        menu()
        n=int(input("enter ur choice:"))
        match(n):
            case 1:
                addstudent()
            case 2:
                deletestudent()
            case 3:
                updatestudent()
            case 4:
                studentsearch()
            case 5:
                viewsinglestudent()
            case 6:
                viewallstudent()
            case 7:
                print("thanks for using this program")
                break
            case _:
                print("ur selection program is wrong try again")
    except ValueError:
        print("don't enter alnums,strs and symbols for choice")