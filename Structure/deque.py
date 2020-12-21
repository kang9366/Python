score = []
while True:
    temp = input("입력 : ")
    try:
        if temp == "stop":
            break
        elif int(temp) > 100 or int(temp) < 0:
            print("잘못 입력")
        else:
            score.append(int(temp))
    except ValueError as e:
        print("잘못 입력")
    

rank = []
for i in range(0, len(score)):
    rank.append(1)

print(score)