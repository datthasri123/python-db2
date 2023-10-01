import decimal
import threading

import ibm_db
import random
import multiprocessing as mp

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

account = '789171908858486'


def random_account_amt(p_acc):
    # p_amount = random.randint(15548953, 95548953)/100
    p_amount = '{}'.format(decimal.Decimal(random.randrange(15548953, 95548953)) / 100)
    return p_amount, p_acc


def sql_operation(acc_num, connection_string, count):

    conn = ibm_db.connect(connection_string, "", "")
    commit_count = 0

    if conn:
        ibm_db.autocommit(conn, ibm_db.SQL_AUTOCOMMIT_OFF)

        while count > 0:
            sql = "UPDATE BALANCES SET AMOUNT = ? WHERE AC_ID = ?;"
            stmt = ibm_db.prepare(conn, sql)
            count -= 1

            bind_parms = random_account_amt(acc_num)
            # print(threading.current_thread().native_id.__str__() + ' --> bind_parms -> ' + bind_parms.__str__())

            try:
                ibm_db.execute(stmt, bind_parms)
                commit_count += 1
                if commit_count > 2:
                    ibm_db.commit(conn)
                    # print(threading.current_thread().native_id.__str__() + ' --> bind_parms -> ' + bind_parms.__str__() + ' -- Updated')
                    commit_count = 0
                else:
                    pass
            except:
                errorCode = ibm_db.stmt_error()
                print('issue with sql - ', ibm_db.stmt_errormsg(), " SQLSTATE: " + errorCode)

    ibm_db.commit(conn)
    ibm_db.close(conn)
    print(threading.current_thread().native_id.__str__() + "connection closed")


if __name__ == '__main__':
    mp.Process(name='T1', target=sql_operation, args=(account, connString, 100)).start()
    mp.Process(name='T2', target=sql_operation, args=(account, connString, 100)).start()
    # mp.Process(name='T3', target=sql_operation, args=(account, connString, 100)).start()
    # mp.Process(name='T4', target=sql_operation, args=(account, connString, 100)).start()
    # mp.Process(name='T5', target=sql_operation, args=(account, connString, 100)).start()
    # mp.Process(name='T6', target=sql_operation, args=(account, connString, 100)).start()
    # mp.Process(name='T7', target=sql_operation, args=(account, connString, 100)).start()
    # mp.Process(name='T8', target=sql_operation, args=(account, connString, 100)).start()
