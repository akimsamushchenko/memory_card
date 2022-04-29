#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle, randint
class Question():


    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


app = QApplication([])
win = QWidget()

win.resize(600, 400)
win.setWindowTitle('Memory Card')

text = QLabel('Какой нацианальности не существует')
btn = QPushButton('Ответить')

v1 = QRadioButton('в 1')
v2 = QRadioButton('в 2')
v3 = QRadioButton('в 3')
v4 = QRadioButton('в 4')

l1 = QHBoxLayout()
l2 = QVBoxLayout()
l3 = QVBoxLayout()

l2.addWidget(v1, alignment= Qt.AlignLeft)
l2.addWidget(v3, alignment= Qt.AlignLeft)
l3.addWidget(v2, alignment= Qt.AlignLeft)
l3.addWidget(v4, alignment= Qt.AlignLeft)
l1.addLayout(l2)
l1.addLayout(l3)

rgb = QGroupBox('Варианты ответов')
rgb.setLayout(l1)


l4 = QHBoxLayout()
l5 = QHBoxLayout()
l6 = QHBoxLayout()
l4.addWidget(text, alignment= Qt.AlignCenter)
l5.addWidget(rgb, alignment= Qt.AlignCenter)
l6.addWidget(btn)

main_line = QVBoxLayout()
main_line.addLayout(l4)
main_line.addLayout(l5)
main_line.addLayout(l6)

#Скрой варианты ответов 




t1 = QLabel('Правильно/неправильно')
t2 = QLabel('Правильный ответ')

l7 = QVBoxLayout()
l7.addWidget(t1)
l7.addWidget(t2)
gr = QGroupBox('Результат текста')
gr.setLayout(l7)
gr.hide()
l5.addWidget(gr)

RadioGroup= QButtonGroup()
RadioGroup.addButton(v1)
RadioGroup.addButton(v2)
RadioGroup.addButton(v3)
RadioGroup.addButton(v4)


def show_question():
    rgb.show()
    gr.hide()
    btn.setText('Ответить')
    RadioGroup.setExclusive(False)
    v1.setChecked(False)
    v2.setChecked(False)
    v3.setChecked(False)
    v4.setChecked(False)
    RadioGroup.setExclusive(True)


def show_result():
    rgb.hide()
    gr.show()
    btn.setText('Следующий вопрос')
'''
def start_test():
    if 'Ответить' == btn.text(): 
        show_resu()
    else:
        show_result()

'''

answers = [v1, v2, v3, v4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    text.setText(q.question)
    t2.setText(q.right_answer)
    show_question()

def check_answer():
    if answers[0].isChecked():
        win.score += 1
        show_correct('правильно')
    if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('неправильно')
    rt = (win.score/win.total*100)
    print('рейтинг:',rt)
    print('статистика:')
    print('правильных ответов:',win.score)
    print('Всего ответов:', win.total)
    

   



def show_correct(res):
    t1.setText(res)
    show_result()


win.total = 0
win.score = 0

def next_question():
    rand = randint(0, len(list_question) -1)
    q = list_question[rand]
    ask(q)
    win.total += 1
  



def click_ok():
    if btn.text() == 'Ответить':
        check_answer()
    else:
        next_question()



list_question = list() 
q = Question('Подвижный холм песка в пустыне называется…', 'Дюна', 'Утес', 'Скала', 'Гора')
q1 = Question('Как называется повар на судне?', 'Кок', 'Квартирмейстер', 'Канонир', 'Боцман')
q2 = Question('Где находится яд у кобры?', 'В зубе', 'На кончике языка', 'В хвосте', 'В капюшоне')
q3 = Question('Какая самая высокая гора в мире', 'Эверест(Джомолунгма)', 'Эльбрус', 'Олимп', 'Монблан')
q4 = Question('Как называется помещение на судне, где живут матросы?', 'Кубрик', 'Келья', 'Квартира','Кабинет')
q5 = Question('Что использовали японцы вместо денег до появления монет?', 'Рис и ткани', ' Жемчужины', 'Картофель', 'Ракушки')
q6 = Question('У какой птицы самое острое зрение?', ' У орла', 'У дятла', 'У скворца', 'У ворона')
q7 = Question('У кого из перечисленных животных самый острый слух?', 'У летучей мыши', 'У ежа',  'У кошки', 'У собаки')
q8 = Question('Какая самая маленькая страна в мире', 'Ватикан', 'Кипр', 'Люксембург', 'Черногория')



list_question.append(q)
list_question.append(q1)
list_question.append(q2)
list_question.append(q3)
list_question.append(q4)
list_question.append(q5)
list_question.append(q6)
list_question.append(q7)
list_question.append(q8)

next_question()







btn.clicked.connect(click_ok)
win.setLayout(main_line)
win.show()
app.exec()



