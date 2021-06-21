def main():
    def judge(m):
        count = 0
        old = 0
        for i in range(0, n):
            if a[i] - old >= m and l - a[i] >= m:
                count += 1
                old = a[i]
        if (count >= k):
            return True
        else:
            return False

    n, l = map(int, input().split())
    k = int(input())
    a = list(map(int, input().split()))

    left = 0
    right = l

    while(right - left > 1):
        mid = left + (right - left) // 2
        if judge(mid):
            left = mid
        else:
            right = mid
    print(left)

if __name__=="__main__":
    main()