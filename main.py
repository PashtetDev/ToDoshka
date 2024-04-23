import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtSql import QSqlTableModel
from PySide6.QtCore import QDate
from main_ui import Ui_MainWindow
from task_ui import Ui_dialog
from connection import Data


class TaskTracker(QMainWindow):
    def __init__(self):
        super(TaskTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data()
        self.view_data()

        self.ui.newTaskBtn.clicked.connect(self.open_task_editor)
        self.ui.editBtn.clicked.connect(self.open_task_editor)
        self.ui.deleteBtn.clicked.connect(self.delete_current_task)

    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('backlog')
        self.model.select()
        self.ui.tableView.setModel(self.model)

    def open_task_editor(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_dialog()
        self.ui_window.setupUi(self.new_window)
        self.ui_window.deadlineEdit.setDate(QDate.currentDate())

        sender = self.sender()
        if sender.text() == "New Task":
            self.ui_window.completeBtn.clicked.connect(self.add_new_task)
            self.new_window.show()
        elif len(self.ui.tableView.selectedIndexes()) > 0:
            self.ui_window.completeBtn.clicked.connect(self.edit_current_task)
            index = self.ui.tableView.selectedIndexes()[0]
            title = self.ui.tableView.model().data(self.ui.tableView.model().index(index.row(), 1))
            description = self.ui.tableView.model().data(self.ui.tableView.model().index(index.row(), 2))
            deadline_str = self.ui.tableView.model().data(self.ui.tableView.model().index(index.row(), 3))
            deadline = QDate.fromString(deadline_str, "dd.MM.yyyy")
            status = self.ui.tableView.model().data(self.ui.tableView.model().index(index.row(), 4))

            self.ui_window.titleEdit.setText(title)
            self.ui_window.descriptionEdit.setPlainText(description)
            self.ui_window.deadlineEdit.setDate(deadline)
            self.ui_window.statusEdit.setCurrentText(status)
            self.new_window.show()
        else:
            QtWidgets.QMessageBox.warning(None, "Warning!",
                                           "No task has been selected", QtWidgets.QMessageBox.Cancel)

    def add_new_task(self):
        title = self.ui_window.titleEdit.text()
        description = self.ui_window.descriptionEdit.toPlainText()
        deadline = self.ui_window.deadlineEdit.date().toString("dd.MM.yyyy")
        status = self.ui_window.statusEdit.currentText()

        if len(title) == 0 or len(description) == 0 or len(status) == 0:
            QtWidgets.QMessageBox.warning(None, "Warning!",
                                           "Please fill in all the fields!", QtWidgets.QMessageBox.Cancel)
        else:
            self.conn.add_new_task_query(title, description, deadline, status)
            self.view_data()
            self.new_window.close()

    def edit_current_task(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().data(self.ui.tableView.model().index(index.row(), 0)))

        title = self.ui_window.titleEdit.text()
        description = self.ui_window.descriptionEdit.toPlainText()
        deadline = self.ui_window.deadlineEdit.date().toString("dd.MM.yyyy")
        status = self.ui_window.statusEdit.currentText()

        if len(title) == 0 or len(description) == 0 or len(status) == 0:
            QtWidgets.QMessageBox.warning(None, "Warning!",
                                           "Please fill in all the fields!", QtWidgets.QMessageBox.Cancel)
        else:
            self.conn.update_task_query(title, description, deadline, status, id)
            self.view_data()
            self.new_window.close()

    def delete_current_task(self):
        if len(self.ui.tableView.selectedIndexes()) > 0:
            index = self.ui.tableView.selectedIndexes()[0]
            id = str(self.ui.tableView.model().data(self.ui.tableView.model().index(index.row(), 0)))
            self.conn.delete_task_query(id)
        else:
            QtWidgets.QMessageBox.warning(None, "Warning!",
                                          "No task has been selected", QtWidgets.QMessageBox.Cancel)

        self.view_data()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaskTracker()
    window.show()

    sys.exit(app.exec())