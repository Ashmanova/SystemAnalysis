import math
import numpy as np

def task():
    # Создаем массивы с уникальными суммами и произведениями
    sums = sorted(set(i1 + i2 for i1 in range(1, 7) for i2 in range(1, 7)))
    products = sorted(set(i1 * i2 for i1 in range(1, 7) for i2 in range(1, 7)))

    # Создаем матрицу с количествами комбинаций для заданных суммы и произведения
    counts = np.zeros((len(sums), len(products)))
    for i in range(1, 7):
        for j in range(1, 7):
            sum_val = i + j
            product_val = i * j
            counts[sums.index(sum_val), products.index(product_val)] += 1

    entropy_A=0
    for i in range(counts.shape[0]):
        sum_A = sum(counts[i])
        entropy_A += sum_A / 36 * math.log2(sum_A / 36)

    entropy_B = 0
    for j in range(counts.shape[1]):
        sum_B=0
        for i in range(counts.shape[0]):
            sum_B+=counts[i,j]
        entropy_B += sum_B/36 * math.log2(sum_B/36)

    # Создаем матрицу с вероятностями комбинаций для заданных суммы и произведения
    p = counts / 36  # 36 возможных комбинаций (6 * 6)

    entropy_AB = 0
    for i in range(p.shape[0]):
        for j in range(p.shape[1]):
            if p[i, j] != 0:
                entropy_AB+=p[i,j]*(math.log2(p[i, j]))


    entropy_aB = entropy_AB - entropy_A
    information_AB = entropy_B - entropy_aB

    list = [-entropy_AB, -entropy_A, -entropy_B, -entropy_aB, -information_AB]
    rounded_list = [round(value, 2) for value in list]
    return rounded_list




if __name__ == '__main__':
    task()
