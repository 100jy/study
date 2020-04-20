def solution(answers):
    answer = []

    ch_1, ch_2, ch_3 = [0, 0, 0]
    array_1 = [1, 2, 3, 4, 5]
    array_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    array_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    list = [array_1, array_2, array_3]
    a = []
    length = len(answers)

    for i in range(3):
        n = length // len(list[i])
        el = (length % len(list[i]))
        a.append(list[i] * n + list[i][:el])

    for i in range(length):

        if answers[i] == a[0][i]:
            ch_1 += 1
        if answers[i] == a[1][i]:
            ch_2 += 1
        if answers[i] == a[2][i]:
            ch_3 += 1

    arr = [ch_1, ch_2, ch_3]

    for i in range(3):
        if arr[i] == max(arr):
            answer.append(i + 1)

    return answer


answers = [1, 3, 2, 4, 2]
solution(answers)
