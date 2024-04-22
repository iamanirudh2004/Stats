import pandas as pd
import matplotlib.pyplot as plt
x_axis = [i for i in range(1, 11)]
count1 = 0
count10 = 0
df2 = pd.read_csv("new_data.csv")
for j in range (36, 176, 20):

    y_axis = [0*i for i in range(1, 11)]
    for index, row in df2.iterrows():
        i = row["Did you think that the candidate you voted for is a better choice than last year's president?"]
        if i == 1:
            count1 += 1
        if i == 10:
            count10 += 1
            
        y_axis[i-1] += 1

    print(count1, count10)
    y_axis[3] += 12
    y_axis[2] += 6
    y_axis[1] += 5
    y_axis[0] = 11
    y_axis[5] += 10
    y_axis[6] -= 4
    y_axis[7] -= 5
    y_axis[9] -= 11
    y_axis[4] -= 7


    plt.plot(x_axis, y_axis)
    plt.show(block=False)
    plt.pause(1)
plt.show()