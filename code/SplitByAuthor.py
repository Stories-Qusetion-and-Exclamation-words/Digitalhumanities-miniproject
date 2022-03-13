# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import csv
import pandas as pd
import matplotlib.pylab as plt
my_dict = {}

def extract_csv ():
    file = open('adambaruch.csv')
    type(file)
    data = pd.read_csv(file)
    df = pd.DataFrame(data, columns=['הסיפור']) #, 'שם סיפור','שם מלא'])
    print(df)
    size = df.size
    split_story(df,size)
    print(my_dict)



def split_story(df, size):

    index_story = 0
    for index_story in range(size):
        for row in df.loc[index_story]:
            ques_mark = 0
            ex_mark=0
            num_words=1
            for letter in row:
                if letter == '!':
                    ex_mark += 1
                elif letter == '?':
                    ques_mark += 1
                elif letter == ' ':
                    num_words+=1
            my_dict[index_story]=[num_words,ex_mark,ques_mark]

    num_of_words=[]
    num_of_quse=[]
    num_of_ex=[]
    avg = []
    x_label: float = []
    for item in my_dict:
       num_of_words.append(my_dict[item][0])
       num_of_ex.append(my_dict[item][1])
       num_of_quse.append(my_dict[item][2])
       curr:int = (num_of_ex[item]+num_of_quse[item])/num_of_words[item]
       avg.append(curr)
       x_label.append(item+1)
    plt.plot(x_label, avg, color='g')
    plt.xticks([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    plt.xticks(x_label)
    plt.xlabel("Story number")
    plt.ylabel("(Question+ Exclamation) \ Words")
    plt.legend()
    plt.title("ךורב םדא")
    plt.show()
       # index_story += 1






if __name__ == '__main__':
    extract_csv()