import oracledb as orc
def viewsinglestudent():
    try:
        con=orc.connect("system/773733@127.0.0.1/orcl")
        cur=con.cursor()
        sno=int(input("enter student number for view student details:"))
        sq="select * from student where sno=%d" %sno
        cur.execute(sq)
        print("*" * 50)
        while ("aa"):
            record = cur.fetchone()
            if (record != None):
                for val in record:
                    print("\t{}".format(val), end="\t")
                print()
            else:
                print("*" * 50)
                break
            n=input("do u want to search another record (yes or no):")
            if (n.lower()=="no"):
                break
    except orc.DatabaseError as k:
        print("problem in oracle DB:", k)

