import sys
import random

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QPushButton, QLabel, QLCDNumber
from PyQt5.QtWidgets import QInputDialog


class MyWidget(QMainWindow):# Подклучение кнопки
    def __init__(self):
        super().__init__()
        uic.loadUi('Проект.ui', self)
        self.tic_tac_toe.clicked.connect(self.games1)
        self.nim.clicked.connect(self.games2)
        self.sapper.clicked.connect(self.games4)
        self.psewdo_nim.clicked.connect(self.games3)
        self.setWindowTitle('Главная страница')
        self.butten = QPushButton(self)
        self.butten.move(0, 0)
        self.butten.resize(300, 20)
        self.butten.setText('Не нажимай на меня')
        self.butten.clicked.connect(self.kek)

    def kek(self): #Прикол между друзьями(не обращайти внимание)
        if self.butten.text() == 'Зверюга, лучший|| Ну всё больше не нужно нажимать':
            self.close()
        else:
            self.butten.setText('Зверюга, лучший|| Ну всё больше не нужно нажимать')


    def games1(self):#Закрывается главное окно и открывается игра
        self.p = MyWin()
        self.p.show()
        self.close()

    def games2(self):#Закрывается главное окно и открывается игра
        self.l = MyWin1()
        self.l.show()
        self.close()

    def games3(self):#Закрывается главное окно и открывается игра
        self.m = MyWin2()
        self.m.show()
        self.close()

    def games4(self):#Закрывается главное окно и открывается игра
        self.w = MyWin3()
        self.w.show()
        self.close()


class MyWin(QMainWindow):#Создание интерфейса

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Крестики-Нолики')
        self.setGeometry(700, 300, 400, 400)
        self.symbol = 'X'

        self.button = QPushButton(self)
        self.button.move(0, 0)
        self.button.resize(70, 20)
        self.button.setText('Назад')
        self.button.clicked.connect(self.help)

        self.radio_button_one = QRadioButton("X", self)
        self.radio_button_one.move(155, 20)
        self.radio_button_one.setChecked(True)

        self.radio_button_two = QRadioButton("O", self)
        self.radio_button_two.move(195, 20)

        self.buttons = []#Создание кнопок(игравого поля)
        x, y = 100, 60
        for i in range(1, 10):
            interval = QPushButton(self)
            interval.resize(50, 50)
            interval.move(x, y)
            interval.clicked.connect(self.set)
            self.buttons.append(interval)
            x += 60
            if i % 3 == 0:
                x, y = 100, y + 60

        self.label = QLabel(self)
        self.label.setStyleSheet("font-size: 14px")
        self.label.resize(100, 100)
        self.label.move(150, 250)

        self.new_game = QPushButton("Новая игра", self)
        self.new_game.move(130, 350)
        self.new_game.clicked.connect(self.start_game)

    def help(self):#Функция кнопки назад
        self.close()
        self.p = MyWidget()
        self.p.show()

    def stop_game(self):#При победе, поражении или ничьи, кнопки становяться не активны
        for button in self.buttons:
            button.setDisabled(True)

    def start_game(self):#Кнопки становятся активны
        for button in self.buttons:
            button.setDisabled(False)
            button.setText('')
            self.symbol = 'X'
            self.radio_button_one.setChecked(True)
            self.label.clear()

    def set(self):#Если на поле есть Х, то ходит автамотичиски О и наоборот
        if self.sender().text():
            return
        if self.radio_button_two.isChecked():
            self.symbol = 'O'
            self.radio_button_one.setChecked(True)
        else:
            self.symbol = 'X'
            self.radio_button_two.setChecked(True)
        self.sender().setText(self.symbol)
        if (self.diagonal_win(self.symbol) or
                self.buttons[0].text() == self.symbol and self.buttons[3].text() == self.symbol and self.buttons[
                    6].text() == self.symbol or
                self.buttons[1].text() == self.symbol and self.buttons[4].text() == self.symbol and self.buttons[
                    7].text() == self.symbol or
                self.buttons[2].text() == self.symbol and self.buttons[5].text() == self.symbol and self.buttons[
                    8].text() == self.symbol or
                self.buttons[0].text() == self.symbol and self.buttons[4].text() == self.symbol and self.buttons[
                    8].text() == self.symbol or
                self.buttons[2].text() == self.symbol and self.buttons[4].text() == self.symbol and self.buttons[
                    6].text() == self.symbol):
            self.label.setText(f"Победил {self.symbol.upper()}!")
            self.stop_game()
        draw = 1
        for button in self.buttons:
            if not button.text():
                draw = 0
                break
        if draw:
            self.label.setText("Ничья!")
            self.stop_game()

    def diagonal_win(self, symbol):
        count = 0
        for i in range(9):
            if self.buttons[i].text() == symbol:
                count += 1
            if (i + 1) % 3 == 0:
                if count == 3:
                    return True
                count = 0
        return False


