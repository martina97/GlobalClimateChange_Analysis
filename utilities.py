import calendar
from random import random, choice

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def chooseMonth():
    print("Inserire numero mese per visualizzare grafico:\n",
    "- Gennaio: 1\n",
    "- Febbraio: 2\n",
    "- Marzo: 3\n",
    "- Aprile: 4\n",
    "- Maggio: 5\n",
    "- Giugno: 6\n",
    "- Luglio: 7\n",
    "- Agosto: 8\n",
    "- Settembre: 9\n",
    "- Ottobre: 10\n",
    "- Novembre: 11\n",
    "- Dicembre: 12\n")

    print("Inserire un numero tra quelli elencati:")

    month = input()
    while int(month)>12 or int(month)<1 :
        print("Inserire un numero valido:")
        month = input()

    return int(month)


def chooseRandom(myList, title):

    myList = list(set(myList))
    value = choice(myList)
    #print("Randomly choosen ",title," : ", value)
    return value


def regressionLine(x, y, title):

    plt.plot(x,y,'o')
    m, b = np.polyfit(x, y, 1)
    print ("\nm: ",m, "b:",b)
    plt.plot(x, m * np.array(x) + b)
    plt.xlabel("Years")
    plt.ylabel("Temperature")
    plt.title(title)
    plt.show()
    
    

def main():
    print("Hello World!\n")





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
