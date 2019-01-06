import cx_Oracle
import time


def initOrclDb():
    print('Connecting Oracle Database')
    con =cx_Oracle.connect('pythonhol/welcome@127.0.0.1/orcl')
    ## Using DRCP -- Database Resident Connection Pooling
    ##con = cx_Oracle.connect('pythonhol','welcome','127.0.0.1:/orcl:POOLED',cclass="HOL",purity=cx_Oracle.ATTR_PURITY_SELF)
    # ver = con.version.split(".")
    # print(ver)
    # for v in ver:
    #     print(v)
    cur=con.cursor()
    cur.execute('select * from hr.departments order by department_id')

    # for result in cur:
    #     print(result)

    # row=cur.fetchone()
    # print(row)
    # row=cur.fetchone()
    # print(row)

    res=cur.fetchmany(numRows=3)
    print(res)
    tot = 0
    for idx in range(len(res)):
        print(res[idx][3])
        tot += res[idx][3]

    ##print(sum(res[x][3]) for x in range(len(res)))
    print("Total is "+str(tot))
    res=cur.fetchall()

    for r in res:
        print(r)


    #### Query Arraysize
    start = time.time()
    cur.arraysize=2000
    cur.execute('select * from bigtab')
    res=cur.fetchall()
    elapsed=(time.time()-start)
    print(str(elapsed)+" seconds")

    ### Using Bind variables
    cur.prepare("select * from hr.departments where department_id = :id")
    cur.execute(None,{'id':210})
    res = cur.fetchall()
    print(res)


    rows =[(1, "First"),
           (2, "Second"),
           (3, "Third"),
           (4, "Fourth"),
           (5, "Fifth"),
           (6, "Sixth"),
           (7, "Seventh")]

    cur.bindarraysize=7
    cur.setinputsizes(int,20)
    cur.executemany("insert into mytab(id,data) values(:1,:2)",rows)
    #con.commit() ## Commit will create Transaction
    cur2=con.cursor()
    cur2.execute("select * from mytab")
    res=cur2.fetchall()
    print(res)


    ## Calling PL SQL Function
    res = cur.callfunc('myfunc', cx_Oracle.NUMBER, ('abc', 2))
    print("Function Output "+str(res))


    # Calling PL SQl Proedure
    myvar = cur.var(cx_Oracle.NUMBER)
    cur.callproc('myproc',(123,myvar))
    print("Procedure Value "+str(myvar.getvalue()))


    # Continuous Query Notification



    cur.close()
    cur2.close()

    con.close()


def DCNCallback(message):
    print("Notification:")
    for tab in message.tables:
        print("Table:"+tab.name)
        for row in tab.rows:
            if row.opertion & cx_Oracle.OPCODE_INSERT:
                print("Insert of rowid:"+row.rowid)
            if row.opertion & cx_Oracle.OPCODE_DELETE:
                print("Delete of rowid:"+row.rowid)

def myDCNCallback(message):
    print("Notification:")
    for query in message.queries:
        for tab in query.tables:
            print("Table:"+tab.name)
            for row in tab.rows:
                print("--> --> Table Rows:")
                for row in tab.rows:
                    print("--> --> --> Row RowId:", row.rowid)
                    print("--> --> --> Row Operation:", row.operation)
                    if(row.operation == cx_Oracle.OPCODE_INSERT):
                            print("Data Inserted")
                    print("-" * 60)

            print("=" * 60)

if __name__ == '__main__':
    initOrclDb()
    # con = cx_Oracle.connect('pythonhol/welcome@127.0.0.1/orcl', events=True)
    # # subscriptionInsDel = con.subscribe(callback=DCNCallback,
    # #                                    operations=cx_Oracle.OPCODE_INSERT | cx_Oracle.OPCODE_DELETE,
    # #                                    rowids=True) rowid deprecated
    # subscriptionInsDel = con.subscribe(callback=myDCNCallback,timeout = 1800,
    #                                     qos=cx_Oracle.SUBSCR_QOS_QUERY | cx_Oracle.SUBSCR_QOS_ROWIDS)
    # subscriptionInsDel.registerquery('select * from mytab')
    # input("Hit Enter to conclude this Demo\n")

