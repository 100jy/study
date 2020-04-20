def solution(n):
    rep = ['4', '1', '2']
    remain = n
    answer = ''
    if n>3:
        while remain > 0:
            remain //= 3
            idx = (remain % 3) - 1
            answer = rep[idx] + answer
    else:
        idx = (n % 3) - 1
        print(rep[idx])
        answer = rep[idx] + answer

    return answer

solution(1)