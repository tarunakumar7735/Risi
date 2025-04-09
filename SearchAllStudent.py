import oracledb as k
def viewallstudent():
    try:
        con=k.connect("system/773733@localhost/orcl")
        cur=con.cursor()
        sa="select * from %s" %input("enter table name for view:")
        cur.execute(sa)
        print("*"*50)
        for val in cur.description:
            print("\t{}".format(val[0]),end="\t")
        print()
        print("*"*50)
        x=cur.fetchall()
        for record in x:
            for a in record:
                print("\t{}".format(a),end="\t")
            print()
        print("*"*50)
    except k.DatabaseError as a:
        print("problem in oracle DB:",a)


