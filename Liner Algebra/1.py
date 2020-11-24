import numpy as np

for i in range(1, 10):
    for j in range((i*10)+1, (i*10) + 10):
        globals()['arr_{}'.format(j)] = []

solution = []

for i in range(1, 10):
    print("======== R" + str(i) + " ========")
    s = (i*10)+1 # 행의 시작 지점
    e = (i*10) + 9 # 행의 끝 지점

    # R1 선형방정식
    if i == 1:
        equation = "4 * X" + str(s) + " - X" + str(s+1) + " - X" + str(s+10) + " = T1 + T3"
        print(equation)
        
        arr_11.append(4)
        arr_11.append(-1)
        for i in range(int(equation[11:13]), int(equation[17:19]) - 2):
            arr_11.append(0)
        arr_11.append(-1)
        for i in range(int(equation[17:19]), 100-8):
            arr_11.append(0)
        solution.append("T1 + T3")

        for j in range(s+1, e):
            equation = "- X" + str(j-1) + " + 4 * X" + str(j) + " - X" + str(j+1) + " - X" + str(j+10) + " = T3"
            print(equation)
            # X12 ~ X18 행렬
            for i in range(11, int(equation[3:5])):
                globals()['arr_{}'.format(j)].append(0)
            globals()['arr_{}'.format(j)].append(-1)

            for i in range(int(equation[3:5]), int(equation[13:15])-1):
                globals()['arr_{}'.format(j)].append(0)
            globals()['arr_{}'.format(j)].append(4)

            for i in range(int(equation[13:15]), int(equation[19:21])-1):
                globals()['arr_{}'.format(j)].append(0)
            globals()['arr_{}'.format(j)].append(-1)

            for i in range(int(equation[19:21])+1, int(equation[25:27])-1):
                globals()['arr_{}'.format(j)].append(0)
            globals()['arr_{}'.format(j)].append(-1)

            for i in range(int(equation[25:27])-1, 91):
                globals()['arr_{}'.format(j)].append(0)
            
            solution.append("T3")
            
        # X19 선형방정식, 행렬
        equation = "- X" + str(e-1) + " + 4 * X" + str(e) + " - X" + str(e+10) + " = T2 + T3\n"
        print(equation)
        for i in range(11, int(equation[3:5])):
            arr_19.append(0)
        arr_19.append(-1)
        arr_19.append(4)
        for j in range(int(equation[3:5])+1, int(equation[19:21])-1):
            arr_19.append(0)
        arr_19.append(-1)
        for k in range(int(equation[19:21]), 91):
            arr_19.append(0)
        solution.append("T2 + T3")
        

    # R9 선형방정식
    elif i == 9:
        # 1열 선형방정식
        equation = "- X" + str(s-10) + " + 4 * X" + str(s) + " - X" + str(s+1) + " = T1 + T4"
        print(equation)

        # 1열 행렬
        for i in range(11, int(equation[3:5])-7):
            arr_91.append(0)
        arr_91.append(-1)
        for i in range(int(equation[3:5])+1, int(equation[13:15])-1):
            arr_91.append(0)
        arr_91.append(4)
        arr_91.append(-1)
        for i in range(int(equation[19:21]), 99):
            arr_91.append(0)
        
        solution.append("T1 + T4")

        # 2~8 열 행렬
        for j in range(s+1, e):
            equation = "- X" + str(j-10) + " - X" + str(j-1) + " + 4 * X" + str(j) + " - X" + str(j+1) + " = T4"
            print(equation)
            for i in range(11, int(equation[3:5])-7):
                globals()['arr_{}'.format(j)].append(0)
            globals()['arr_{}'.format(j)].append(-1)
            for i in range(int(equation[3:5])+1, int(equation[9:11])-1):
                globals()['arr_{}'.format(j)].append(0)
            globals()['arr_{}'.format(j)].append(-1)
            globals()['arr_{}'.format(j)].append(4)
            globals()['arr_{}'.format(j)].append(-1)
            for i in range(int(equation[9:11])+1, 99-1):
                globals()['arr_{}'.format(j)].append(0)

            solution.append("T4")
        
        # 9열
        equation = "- X" + str(e-10) + " - X" + str(e-1) + " + 4 * X" + str(e) + " = T2 + T4\n"
        print(equation)
        for i in range(11, int(equation[3:5])-7):
            arr_99.append(0)
        arr_99.append(-1)
        for i in range(int(equation[3:5])+1, int(equation[9:11])-1):
            arr_99.append(0)
        arr_99.append(-1)
        arr_99.append(4)

        solution.append("T2 + T4")

    # R2 ~ R8 선형방정식
    else:
        # 1열
        equation = "- X" + str(s-10) + " + 4 * X" + str(s) + " - X" + str(s+1) + " - X" + str(s+10) + " = T1"
        print(equation)

        if int(equation[3:5]) == 11:
            globals()['arr_{}'.format((i*10)+1)].append(-1)
        else:
            for j in range(0, 9*(i-2)):
                globals()['arr_{}'.format((i*10)+1)].append(0)
            globals()['arr_{}'.format((i*10)+1)].append(-1)
        
        for j in range(0, 8):
            globals()['arr_{}'.format((i*10)+1)].append(0)
        globals()['arr_{}'.format((i*10)+1)].append(4)
        globals()['arr_{}'.format((i*10)+1)].append(-1)

        for j in range(0, 7):
            globals()['arr_{}'.format((i*10)+1)].append(0)
        globals()['arr_{}'.format((i*10)+1)].append(-1)
        
        for j in range(0, 8 + (9*(9-(i+1)))):
            globals()['arr_{}'.format((i*10)+1)].append(0)

        
        solution.append("T1")

        # 2~8열
        for j in range(s+1, e):
            equation = "- X" + str(j-10) + " - X" + str(j-1) + " + 4 * X" + str(j) + " - X" + str(j+1) + " - X" + str(j+10) + " = 0"
            print(equation)

            for k in range(0, j-21-(i-2)):
                globals()['arr_{}'.format(j)].append(0)
            globals()['arr_{}'.format(j)].append(-1)

            for k in range(0, 7):
                globals()['arr_{}'.format(j)].append(0)
            globals()['arr_{}'.format(j)].append(-1)
            globals()['arr_{}'.format(j)].append(4)

            for k in range(0, 8):
                globals()['arr_{}'.format(j)].append(0)
            globals()['arr_{}'.format(j)].append(-1)

            for k in range(0, 99 - int(equation[31:33])):
                globals()['arr_{}'.format(j)].append(0)
            
            print(globals()['arr_{}'.format(j)])
            print(len(globals()['arr_{}'.format(j)]))
            solution.append(0)
        
        # 9열
        equation = "- X" + str(e-10) + " - X" + str(e-1) + " + 4 * X" + str(e) + " - X" + str(e+10) + " = T2\n"
        print(equation)

        for j in range(0, 9*(i-1)-1):
            globals()['arr_{}'.format((i*10)+9)].append(0)
        globals()['arr_{}'.format((i*10)+9)].append(-1)

        for j in range(0, 7):
            globals()['arr_{}'.format((i*10)+9)].append(0)
        globals()['arr_{}'.format((i*10)+9)].append(-1)
        globals()['arr_{}'.format((i*10)+9)].append(4)

        for j in range(0, 8):
            globals()['arr_{}'.format((i*10)+9)].append(0)
        globals()['arr_{}'.format((i*10)+9)].append(-1)
            
        if int(equation[25:27]) < 99:
            for j in range(0, 9*(9-(i+1))):
                globals()['arr_{}'.format((i*10)+9)].append(0)
        
        solution.append("T2")

for i in range(1, 10):
    for j in range((i*10)+1, (i*10) + 10):
        globals()['arr_{}'.format(j)] = np.array([globals()['arr_{}'.format(j)]])
        print(globals()['arr_{}'.format(j)])
        print(len(globals()['arr_{}'.format(j)]))

solution = np.array([solution])
print(solution)
