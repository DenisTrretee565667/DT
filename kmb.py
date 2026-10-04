from tkinter import *
import random
beats = {
    'Камень': 'Ножницы',
    'Ножницы': 'Бумага',
    'Бумага': 'Камень',
}
emoj = {
    "Камень": '✊🏿',
    'Бумага': '✋🏿',
    'Ножницы': '✌🏿'
}

class RockPaperScissors(Frame):
    def _init_(self, root):
        super()._init_(root)

        self.root = root

        self.win = 0
        self.lose = 0
        self.draw = 0

        self.build_ui()
    
    def build_ui(self):
        self.result_label(
            self.root,
            text = 'Ходи',
            bg = '#FFF',
            font=('Times New Roman', 20, 'bold'),
            fg='#333'
        )
        self.result_label.place(x=0, y=15, width=430)

        self.comp_label = Label(
            self.root,
            text = '#Компьютер: -',
            bg='#FFF',
            front=("Times New Roman", 13),
           fg = '#666'

        )
        self.comp_label.place(x=0, y=55, width=430)

        buttons = [('Камень', 10), ('Ножницы', 155), ('Бумага', 300)]
        for text, x in buttons:
            Button(
                self.root,
                text=f"{emoj[text]}, {text}",
                front=("Times New Roman", 14),
                bg= "#FF0B0B",
                activebackground= "#F2FF00",
                command=lambda t =text: self.play(t)

            ).place(x=x, y = 90, width=120, height=50)
        Button(
            self.root,
            text = 'Сбросить счёт',
            font = ("Times New Roman", 10),
            command= self.reset_store

        ).place(x= 300, y =150, widght=120, height = 25)

        self.score_label = Label(
            self.root,
            justify= "left",
            font = ("Times New Roman", 12)
            text = self.format_score(),
            bg='#FFF',
            fg ='#222'


        )
        self.score_label.place(x=10, y=148)


    def play(self, player_choice):
        comp_choice = random.choice(list(beats.keys()))

        if player_choice == comp_choice:
            self.draw+=1
            verdict = "Ничья"
            color = '#888',
        elif beats[player_choice] == comp_choice:
            self.win += 1
            verdict = 'Поздравляю'
            color = "#0C7C10"
        else:
            self.lose += 1
            verdict = 'Проигрыш'
            color = "#7C0C0C"

        self.result_label.config(text=verdict, fg=color)

        self.comp_label.config(text=f"Компьютер: {emoj[comp_choice]} {comp_choice}")

    def reset_score(self):
        self.win = self.lose = self.draw = 0
        self.result_label.config(text='Счёт сброшен', fg='#333')
        self.comp_label.config(text='Компьютер: -')
        self.score_label.config(text=self.format_score())

    def format_score(self):
        
