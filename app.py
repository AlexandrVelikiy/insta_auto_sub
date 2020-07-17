import os
import traceback
from random import randint
import sys
import logging
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QMessageBox, QDialog,  QFileDialog
from PyQt5.QtCore import *
from db import db, Config, Historys
import mf,settings
from PyQt5.QtCore import *
from time import sleep
import datetime
import peewee
from apscheduler.schedulers.qt import QtScheduler

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

REPORTS_DIRECTORY_NAME = 'reports'

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
        self.lg = logging.getLogger('insta')
        self.buttonBox.accepted.connect(self.save_settings)
        self.pushButton_path.clicked.connect(self.btn_open_folder)
        #self.dateTime_start.editingFinished.connect(self.start_stateChanged)
        #self.dateTime_stop.editingFinished.connect(self.stop_stateChanged)
        self.checkBox_sheduled.stateChanged.connect(self.shedule_change_state)
        self.load_stored_data()

        self.curr_dateTime_stop = None
        self.curr_dateTime_start = None

    def shedule_change_state(self):
        self.curr_dateTime_stop = self.dateTime_stop.dateTime().toPyDateTime()
        self.curr_dateTime_start = self.dateTime_start.dateTime().toPyDateTime()

        message = ''
        if self.curr_dateTime_start < datetime.datetime.now():
            message =  message + 'Дата старта не может быть меньше текущей даты. '

        if self.curr_dateTime_stop < datetime.datetime.now():
            message = message + 'Дата остановки не может быть меньше текущей даты. '

        if self.curr_dateTime_stop < self.curr_dateTime_start:
            message = message + 'Дата старта не может быть меньше даты остановки'

        if message:
            QMessageBox.warning(self, 'Внимание!', message, QMessageBox.Ok)
         #   if self.checkBox_sheduled.isChecked():
            if self.checkBox_sheduled.isChecked():
                self.checkBox_sheduled.setChecked(False)
            else:
                self.checkBox_sheduled.setChecked(False)
        else:
            running_time = self.curr_dateTime_stop - self.curr_dateTime_start
            self.lineEdit.setText(str(running_time))

    def start_stateChanged(self):
        self.curr_dateTime_start = self.dateTime_start.dateTime().toPyDateTime()

        if self.curr_dateTime_start < datetime.datetime.now():
            QMessageBox.warning(self, 'Внимание!', 'Дата старта не может быть меньше текущей даты',
                                QMessageBox.Ok)
            self.curr_dateTime_start = None
            return
        if self.curr_dateTime_stop:
            if self.curr_dateTime_stop > self.curr_dateTime_start:
                # определяем разницу
                running_time = self.curr_dateTime_stop - self.curr_dateTime_start
                self.lineEdit.setText(str(running_time))
            else:
                QMessageBox.warning(self,'Внимание!','Дата старта не может быть меньше даты остановки', QMessageBox.Ok)

    def stop_stateChanged(self):
        self.curr_dateTime_stop = self.dateTime_stop.dateTime().toPyDateTime()
        if self.curr_dateTime_stop < datetime.datetime.now():
            QMessageBox.warning(self, 'Внимание!', 'Дата остановки не может быть меньше текущей даты',
                                QMessageBox.Ok)
            self.curr_dateTime_stop = None
            return

        if self.curr_dateTime_start:
            if self.curr_dateTime_stop > self.curr_dateTime_start:
                # определяем разницу
                running_time = self.curr_dateTime_stop - self.curr_dateTime_start
                self.lineEdit.setText(str(running_time))
            else:
                QMessageBox.warning(self, 'Внимание!', 'Дата остановки не может быть больше даты старта', QMessageBox.Ok)

    def load_stored_data(self):
        try:
            config = Config.select().get()
            self.lineEdit_chromepath.setText(config.chrome_path)
            self.spinBox_timeout.setValue(config.timeout)
            self.spinBox_timeout_confirm.setValue(config.timeout_confirm)
            if config.sheduled:
                self.checkBox_sheduled.setChecked(config.sheduled)
            else:
                self.checkBox_sheduled.setChecked(False)
            if config.stop_data_time:
                self.dateTime_stop.setDateTime(config.stop_data_time)
            if config.start_data_time:
                self.dateTime_start.setDateTime(config.start_data_time)

        except peewee.DoesNotExist:
            # загружаем значения по умолчанию
            self.lineEdit_chromepath.setText('')
            self.spinBox_timeout.setValue(30)
            self.spinBox_timeout_confirm.setValue(5)
            self.checkBox_autostart.setChecked(False)
            self.dateTime_stop.setDateTime(datetime.datetime.now()+datetime.timedelta(days=1))

    def save_settings(self):
        try:
            chromepath = self.lineEdit_chromepath.text()
            timeout = self.spinBox_timeout.value()
            timeout_confirm = self.spinBox_timeout_confirm.value()
            sheduled = self.checkBox_sheduled.isChecked()
            stop_datetime = self.dateTime_stop.dateTime().toPyDateTime()
            start_datetime = self.dateTime_start.dateTime().toPyDateTime()

            config = Config.select().get()
            config.chrome_path =chromepath
            config.timeout = timeout
            config.timeout_confirm = timeout_confirm
            config.sheduled = sheduled
            config.start_data_time = start_datetime
            config.stop_data_time = stop_datetime
            config.save()

        except peewee.DoesNotExist:
            config = Config(chrome_path=chromepath, timeout=timeout,sheduled =sheduled,
                            start_data_time = start_datetime,stop_data_time=stop_datetime,timeout_confirm = timeout_confirm)
            config.save()


        return sheduled
        print('save_settings')

    def btn_open_folder(self):
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.lineEdit_chromepath.setText(file)

