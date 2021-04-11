def solution(s1, s2):
    
    s1 = s1.split(":")
    s2 = s2.split(":")
    
    # 先轉成秒
    start = 60 * 60 * int(s1[0]) + 60 * int(s1[1]) + int(s1[2])
    end = 60 * 60 * int(s2[0]) + 60 * int(s2[1]) + int(s2[2])
    ans = 0
    
    # 掃時間
    for i in range(start, end + 1):
        arr = hms(i)                     # 再轉成 h:m:s
        if arr[0] == arr[1] and arr[1] == arr[2]:
            continue
        if arr[0] == arr[1]:
            ans += 1
            continue
        if arr[0] == arr[2]:
            ans += 1
            continue
        if arr[1] == arr[2]:
            ans += 1
    return ans

def hms(sec):
    h = sec // 3600
    m = sec % 3600 // 60
    s = sec % 60
    return [h, m, s]

s1 = "10:11:09"
s2 = "10:11:12"
print(solution(s1, s2))