import csv
import numpy as np
from io import StringIO

def task(csv_string):
    csv_data = StringIO(csv_string)
    data = np.genfromtxt(csv_data, delimiter=',', dtype=float)
    #определяем сколько узлов
    gr = []
    for i in data:
        if i[0] not in gr:
            gr.append(i[0])
        if i[1] not in gr:
            gr.append(i[1])

    # матрица для ответов
    m = np.zeros((len(gr), 5))
    for i in data:
        point = list(map(int, i))
        m[point[0]-1][0]+=1
        m[point[1]-1][1]+=1
        for j in data:
            point2 = list(map(int, j))
            if point2[0] == point[1]:
                m[point[0]-1][2]+=1
                m[point2[1]-1][3]+=1
            if point2[0] == point[0] and point2[1] != point[1]:
                m[point2[1]-1][4]+=1
    csv_string = ""
    np.savetxt('temp.csv', m, delimiter=',', fmt='%d')
    with open('temp.csv', 'r') as file:
        csv_string = file.read()
    return csv_string



if __name__ == '__main__':
    path = 'task2.csv'
    with open(path, 'r') as file:
        reader_csv = file.read()
        task(reader_csv)



