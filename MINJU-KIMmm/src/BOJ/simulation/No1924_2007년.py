Day = 0
arrList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekList = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

x, y = map(int, input().split())

for i in range(x - 1):
    Day = Day + arrList[i]
Day = (Day + y) % 7

print(weekList[Day])
# date = ['MON', 'TUE', 'WED', "THU", 'FRI', 'SAT', 'SUN']

# first = [3, 0, 2, 3, 3, 2, 3, 3, 2, 3, 2, 3]
#
# #x, y = map(int, input().split())
#
# def calc(x,y):
#
#     start = 0
#
#     if x>1:
#         for month in range(1, x):
#             start = (start+first[month-1])%7
#
#         day = (y-1)%7
#         print(date[(start+day)%7], end=' ')
#         return date[(start+day)%7]
#     else:
#         day = (y-1)%7
#         print(date[(start+day)%7], end=' ')
#         return date[(start + day) % 7]
#
#
# for i in range(1, 13):
#     print(i)
#     if first[i-1]==3:
#         for j in range(1, 32):
#             if(calc(i, j)=='SUN'):
#                 print()
#
#     elif first[i-1]==2:
#         for j in range(1, 31):
#             if(calc(i, j)=='SUN'):
#                 print()
#     else:
#         for j in range(1, 29):
#             if(calc(i, j)=='SUN'):
#                 print()