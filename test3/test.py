import logging
import time
import math
import os
import getpass
import psutil
import string
import random

logging.basicConfig(filename="result.log", level=logging.INFO)


class ListOfFiles:
    tc_id = 1
    name = "List of files"
    prepare = False
    CurrentUser = None

    def preparation(self):
        actualtime = int(time.time())
        if math.fmod(actualtime, 2) != 0:
            prepare = False
        else:
            prepare = True
        return prepare

    def run(self):
        CurrentUser = getpass.getuser()
        for dirpath, dirnames, filenames in os.walk(f"C:\\Users\\{CurrentUser}\\Documents"):
            # перебрать каталоги
            for dirname in dirnames:
                logging.info(f"Каталог: {os.path.join(dirpath, dirname)}")
            # перебрать файлы
            for filename in filenames:
                logging.info(f"Файл: {os.path.join(dirpath, filename)}")
        return

    def execute(self):
        if self.preparation():
            try:
                logging.info(f"Запущен тест № {self.tc_id}")
                self.run()
            except FileNotFoundError:
                logging.error("Папки/файла не существует")
            except:
                logging.error("Неожиданная ошибка")
            finally:
                logging.info("-----------------------------------------------")
        else:
            logging.info("Тест не может быть запущен, не выполнены условия")
            logging.info("-----------------------------------------------")
        return


class RandomFile:
    tc_id = 2
    name = "Random File"
    prepare = False

    def preparation(self):
        ram = psutil.virtual_memory().total
        if ram < 1048576:
            logging.info("Выполнение кейса невозможно")
            prepare = False
        else:
            prepare = True
        return prepare

    def run(self):
        content = ""
        for i in range(1048576):
            content = content + random.choice(string.ascii_letters)
        file = open("test", "w")
        logging.info("Создан файл test размером 1024 килобайт")
        file.write(content)
        logging.info("Случайное содержимое записано в файл test")
        file.close()
        return

    def clean_up(self):
        check_file = os.path.exists("test")
        if check_file:
            os.remove("test")
        return

    def execute(self):
        if self.preparation():
            try:
                logging.info(f"Запущен тест № {self.tc_id}")
                self.run()
            except IndexError:
                logging.error("Индекс находится вне диапазона")
                logging.info("-----------------------------------------------")
                return
            except MemoryError:
                logging.error("Не хватает оперативной памяти для выполнения программы")
                logging.info("-----------------------------------------------")
                return
            except:
                logging.error("Неожиданная ошибка")
                logging.info("-----------------------------------------------")
            finally:
                self.clean_up()
                logging.info("Файл test удалён")
                logging.info("-----------------------------------------------")


# рабочий вывод списка файлов и папок
a = ListOfFiles()

# рабочее создание файла test
b = RandomFile()

a.execute()
b.execute()
