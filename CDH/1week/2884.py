H, M = map(int, input().split())  # 현재 알람 시간을 입력받음

if M >= 45:
    M -= 45
else:
    if H == 0:
        H = 23
    else:
        H -= 1
    M += 15

print(f"{H} {M}")