class MyWin1(QMainWindow):

    def __init__(self):#Подключение кнопок
        super().__init__()

        uic.loadUi('Псевдоним. Возвращение.ui', self)
        self.name, ok_pressed = QInputDialog.getText(self, "Введите имя", "Как тебя зовут?")
        self.setWindowTitle('Ним')
        self.ask.clicked.connect(self.help)
        self.to_take.clicked.connect(self.help2)
        self.button = QPushButton(self)
        self.button.move(700, 10)
        self.button.resize(70, 20)
        self.button.setText('Назад')
        self.button.clicked.connect(self.help3)

    def help(self):#Получения информации с дисплея и очистка всего
        self.remains.display(int(self.number_of_stones.text()))
        self.minus_x = int(self.number_of_stones.text())
        self.take_the_stones.clear()
        self.edit.clear()
        self._win_.setText('')

    def help2(self):#Игровой процесс, описание ходов ии
        x = int(self.take_the_stones.toPlainText())
        count = 1
        if int(x) > 0 and int(x) <= 3:
            self.eror.setText('')
            if int(x) <= 3:
                self.minus_x -= x
                self.edit.addItem(f'Игрок взял - {x}')
                self.remains.display(self.minus_x)
                if self.minus_x == 0:
                    self._win_.setText(f'Победил {self.name}')
            if (self.minus_x - 3) % 4 == 0:
                count = 3
            if (self.minus_x - 2) % 4 == 0:
                count = 2
            self.minus_x -= count
            self.remains.display(self.minus_x)
            self.edit.addItem(f'ИИ взял - {count}')
            if self.minus_x == 0:
                self._win_.setText(f'Победил ИИ')
        else:
            self.eror.setText('Не верное количество камней!!!')

    def help3(self):#Кнопка назад
        self.close()
        self.l = MyWidget()
        self.l.show()


class MyWin2(QMainWindow):

    def __init__(self):#Подключения кнопок
        super().__init__()
        self.setWindowTitle('Псевдо-ним')
        uic.loadUi('Псевдоним.ui', self)
        self.button = QPushButton(self)
        self.button.move(700, 0)
        self.button.resize(70, 20)
        self.button.setText('Назад')
        self.button.clicked.connect(self.help3)
        self.name, ok_pressed = QInputDialog.getText(self, "Введите имя", "Как тебя зовут?")
        self.setWindowTitle('Псевдо-ним')
        self.ask.clicked.connect(self.help)
        self.to_take.clicked.connect(self.help2)

    def help(self):#Получения информации с дисплея и очистка всего
        self.remains.display(int(self.number_of_stones.text()))
        self.minus_x = int(self.number_of_stones.text())
        self.take_the_stones.clear()
        self.edit.clear()
        self._win_.setText('')

    def help2(self):#Игровой процесс и описание ии
        x = int(self.take_the_stones.toPlainText())
        count = 1
        if int(x) > 0 and int(x) <= 3:
            self.eror.setText('')
            if int(x) <= 3:
                self.minus_x -= x
                self.edit.addItem(f'Игрок взял - {x}')
                self.remains.display(self.minus_x)
                if self.minus_x == 0:
                    self._win_.setText(f'Победил {self.name}')
            if (self.minus_x - 3) % 4 == 1:
                count = 3
            if (self.minus_x - 2) % 4 == 1:
                count = 2
            self.minus_x -= count
            self.remains.display(self.minus_x)
            self.edit.addItem(f'ИИ взял - {count}')
            if self.minus_x == 1:
                self._win_.setText(f'Победил ИИ')
        else:
            self.eror.setText('Не верное количество камней!!!')

    def help3(self):#Кнопка назад
        self.close()
        self.l = MyWidget()
        self.l.show()


