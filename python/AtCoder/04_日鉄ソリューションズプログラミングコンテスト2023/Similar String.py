N = int(input())
S = input()
T = input()

x = True

for i in range(N):
    if S[i] == T[i]:
        continue
    else:
        if (
            (S[i] == "o" and T[i] == "0")
            or (S[i] == "l" and T[i] == "1")
            or (S[i] == "0" and T[i] == "o")
            or (S[i] == "1" and T[i] == "l")
        ):
            continue
        else:
            x = False

if x:
    print("Yes")
else:
    print("No")
