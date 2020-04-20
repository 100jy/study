def solution(land, height):
    answer = 0
    n = len(land)
    arr = []

    def search(i, j, k, d, cost):
        global mini
        if k == n:
            mini = cost

        if mini != 0:
            if cost >= answer:
                return

        if d == 'R':
            dist = abs(land[i - 1][j] - land[i][j])
            if dist > height:
                cost += dist

        if d == 'D':
            dist = abs(land[i][j - 1] - land[i][j])
            if dist > height:
                cost += dist
        if d == 'L':
            dist = abs(land[i + 1][j] - land[i][j])
            if dist > height:
                cost += dist

        if d == 'U':
            dist = abs(land[i][j + 1] - land[i][j])
            if dist > height:
                cost += dist

        if 0 <= i + 1 <= n - 1 and 0 <= j <= n - 1:
            search(i + 1, j, k + 1, 'R', cost)
        if 0 <= i <= n and 0 <= j + 1 <= n - 1:
            search(i, j + 1, k + 1, 'D', cost)
        if 0 <= i - 1 <= n and 0 <= j <= n - 1:
            search(i - 1, j, k + 1, 'L', cost)
        if 0 <= i <= n and 0 <= j - 1 <= n - 1:
            search(i, j - 1, k + 1, 'U', cost)

        return mini

    for i in range(n):
        for j in range(n):
            global mini
            mini = 0
            arr.append(search(i, j, 0, 0, 0))

    print(arr)

    return answer


if __name__ == '__main__':
    print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3))

