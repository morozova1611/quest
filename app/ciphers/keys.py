import random

def text_edit(text):
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    alphabet_c = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    for i in text:
        state = False
        for j in range(len(alphabet)):
            if alphabet[j] == i or alphabet_c[j] == i:
                state = True
        if state == False:
            return state
    return text

# рандом ключа для одинарной перестановки

def key_single_permutation(text):
    key = []
    for i, s in enumerate(text, start=1):
        key.append(i)
    random.shuffle(key, random.random)
    return key


# рандом матрицы
def matrix():  # Функция выбора ключа из 10 возможных
    new_matrix = [[[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 1]],
                  [[4, 5, 14, 11], [1, 15, 8, 10], [16, 2, 9, 7], [13, 12, 3, 6]],
                  [[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]],
                  [[2, 12, 5, 15], [9, 8, 11, 6], [16, 1, 14, 3], [7, 13, 4, 10]],
                  [[9, 6, 12, 7], [2, 11, 5, 16], [15, 14, 4, 1], [8, 3, 13, 10]],
                  [[13, 7, 10, 4], [8, 1, 16, 9], [11, 12, 5, 6], [2, 14, 3, 15]],
                  [[4, 13, 3, 14], [5, 8, 10, 11], [16, 1, 15, 2], [9, 12, 6, 7]],
                  [[3, 14, 1, 16], [8, 11, 6, 9], [13, 2, 15, 4], [10, 7, 12, 5]],
                  [[16, 11, 6, 1], [2, 5, 12, 15], [3, 8, 9, 14], [13, 10, 7, 4]],
                  [[9, 16, 1, 8], [15, 5, 12, 2], [6, 10, 7, 11], [4, 3, 14, 13]],
                  [[7, 4, 9, 14], [13, 10, 3, 8], [2, 5, 16, 11], [12, 15, 6, 1]],
                  [[16, 7, 10, 1], [3, 6, 11, 14], [2, 9, 8, 15], [13, 12, 5, 4]],
                  [[5, 2, 15, 12], [10, 16, 1, 7], [11, 13, 4, 6], [8, 3, 14, 9]],
                  [[3, 6, 12, 13], [15, 8, 10, 1], [14, 9, 7, 4], [2, 11, 5, 16]],
                  [[9, 14, 4, 7], [2, 3, 13, 16], [15, 6, 12, 1], [8, 11, 5, 10]],
                  [[11, 4, 13, 6], [8, 9, 16, 1], [10, 7, 2, 15], [5, 14, 3, 12]],
                  [[12, 13, 8, 1], [2, 7, 14, 11], [5, 4, 9, 16], [15, 10, 3, 6]],
                  [[15, 6, 9, 4], [14, 1, 12, 7], [3, 16, 5, 10], [2, 11, 8, 13]],
                  [[13, 16, 2, 3], [10, 1, 15, 8], [7, 12, 6, 9], [4, 5, 11, 14]],
                  [[13, 12, 6, 3], [10, 5, 11, 8], [7, 16, 2, 9], [4, 1, 15, 14]],
                  [[6, 4, 13, 11], [7, 15, 10, 2], [9, 1, 8, 16], [12, 14, 3, 5]],
                  [[10, 13, 3, 8], [6, 1, 15, 12], [11, 4, 14, 5], [7, 16, 2, 9]],
                  [[4, 10, 7, 13], [9, 15, 2, 8], [5, 3, 14, 12], [16, 6, 11, 1]]]

    return random.choice(new_matrix)


def key_vigenere():
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    key = ''
    for i in range(5):
        key = key + alphabet[random.randint(0, 32)]
    return key

def key_gamma(text):
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    key = ''
    for i in range(len(text)):
        key = key + alphabet[random.randint(0, 32)]
    return key


