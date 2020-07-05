import os
import traceback
from configobj import ConfigObj
import sys
from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QMainWindow, QApplication, QTabWidget, QMessageBox, QDialog,  QFileDialog
from PyQt5.QtCore import *
from db import db, Config, Historys
import mf,settings
from PyQt5.QtCore import *
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(str)

class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    @pyqtSlot()
    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done

class QDialogClass(QDialog, settings.Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.save_settings)
        self.pushButton_path.clicked.connect(self.btn_open_folder)
    def save_settings(self):
        print('save_settings')
    def btn_open_folder(self):
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.lineEdit_chromepath.setText(file)

class MainWindow(QMainWindow, mf.Ui_Form):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)

        self.pushButton_start.clicked.connect(self.btn_start)
        self.pushButton_stop.clicked.connect(self.btn_stop)
        self.pushButton_config.clicked.connect(self.btn_settings)
        #
        self.threadpool = QThreadPool()
        self.stop_spam_thread = False

        config = ConfigObj('config.ini')
        path = config.get('path_portable_chrome')
        self.exec_path_chrome = os.path.join(path, 'App/Chrome-bin/Chrome.exe')
        self.profile_path = os.path.join(path, 'Data/profile/')

    def update_ui(self):
        pass

    def btn_settings(self):
        dialog = QDialogClass()
        dialog.exec_()


    def btn_start(self):
        print('Start')
        worker = Worker(self.insat_monitor,
                        kwargs={ 'data': 'test' })
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.loging_thread)
        # Execute
        self.threadpool.start(worker)


    def btn_stop(self):
        print('Stop')
        self.stop_spam_thread = True


    def print_output(self, s):
        print(s)

    def thread_complete(self):
        self.log.append('Stop')
        self.update_ui()

    def loging_thread(self, s):
        print(f'loging_thread: {s}')
        self.log.append(s)
        self.update_ui()

    def insat_monitor(self,progress_callback, kwargs):
        try:
            ch_options = Options()  # Chrome Options
            ch_options.add_argument(f"user-data-dir={self.profile_path}")  # Extract this path from "chrome://version/"

            ch_options.binary_location = self.exec_path_chrome
            driver = webdriver.Chrome(options=ch_options)  # Chrome_Options is deprecated. So we use options instead.
            driver.get("https://www.instagram.com/accounts/activity/?followRequests")
            progress_callback.emit('starting browser')

            while not self.stop_spam_thread:
                button_confirm = WebDriverWait(driver, 5).until(
                    lambda driver: driver.find_elements_by_xpath('.//button[contains(text(),"Confirm")]'))

                progress_callback.emit(f'find {len(button_confirm)} button confirm!')
                sleep(10)
                driver.refresh()


            progress_callback.emit('stop')
            driver.quit()


        except:
            with open('log', 'w+') as log_file:
                traceback.print_exc(file=log_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    db.connect(reuse_if_open=True) # иначе ошибка peewee.OperationalError: Connection already opened.
    db.create_tables([Config,Historys])
    main_window = MainWindow()
    main_window.show()
    try:
        app.exec_()
    except:
        with open('log', 'w+') as log_file:
            traceback.print_exc(file=log_file)
