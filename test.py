

# width, height = 10, 10

# for 0~2
# for 1~2 -> 0,2 -> 0~1
# if x - x <= 10 and y - y <= 10 
# x_1 = max(x)
# x_2 = min(x) +10
# y_1 = max(y)
# y_2 = min(y) + 10
# answer = (x_2 - x_1)*(y_2 - y_1)

t = 3
location_list =[[3, 7],[15, 7],[5, 2]]


t=int(input())
location_list = [list(map(int, input().split())) for _ in range(t)]

answer = len(location_list)*100
for i in range(t) :
    for j in range(i + 1, t):  # i를 제외하고 중복 계산 방지
            if abs(location_list[i][0] - location_list[j][0]) <= 10 and abs(location_list[i][1] - location_list[j][1]) <= 10 :
                  x_1 = max(location_list[i][0], location_list[j][0])
                  x_2 = min(location_list[i][0], location_list[j][0]) + 10
                  y_1 = max(location_list[i][1], location_list[j][1])
                  y_2 = min(location_list[i][1], location_list[j][1]) + 10
                  answer -= (x_2 - x_1)*(y_2 - y_1)
            pass
print(answer)





