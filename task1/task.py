import csv

def read_csv(path,x,y):
    with open(path, encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter=",")
        for row in enumerate(file_reader):
            if row[0]==x:
                return (row[1][y])




if __name__ == '__main__':
    print(read_csv('C:/Users/22354/Desktop/example.csv',3,2))


