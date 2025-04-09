import oracledb as orc
def studentsearch():
    try:
        con=orc.connect("system/773733@localhost/orcl")
        cur=con.cursor()
        sno = int(input("enter student number for view:"))
        sq="select * from student where sno=%d" %sno
        cur.execute(sq)
        print("*"*50)
        while("aa"):
            record=cur.fetchone()
            if (record!=None):
                for val in record:
                    print("\t{}".format(val),end="\t")
                print()
            else:
                print("*"*50)
                break
    except orc.DatabaseError as k:
        print("problem in oracle DB:",k)


