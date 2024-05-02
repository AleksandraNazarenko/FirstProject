from tkinter import *


class Cat:

  def __init__(self):
    self.root = Tk()
    self.root.title("Cat Timer")
    self.root.config(bg="white")
    #Таймер
    button = Button(self.root)
    button.config(bg="pink",
                  text="Начать заниматься!",
                  command=self.new_window)
    button.pack()
    self.root.mainloop()

  def new_window(self):
    Window().mainloop()


class Window:

  def __init__(self):
    self.master = Tk()
    self.master.config(bg="white")
    self.master.title("Cat Timer")
    label = Label(self.master, text="Выберите время:", bg="white")
    button1 = Button(self.master)
    button2 = Button(self.master)
    button3 = Button(self.master)
    button1.config(bg="pink", text="30 минут", command=self.thirty_minutes)
    button2.config(bg="pink", text="45 минут", command=self.forty_five_minutes)
    button3.config(bg="pink", text="1 час", command=self.one_hour)
    label.pack()
    button1.pack()
    button2.pack()
    button3.pack()
    self.master.mainloop()

  def thirty_minutes(self):
    ThirtyMinutes().mainloop()

  def forty_five_minutes(self):
    FortyFiveMinutes().mainloop()

  def one_hour(self):
    OneHour().mainloop()

class ThirtyMinutes:

  def __init__(self):
    self.master1 = Tk()
    self.master1.config(bg="white")
    self.master1.title("Cat Timer")
    #Timer
    button1 = Button(self.master1)
    button1.config(bg="pink", text="Стоп")
    button1.pack()
    self.master1.mainloop()


class FortyFiveMinutes:

  def __init__(self):
    self.master2 = Tk()
    self.master2.config(bg="white")
    self.master2.title("Cat Timer")
    #Timer
    button1 = Button(self.master2)
    button1.config(bg="pink", text="Стоп")
    button1.pack()
    self.master2.mainloop()


class OneHour:

  def __init__(self):
    self.master3 = Tk()
    self.master3.config(bg="white")
    self.master3.title("Cat Timer")
    #Timer
    button1 = Button(self.master3)
    button1.config(bg="pink", text="Стоп")
    button1.pack()
    self.master3.mainloop()


if __name__ == "__main__":
  Cat()