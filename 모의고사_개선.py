def solution(answers):
    answer = []

    ch_1, ch_2, ch_3 = [0, 0, 0]
    array_1 = [1, 2, 3, 4, 5]
    array_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    array_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i,num in enumerate(answers):
        if num == array_1[i % len(array_1)]:
            ch_1 += 1
        if num == array_1[i % len(array_2)]:
            ch_2 += 1
        if num == array_1[i % len(array_3)]:
            ch_3 += 1
    a = [ch_1, ch_2, ch_3]
    for i in range(3):
        if a[i] == max(a):
            answer.append(i+1)

    return print(answer)

answers = [1, 3, 2, 4, 2]
solution(answers)
