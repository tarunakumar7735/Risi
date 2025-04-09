import oracledb as orc
def deletestudent():
        while(True):
            try:
                con=orc.connect("system/773733@127.0.0.1/orcl")
                cur=con.cursor()
                sno=int(input("enter student number for delete student:"))
                dq="delete from student where sno=%d" %sno
                cur.execute(dq)
                con.commit()
                if (cur.rowcount>0):
                    print("\t{} record deleted".format(cur.rowcount))
                else:
                    print("record does not exist")
                n=input("do you want to delete another record (yes or no):")
                if (n.lower()=="no"):
                    break
            except orc.DatabaseError as k:
                print("problem in oracle DB:",k)





