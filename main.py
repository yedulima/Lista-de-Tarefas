"""

TASKS DE TAREFAS

Cada pessoa terá seu próprio calendário. Será necessário que cada pessoa 
tenha acesso a pedir o dia da semana, tempo atual (horas, minutos e
segundos), além de poder marcar uma tarefa específica para um dia da
semana.

Neste calendário deverá ter as seguintes funções:

- ADICIONAR;
- REMOVER;
- MODIFICAR;
- MOSTRAR;

(Basicamente um C.R.U.D como já apresentado na disciplina de Programação
Estruturada)

LEMBRANDO: CADA PESSOA TEM DE TER SUA PRÓPRIA LISTA, SEM TER ACESSO AS
LISTAS DAS OUTRAS PESSOAS POR QUESTÕES DE PRIVACIDADE!

Boa sorte!

"""

import schedule
from time import sleep
from datetime import date, datetime
from calendar import day_name
from os import system
from sys import exit

class TaskCalendar:
    def __init__(self):
        self.__tasks: dict = {}

    def addTask(self, name: str, description='') -> bool:
        if name not in self.__tasks:
            self.__tasks[name] = {
                "Task_register": ':'.join(self.__getCurrentTime()),
                "Task_modify": '',
                "Task_description": description if len(description) else ''
            }
            return True
        return False

    def removeTask(self, task: str) -> bool:
        if task in self.__tasks:
            del self.__tasks[task]
            return True
        return False

    def modifyTask(self, name: str, description='') -> bool:
        if name in self.__tasks:
            self.__tasks[name] = {
                "Task_register": self.__tasks[name]['Task_register'],
                "Task_modify": ':'.join(self.__getCurrentTime()),
                "Task_description": description if len(description) else self.__tasks[name]['Task_description']
            }
            return True
        return False

    def showTasks(self) -> bool:
        if len(self.__tasks):
            for task in self.__tasks:
                print(f"{'='*5} {task} {'='*5}\n")
                print(f"Description:\n{self.__formatText(self.__tasks[task]['Task_description'], 6)}")
                print(f"Task register: {self.__tasks[task]['Task_register']}")
                if len(self.__tasks[task]['Task_modify']):
                    print(f"Task modify: {self.__tasks[task]['Task_modify']}")
            return True
        return False

    def __formatText(text: str, key: int) -> str:
        # text = String de entrada
        # key = Palavras por linha

        words: int = 0
        final_text: str = ''
        word_count: int = 0

        text = text.split()

        while word_count != len(text):
            if words != key:
                final_text += f'{text[word_count]} '
                words += 1
                word_count += 1
                continue

            words = 0
            final_text += '\n'
        
        return final_text

    @staticmethod
    def __getWeekName() -> str:
        return day_name[date.today().weekday()]
    
    @staticmethod
    def __getCurrentTime() -> tuple:
        current_time: str = str(datetime.now())[11:19]
        hours, minutes, seconds = current_time.split(':')
        return hours, minutes, seconds

    def __str__(self):
        return "This class have some functions about tasks calendar\nto each person."

class Person(TaskCalendar):
    pass

if __name__ == "__main__":
    newPerson = Person()
    system('clear')
    while True:
        try:
            c = int(input("A: "))
        except:
            print("\nError\n")
            input()
            system('clear')
        else:
            if c == 1:
                task_name = input("Insert new task name: ")
                task_description = input("Inser new task description or ENTER\nfor skip: ")
                confirm = newPerson.addTask(task_name, task_description)
                if confirm:
                    print("Sucess")
                    continue
                print("Failure in the operation")

            elif c == 2:
                newPerson.showTasks()
                task_name = input("Insert task name: ")
                confirm = newPerson.removeTask(task_name)
                if confirm:
                    print("Sucess")
                    continue
                print("Failure in the operation")

            elif c == 3:
                newPerson.showTasks()
                task_name = input("Insert new task name: ")
                task_description = input("Inser new task description or ENTER\nfor skip: ")
                confirm = newPerson.modifyTask(task_name, task_description)
                if confirm:
                    print("Sucess")
                    continue
                print("Failure in the operation")

            elif c == 4:
                if not newPerson.showTasks():
                    print("Failure in the operation")

            elif c == 0:
                exit()