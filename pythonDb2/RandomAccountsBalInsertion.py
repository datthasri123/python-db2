import ibm_db
import random
import string


def random_account_amt():
    p_account = ''.join(random.choice(string.digits) for i in range(15))
    p_amount = random.uniform(300000.52, 917500.5)
    return p_account, p_amount


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
sql = "INSERT INTO BALANCES VALUES(?, ?)"
stmt = ibm_db.prepare(conn, sql)

for i in range(1000):
    ibm_db.execute(stmt, random_account_amt())

ibm_db.close(conn)
print("connection closed")
