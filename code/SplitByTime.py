# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import csv
import pandas as pd
import matplotlib.pylab as plt
my_dict = {}

def extract_csv (name_of_file):
    file = open(name_of_file)
    type(file)
    data = pd.read_csv(file)
    df = pd.DataFrame(data, columns=['הסיפור']) #, 'שם סיפור','שם מלא'])
    print(df)
    size = df.size
    return df, size



def split_story(name_of_file):
    df,size = extract_csv(name_of_file)
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

    num_of_words=0
    num_of_quse=0
    num_of_ex=0
    avg = 0
    x_label: float = 0
    for item in my_dict:
       num_of_words += my_dict[item][0]
       num_of_ex += my_dict[item][1]
       num_of_quse += my_dict[item][2]

    return (num_of_ex + num_of_quse )/num_of_words







if __name__ == '__main__':
    x_label=['םייניבה ימי','הלכשהה','היחתה','השדח תירבע תורפס']
    #x_label = ["ימי הביניים","ההשכלה","התחייה","ספרות עברית חדשה"]
    y_label =[]
    y_label.append(split_story("MedievalPeriod.csv"))
    y_label.append(split_story("PeriodOfEducation.csv"))
    y_label.append(split_story("RevivalPeriodN.csv"))
    y_label.append(split_story("NewHebrewLiteratureN.csv"))
    plt.bar(x_label, y_label, width=0.25, color='orange', label="(Q+E) /num of words")
   # plt.bar(x_label, num_of_ex, width=0.25, bottom=num_of_quse, color='b', label="Ex Mark")
    plt.xticks(x_label)
    plt.xlabel("Period Time")
    plt.ylabel("Averge of (Q+E) /num of words from All Stories")
    plt.legend()
    plt.title("Period")
    plt.show()