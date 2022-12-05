import ibm_db

database = "SAMPLE"
hostName = "0.0.0.0"
userID = "db2inst1"
passWord = "password"
portNum = "50000"

connString = ''
connString = "DRIVER={IBM DB2 ODBC DRIVER}"
connString += ";ATTACH=FALSE"             # Attach To A Server; Not A Database
connString += ";DATABASE=" + database    # Ignored When Connecting To A Server
connString += ";HOSTNAME=" + hostName    # Required To Connect To A Server
connString += ";PORT=" + portNum         # Required To Connect To A Server
connString += ";PROTOCOL=TCPIP"          # Required To Connect To A Server
connString += ";UID=" + userID
connString += ";PWD=" + passWord

conn = ibm_db.connect(connString, "", "")

account = '789171908858486'

if conn:
    ibm_db.autocommit(ibm_db.SQL_AUTOCOMMIT_OFF)
    sql = "UPDATE BALANCES SET AMOUNT = (AMOUNT * 0.1) + AMOUNT WHERE AC_ID = ?;"
    # stmt = ibm_db.exec_immediate(conn, sql)
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt, 1, account)

    try:
        ibm_db.execute(stmt)
        ibm_db.commit(conn)
    except:
        print(ibm_db.stmt_errormsg())
        print('connect not successful')


ibm_db.close(conn)
print("connection closed")
