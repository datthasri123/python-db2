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

if conn:
    sql = "SELECT FIRSTNME FROM EMPLOYEE"
    stmt = ibm_db.exec_immediate(conn, sql)
    result = ibm_db.fetch_both(stmt)

    while result:
        print('LAST NAME -> ', result[0])
        result = ibm_db.fetch_both(stmt)

    print('connect succesful')

ibm_db.close(conn)
print("connection closed")
