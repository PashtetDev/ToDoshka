from PySide6 import QtWidgets, QtSql


class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('backlog_db.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database",
                                           "Click Cancel to exit", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS backlog (ID В integer primary key AUTOINCREMENT, Title VARCHAR(30), "
                   "Description VARCHAR(100), Deadline VARCHAR(20), Status VARCHAR(20))")
        return True

    def execute_query_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()

    def add_new_task_query(self, title, description, deadline, status):
        sql_query = "INSERT INTO backlog (Title, Description, Deadline, Status) VALUES (?, ?, ?, ?)"
        self.execute_query_params(sql_query, [title, description, deadline, status])

    def update_task_query(self, title, description, deadline, status, id):
        sql_query = "UPDATE backlog SET Title=?, Description=?, Deadline=?, Status=? WHERE ID=?"
        self.execute_query_params(sql_query, [title, description, deadline, status, id])

    def delete_task_query(self, id):
        sql_query = "DELETE FROM backlog WHERE ID=?"
        self.execute_query_params(sql_query, [id])