class MyWin3(QMainWindow):#Очень *сырой* сапёр, может не сразу запуститься

    def __init__(self):#Окно сапёра
        super().__init__()

        self.setWindowTitle('Сапёр')
        self.setGeometry(700, 400, 600, 500)
        self.button = QPushButton(self)
        self.button.move(0, 0)
        self.button.resize(70, 20)
        self.button.setText('Назад')
        self.button.clicked.connect(self.help)
        self.sapper()

    def sapper(self):#Создание кнопок

        self.but_norm = []
        self.but = []
        for y in range(100, 370, 30):
            self.but.append([])
            for x in range(170, 440, 30):
                interval = QPushButton(self)
                interval.resize(30, 30)
                interval.move(x, y)
                interval.clicked.connect(self.set)
                self.but[-1].append(interval)
        for i in self.but:
            for j in i:
                self.but_norm.append(j)
        self.min()

    def help(self):#Открытия главной страницы
        self.close()
        self.m = MyWidget()
        self.m.show()

    def min(self):#Создание мин и их расположение

        self.bomb = QLabel(self)
        self.bomb.resize(50, 20)
        self.bomb.move(170, 50)
        self.bomb.setText('Бомб:')

        self.count = QLCDNumber(self)
        self.count.resize(50, 20)
        self.count.move(200, 50)
        self.bombs = 10
        self.count.display(self.bombs)
        self.mins2 = []
        for i in range(10):
            a = random.choice(self.but_norm)
            clear = self.but_norm.index(a)
            self.but_norm.pop(clear)
            self.mins2.append(a)

        self.but_norm.clear()
        for i in range(9):
            self.but[i].insert(0, [])
            self.but[i].append([])
        list = [[], [], [], [], [], [], [], [], []]
        self.but.append(list)
        self.but.insert(0, list)
        self.nomer = []
        self.helps()

    def set(self):#Если нажата кнопка с миной
        if self.sender() in self.mins2:
            self.a = Loser()
            self.a.show()
            self.loser()
        else:
            self.mines_around()

    def mines_around(self):#Обработка полей вокруг мины
        try:
            self.count = 0
            self.fields = 71
            for i in range(1, 10):
                for j in range(1, 10):
                    if self.but[i][j].pos() == self.sender().pos():
                        if self.but[i + 1][j] in self.mins2 and self.but[i + 1][j] != []:
                            self.count += 1
                        if self.but[i - 1][j] in self.mins2 and self.but[i - 1][j] != []:
                            self.count += 1
                        if self.but[i + 1][j - 1] in self.mins2 and self.but[i + 1][j - 1] != []:
                            self.count += 1
                        if self.but[i + 1][j + 1] in self.mins2 and self.but[i + 1][j + 1] != []:
                            self.count += 1
                        if self.but[i - 1][j - 1] in self.mins2 and self.but[i - 1][j - 1] != []:
                            self.count += 1
                        if self.but[i - 1][j + 1] in self.mins2 and self.but[i - 1][j + 1] != []:
                            self.count += 1
                        if self.but[i][j + 1] in self.mins2 and self.but[i][j + 1] != []:
                            self.count += 1
                        if self .but[i][j - 1] in self.mins2 and self.but[i][j - 1] != []:
                            self.count += 1
                        if self.count > 0:
                            self.sender().setText(f'{self.count}')
                        else:
                            self.sender().setEnabled(False)
                            for _ in range(1, 10):
                                for __ in range(1, 10):
                                    if self.but[_][__] not in self.mins2 and self.but[_][__] not in self.nomer:
                                        self.but[_][__].setText('  ')
                                        self.but[_][__].setEnabled(False)
            for _ in range(1, 10):
                for __ in range(1, 10):
                    if self.but[_][__].text() == '1' or self.but[_][__].text() == '2' or self.but[_][__].text() == '3'\
                            or self.but[_][__].text() == '4' or self.but[_][__].text() == '5' or\
                            self.but[_][__].text() == '  ' and self.but[_][__] != []:
                        self.fields -= 1
                        if self.fields == 0:
                            self.a = Winner()
                            self.a.show()
                            self.winner()
        except Exception as Er:
            print(Er)

    def helps(self):#Поля вокруг мин добавляем в список, что бы потом при нажатии на пустоту, убирать все пустые кнопки
                    # и оставлять только кнопки с минами и цифрами
        for i in range(1, 10):
            for j in range(1, 10):
                if self.but[i][j] in self.mins2:
                    if self.but[i + 1][j] != []:
                        self.nomer.append(self.but[i + 1][j])
                    if self.but[i - 1][j] != []:
                        self.nomer.append(self.but[i - 1][j])
                    if self.but[i + 1][j - 1] != []:
                        self.nomer.append(self.but[i + 1][j - 1])
                    if self.but[i + 1][j + 1] != []:
                        self.nomer.append(self.but[i + 1][j + 1])
                    if self.but[i - 1][j - 1] != []:
                        self.nomer.append(self.but[i - 1][j - 1])
                    if self.but[i - 1][j + 1] != []:
                        self.nomer.append(self.but[i - 1][j + 1])
                    if self.but[i][j + 1] != []:
                        self.nomer.append(self.but[i][j + 1])
                    if self.but[i][j - 1] != []:
                        self.nomer.append(self.but[i][j - 1])

    def winner(self):#Окно победы
        for _ in range(1, 10):
            for __ in range(1, 10):
                self.but[_][__].setText('')
                self.but[_][__].setEnabled(True)
        self.but_norm = []
        self.but = []
        self.mins2 = []
        self.nomer = []

    def loser(self):#Окно поражения
        for _ in range(1, 10):
            for __ in range(1, 10):
                self.but[_][__].setText('')
                self.but[_][__].setEnabled(True)
        self.but_norm = []
        self.but = []
        self.mins2 = []
        self.nomer = []







class Loser(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('Loser.ui', self)
        self.setWindowTitle('Проиграл')


class Winner(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('Winner.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