class MainWindow(QMainWindow, mf.Ui_Form):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        if not os.path.exists(REPORTS_DIRECTORY_NAME):
            os.makedirs(REPORTS_DIRECTORY_NAME)
        self.setupUi(self)
        self.setWindowTitle('Instagram auto follow confirm v.1.3')
        self.pushButton_start.clicked.connect(self.btn_start)
        self.pushButton_stop.clicked.connect(self.btn_stop)
        self.pushButton_config.clicked.connect(self.btn_settings)
        self.pushButton_pause.clicked.connect(self.btn_pause)
        finish = QAction("Quit", self)
        finish.triggered.connect(self.closeEvent)

        # таймер для вывода времени работы
        self.timer = QTimer()
        self.timer.timeout.connect(self.handleTimer)
        self.timer.setInterval(1000)

        # таймер для старта планировщика
        self.timer_start = QTimer()
        self.timer_start.timeout.connect(self.handleTimerstart)
        self.is_startet_sheduler = False

        self.lg = logging.getLogger('insta')
        self.threadpool = QThreadPool()
        self.stop_thread = False
        self.pause_thread = False
        self.is_sheduled = False # программа запустилась по расписанию

        try:
            config = Config.select().get()
            # если врямя запуска уже прошло  - устанавливаем насильно ручной режим
            if datetime.datetime.now() > config.start_data_time:
                config.sheduled = False
                config.save()
            # настраиваем внешний вид в зависимости от  config.sheduled
            if config.sheduled:
                # запуск по планировщику
                self.set_shedule_mode(config)
            else:
                # запуск в ручном режиме
                self.set_manual_mode(config)

        except peewee.DoesNotExist:
            self.log.append('Внимание! необходимо настроить путь к браузеру')
            config = Config(chrome_path='', timeout=10, auto_start=False)
            config.save()

        self.update_ui()

    def handleTimer(self):
        # Выводим таймер с момента нажатия старт или с момента запуска по расписанию
        if not self.is_sheduled:
            time = datetime.datetime.now() - self.curren_time
            self.label_timer.setText(str(time).split('.', 2)[0])

    def handleTimerstart(self):
        if datetime.datetime.now() > self.start_data_time:
            # запускаем скрипт
            if not self.is_sheduled:
                self.is_sheduled = True
                self.log.append('Запускаем по расписанию')
                self.pushButton_stop.setDisabled(False)
                self.btn_start()
                # меняем надписи
                self.label_timer_text.setText('Время работы:')
            else:
                #выводим время работы
                time = datetime.datetime.now() - self.start_data_time
                self.label_timer.setText(str(time).split('.', 2)[0])
                self.label_timer_text_2.setText('Работать осталось:')
                time = self.stop_data_time - datetime.datetime.now()
                self.label_timer_2.setText(str(time).split('.', 2)[0])
        else:
            # выводим время до старта
            time = self.start_data_time - datetime.datetime.now()
            self.label_timer.setText(str(time).split('.', 2)[0])
            self.label_timer_2.setText('0:00:00')

        if datetime.datetime.now() > self.stop_data_time:
            # останавливаем скрипт
            self.log.append('Останавливаем по расписанию')
            if self.is_sheduled:
                # останавливаем таймер
                self.timer_start.stop()
                # останавливаем процесс
                self.btn_stop()
                # сбрасываем настроку автозапуска
                self.is_sheduled = False
                config = Config.select().get()
                config.sheduled = self.is_sheduled
                config.save()
                self.set_manual_mode(config)

    def closeEvent(self, event):
        close = QMessageBox.question(self,"Выход","Хотите завершить работу программы?",
                                     QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def update_ui(self):
        history_all = Historys.select().count()
        self.label_countAll.setText(str(history_all))
        curr_datetime = datetime.datetime.now()
        td = datetime.timedelta(days=1)
        last_24 = curr_datetime-td
        history_24 = Historys.select().where(Historys.date_time >last_24 ).count()
        self.label_count24hour.setText(str(history_24))
        config = Config.select().get()
        history_last_start = Historys.select().where(Historys.date_time > config.last_start_dt).count()
        self.label_countLaststart.setText(str(history_last_start))

    def set_shedule_mode(self,config):
        # запуск по планировщику
        self.start_data_time = config.start_data_time
        self.stop_data_time = config.stop_data_time
        self.pushButton_start.setDisabled(True)
        self.pushButton_stop.setDisabled(True)
        self.pushButton_pause.setDisabled(True)
        self.label_timer_text_2.setVisible(True)
        self.label_timer_2.setVisible(True)
        self.label_timer_text.setText('До запуска осталось:')
        self.label_timer_text_2.setText('Время работы:')
        # Запускем таймер для отсчета времени до запуска
        self.timer_start.start(1000)

    def set_manual_mode(self,config):
        # запуск в ручном режиме
        self.start_data_time = config.start_data_time
        self.stop_data_time = config.stop_data_time
        self.pushButton_start.setDisabled(False)
        self.pushButton_stop.setDisabled(True)
        self.pushButton_pause.setDisabled(True)
        self.label_timer_text_2.setVisible(False)
        self.label_timer_2.setVisible(False)
        self.label_timer_text.setText('Время работы:')
        # останавливаем таймер
        self.timer_start.stop()
        self.label_timer.setText('0:00:00')

    def btn_settings(self):
        dialog = QDialogClass()
        dialog.exec_()
        # тут проверяем каждый раз установлен ли запуск по времени
        config = Config.select().get()
        # если врямя запуска уже прошло  - устанавливаем насильно ручной режим
        if datetime.datetime.now() > config.start_data_time:
            config.sheduled = False
            config.save()
        if config.sheduled:
            self.set_shedule_mode(config)
        else:
            self.set_manual_mode(config)

    def btn_pause(self):
        self.log.append('Пауза, для продолжения нажмите Старт')
        self.pause_thread = True
        self.pushButton_start.setDisabled(False)
        self.pushButton_pause.setDisabled(True)

    def btn_start(self):
        # обрабатываем паузу
        if self.pause_thread:
            self.pause_thread = False
            self.pushButton_start.setDisabled(True)
            self.pushButton_pause.setDisabled(False)
            return
        else:
            #запускам таймер если нажимаем страт вне паузы
            self.curren_time = datetime.datetime.now()
            self.timer.start()

        # загружаем настройки
        config = Config.select().get()
        chromepath = config.chrome_path
        if chromepath == '':
            QMessageBox.warning(self,'Внимание','Путь к браузеру не указан в настройках!',QMessageBox.Ok)
            return
        timeout = config.timeout
        timeout_confirm = config.timeout_confirm
        #self.stop_data_time = config.stop_data_time
        # сохраняем дату время страта
        config.last_start_dt = datetime.datetime.now()
        config.save()

        self.pushButton_start.setDisabled(True)
        if self.is_sheduled:
            self.pushButton_pause.setDisabled(True)
        else:
            self.pushButton_pause.setDisabled(False)
        self.pushButton_stop.setDisabled(False)
        self.pushButton_config.setDisabled(True)

        print('Start')
        worker = Worker(self.insat_monitor,
                        kwargs={ 'chromepath': chromepath,'timeout':timeout, 'timeout_confirm':timeout_confirm })
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.loging_thread)
        # Execute
        self.threadpool.start(worker)

    def btn_stop(self):
        self.log.append('Нажали Стоп, ждем закрытя браузера')
        self.stop_thread = True
        self.timer.stop()
        if self.is_sheduled:
            # сбрасываем настроку автозапуска
            self.is_sheduled = False
            config = Config.select().get()
            config.sheduled = self.is_sheduled
            config.save()
            self.timer_start.stop()
            self.set_manual_mode(config)

    def print_output(self, s):
        print(s)

    def thread_complete(self):
        #self.log.append('браузер закрыт')
        self.stop_thread = False
        self.pushButton_start.setDisabled(False)
        self.pushButton_stop.setDisabled(True)
        self.pushButton_pause.setDisabled(True)
        self.pushButton_config.setDisabled(False)
        self.update_ui()
        self.save_report()

    def loging_thread(self, s):
        print(f'loging_thread: {s}')
        self.log.append(s)
        self.update_ui()

    def save_report(self):
        try:
            curr_datetime = datetime.datetime.now()
            td = datetime.timedelta(days=1)
            last_24 = curr_datetime - td
            history_24 = Historys.select().where(Historys.date_time > last_24).count()

            config = Config.select().get()
            history_last_start = Historys.select().where(Historys.date_time > config.last_start_dt).count()

            file_name = f'{REPORTS_DIRECTORY_NAME}/report_{datetime.datetime.now().strftime("%H%M%S_%m%d%Y")}.txt'
            with open(file_name,'w') as file:
                file.write(f'Окончание работы: {datetime.datetime.now().strftime("%H:%M:%S %m.%d.%Y")}' +'\n')
                file.write(f'За сутки было принято: {history_24}'+ '\n')
                file.write(f'За время работы было принято: {history_last_start}' + '\n')
        except:
            self.lg.exception('save_report')

    def insat_monitor(self,progress_callback, kwargs):
        try:
            driver = None
            chromepath =  kwargs.get('chromepath')
            exec_path_chrome = os.path.join(chromepath, 'App/Chrome-bin/Chrome.exe')
            profile_path = os.path.join(chromepath, 'Data/profile/')
            timeout = int(kwargs.get('timeout'))
            timeout_confirm = int(kwargs.get('timeout_confirm'))

            ch_options = Options()  # Chrome Options
            ch_options.add_argument(f"user-data-dir={profile_path}")  # Extract this path from "chrome://version/"
            ch_options.add_argument('window-size=640x780')


            try:
                ch_options.binary_location = exec_path_chrome
                driver = webdriver.Chrome(options=ch_options)  # Chrome_Options is deprecated. So we use options instead.
            except:
                self.lg.exception('start browser' )
                progress_callback.emit('Похоже что портабле хром уже запущен, закройте его и попробуйте еще раз')
                if driver:
                    driver.quit()
                return

            driver.get("https://www.instagram.com/accounts/activity/?followRequests")
            progress_callback.emit('Открываем браузер')

            try:
                h1 = WebDriverWait(driver, 2).until(
                    lambda driver: driver.find_elements_by_xpath(('.//h1')))
                progress_callback.emit(f'Похоже вы не залогинены в Инстаграм, заголинтесь и попробуйте снова')
                return
            except:
                pass

            while not self.stop_thread:
                if not self.pause_thread:
                    try:
                        invites = WebDriverWait(driver, 30).until(
                            lambda driver: driver.find_elements_by_xpath(('.//div[@class="PUHRj  H_sJK"]')))
                    except TimeoutException:
                        dt = datetime.datetime.now().strftime("%H:%M:%S %m.%d.%Y")
                        progress_callback.emit(f'{dt}: Нет необработаных запросов, пауза {timeout} секунд.')
                        sleep(timeout)
                        try:
                            driver.refresh()
                        except:
                            progress_callback.emit(f'Похоже браузер закрыт или не отвечает, попробуйте нажать старт снова')
                        continue

                    if invites:
                        dt = datetime.datetime.now().strftime("%H:%M:%S %m.%d.%Y")
                        progress_callback.emit(f'{dt}: Есть {len(invites)} необработаных запросов!')
                        #
                        # ('.//div[@class="PUHRj  H_sJK"]//div [@class="_7WumH"]/span/text()')
                        try:
                            for invite in invites:
                                user_login = invite.find_element(By.XPATH,'.//div [@class="_7WumH"]/a').text
                                user_name = invite.find_element(By.XPATH,'.//div [@class="_7WumH"]/span').text
                                button_confirm = invite.find_element(By.XPATH,'//button[contains(text(),"Confirm")]')
                                button_confirm.click()
                                dt = datetime.datetime.now().strftime("%H:%M:%S %m.%d.%Y")
                                progress_callback.emit(f'{dt}: Подтверждаем запрос от пользователя: {user_name}.')
                                history= Historys(user_name = user_name,insta_login = user_login, date_time = datetime.datetime.now())
                                history.save()
                                sleep(randint(timeout_confirm-1,timeout_confirm+3))
                        except:
                            self.lg.exception('invite')
                            continue

                    else:
                        dt = datetime.datetime.now().strftime("%H:%M:%S %m.%d.%Y")
                        progress_callback.emit(f'{dt}: Нет необработаных запросов, пауза {timeout} секунд.')

                    sleep(timeout)
                    driver.refresh()
                else:
                    sleep(1)


            progress_callback.emit('Закрываем браузер')
            driver.quit()

        except:
            self.lg.exception('insat_monitor')


if __name__ == '__main__':
    DEBUG = True
    logger = logging.getLogger('insta')
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler('insta_log.txt')
    fh.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    if DEBUG:
        formatter = logging.Formatter('[LINE:%(lineno)d]#%(asctime)s: %(message)s')
    else:
        formatter = logging.Formatter('%(asctime)s: %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)

    app = QApplication(sys.argv)
    db.connect(reuse_if_open=True) # иначе ошибка peewee.OperationalError: Connection already opened.
    db.create_tables([Config,Historys])
    main_window = MainWindow()
    main_window.show()
    try:
        app.exec_()
    except:
        logger.exception('main')
