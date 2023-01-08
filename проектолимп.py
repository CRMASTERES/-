import sys
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, \
    QLabel, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton, \
    QButtonGroup
import webbrowser


# import cgitb
# cgitb.enable(format='text')


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('glmen.ui', self)

        self.label.setWordWrap(True)  # +++

        self.otvleg = ["Катлог", "Файл"]
        self.otvlek = ["Католог"]

        self.pushButton.clicked.connect(self.exit)
        self.pushButton_4.clicked.connect(self.legk)
        self.pushButton_3.clicked.connect(self.sred)
        self.pushButton_2.clicked.connect(self.sloz)

        self.n = 0
        self.stas = True
        self.ans1 = QRadioButton('ans1', self)
        self.ans1.resize(500, 30)
        self.ans1.move(250, 170)
        self.ans1.setVisible(False)

        self.ans2 = QRadioButton('ans2', self)
        self.ans2.resize(500, 30)
        self.ans2.move(250, 220)
        self.ans2.setVisible(False)

        self.ans3 = QRadioButton('ans3', self)
        self.ans3.resize(500, 30)
        self.ans3.move(250, 270)
        self.ans3.setVisible(False)

        self.ans4 = QRadioButton('ans4', self)
        self.ans4.resize(500, 30)
        self.ans4.move(250, 320)
        self.ans4.setVisible(False)

        self.ssil = QPushButton('Исходный код', self)
        self.ssil.resize(150,30)
        self.ssil.move(615,550)


        self.btn_group = QButtonGroup(self)
        self.btn_group.addButton(self.ans1)
        self.btn_group.addButton(self.ans2)
        self.btn_group.addButton(self.ans3)
        self.btn_group.addButton(self.ans4)

        self.s = 0
        self.count = 0
        self.voprleg = ["Как называется группа файлов, которая хранится "
                       "отдельной группой и имеет собственное имя ?","Как называют файлы содержащие рисунки, тексты?","Сколько байтов в одном в одном килобайте?",
                        "Комплект расположенных в определённом порядке клавиш для управления каким-либо устройством или для ввода данных это","Мозг компьютера - это...?"]
        self.voprsr =["Что такое HTTP?","Какой сервис Интернета сокращённо обозначается как WWW?","Что такое фишинг?",
                      "Что рекомендуется делать с любым скачанным из Интернета файлом?","Какая величина характеризует скорость передачи информации?"]
        self.otvleg = ["Каталог","Графические","1024","Клавиатура","Процессор"]
        self.otvsr = ["Протокол передачи гипертекстовых файлов","Всемирная паутина","Вид мошенничества с целью получения логина и пароля пользователя",
                      "Проверять антивирусом","бит/с"]

        self.varleg = ['Каталог',"Текстовые","1048","Монитор","Видеокарта"]
        self.varleg2 = ['Компьютер',"Документы","1024","Наушники","Процессор"]
        self.varleg3 = ['Жесткий диск',"Графические","1064","Коврик для мышки","Блок питания"]
        self.varleg4 = ['Системный блок',"Папки","1056","Клавиатура","Системный блок"]
        self.varsr = ["Адрес документа в Интернете","Всемирная паутина","Вид заработка в Интернете","Проверять антивирусом","км/c"]
        self.varsr2 = ["Протокол передачи гипертекстовых файлов","Файловые архивы","Передача данных по незащищённому каналу","Архивировать","Гбайт/ч"]
        self.varsr3 = ["Необязательная часть при вводе адреса сайта","Электронная почта","Вид мошенничества с целью получения логина и пароля пользователя","Передавать другим людям","км/ч"]
        self.varsr4 = ["Протокол для передачи данных сайту","Социальные сети","База данных сайта","Переименовывать","бит/с"]
        self.voprsl = ["Что такое язык HTML?","Что такое JavaScript?"]
        self.otvsl = ["Язык разметки гипертекста","Язык веб-программирования"]
        self.varsl = ["Язык, созданный для создания стилей элементов интерфейса ","Язык веб-программирования"]
        self.varsl2 = ["Язык разметки гипертекста","Протокол передачи гипертекста"]
        self.varsl3 = ["Язык программирования для создания скриптов, выполняемых в браузере","Веб-браузер"]
        self.varsl4 = ["Язык программирования для создания сайта","Антивирусная система"]

        self.btn_group.buttonClicked.connect(self.radio)
        self.ssil.clicked.connect(lambda: webbrowser.open('http://www.google.com'))

    def legk(self):
        if self.stas == True:
            self.pushButton_3.deleteLater()
            self.pushButton_2.deleteLater()
            self.pushButton_4.move(250,400)
            self.pushButton_4.setText("Подтвердить ответ")
            self.pushButton.deleteLater()
            self.ssil.setVisible(False)
            self.stas = False


        if self.n in self.otvleg:
            self.count += 1

        if self.s == len(self.otvleg):
            self.ans1.deleteLater()
            self.ans2.deleteLater()
            self.ans3.deleteLater()
            self.ans4.deleteLater()
            self.pushButton_4.setText("OK")
            self.label.setText(f"Ваш результат {self.count} из 5")
        else:
            self.label.setText(self.voprleg[self.s])
            self.ans1.setText(self.varleg[self.s])
            self.ans2.setText(self.varleg2[self.s])
            self.ans3.setText(self.varleg3[self.s])
            self.ans4.setText(self.varleg4[self.s])
            self.ans1.setVisible(True)
            self.ans2.setVisible(True)
            self.ans3.setVisible(True)
            self.ans4.setVisible(True)

            self.s += 1
            self.n = " "

    def sred(self):
        if self.stas == True:
            self.pushButton_4.deleteLater()
            self.pushButton_2.deleteLater()
            self.pushButton_3.move(250,400)
            self.pushButton_3.setText("Подтвердить ответ")
            self.pushButton.deleteLater()
            self.ssil.setVisible(False)
            self.stas = False

        if self.n in self.otvsr:
            self.count += 1

        if self.s == len(self.otvsr):
            self.ans1.deleteLater()
            self.ans2.deleteLater()
            self.ans3.deleteLater()
            self.ans4.deleteLater()
            self.pushButton_3.setText("OK")
            self.label.setText(f"Ваш результат {self.count} из 5")
        else:
            self.label.setText(self.voprsr[self.s])
            self.ans1.setText(self.varsr[self.s])
            self.ans2.setText(self.varsr2[self.s])
            self.ans3.setText(self.varsr3[self.s])
            self.ans4.setText(self.varsr4[self.s])
            self.ans1.setVisible(True)
            self.ans2.setVisible(True)
            self.ans3.setVisible(True)
            self.ans4.setVisible(True)

            self.s += 1
            self.n = " "

    def sloz(self):
        if self.stas == True:
            self.pushButton_4.deleteLater()
            self.pushButton_3.deleteLater()
            self.pushButton_2.move(250,400)
            self.pushButton_2.setText("Подтвердить ответ")
            self.pushButton.deleteLater()
            self.ssil.setVisible(False)
            self.stas = False

        if self.n in self.otvsl:
            self.count += 1

        if self.s == len(self.otvsl):
            self.ans1.deleteLater()
            self.ans2.deleteLater()
            self.ans3.deleteLater()
            self.ans4.deleteLater()
            self.pushButton_2.setText("OK")
            self.label.setText(f"Ваш результат {self.count} из 5")
        else:
            self.label.setText(self.voprsl[self.s])
            self.ans1.setText(self.varsl[self.s])
            self.ans2.setText(self.varsl2[self.s])
            self.ans3.setText(self.varsl3[self.s])
            self.ans4.setText(self.varsl4[self.s])
            self.ans1.setVisible(True)
            self.ans2.setVisible(True)
            self.ans3.setVisible(True)
            self.ans4.setVisible(True)

            self.s += 1
            self.n = " "

    def radio(self, button):
        self.n = button.text()

    def exit(self):
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())