import oracledb as orc
def updatestudent():
        while(True):
            try:
                con=orc.connect("system/773733@localhost/orcl")
                cur=con.cursor()
                sno=int(input("enter sno to update:"))
                sname=input("enter student name for update:")
                marks=float(input("enter student marks for update:"))
                uq="update student set sname='%s',marks=%f where sno=%d" %(sname,marks,sno)
                cur.execute(uq)
                con.commit()
                if (cur.rowcount>0):
                    print("\t{} record updated".format(cur.rowcount))
                else:
                    print("record does not exist")
                n=input("do u want to update another record (yes or no):")
                if (n.lower()=="no"):
                    break
            except orc.DatabaseError as k:
                print("problem in oracle DB:",k)
            except ValueError:
                print("dont enter alnums , strs and symbols for sno or marks")




