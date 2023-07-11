# 1번 문제.
# n = 1234
# answer = []
#
# i = 1
# while i <= len(str(n)):
#     temp = n % pow(10, i)
#     answer.append(int(str(temp)[0]))
#     n = n - temp
#     i += 1
#
# print(answer)

# 2번 문제
# 문자열 s를 숫자로 변환한 결과를 반환하는 함수 solution을 만들어보자.
# s는 1 - 5자리 문자열.
# 맨 앞에는 부호가 올 수 있다.
# 부호 + 숫자로 이뤄져 있다.
# s는 0으로 시작하지 않는다.

# n = "1234"
# answer = 0
#
# if(n[0] == "+"):
#     answer = int(n[1:])
# elif(n[0] == "-"):
#     answer = int(n[1:]) - 2*int(n[1:])
# else:
#     answer = int(n[:])
#
# print(answer)

# 3번 문제
# 정수 a, b가 주어졌을 때 a ~ b까지의 합을 return한다.
# a가 b보다 클 수도, 작을 수도 있다.

# a = 3
# b = 7
#
# answer = 0
# if(a - b > 0):
#     i = b
#     while i <= a:
#         answer += i
#         i+=1
# elif(a - b == 0):
#     answer = 0
# else:
#     i = a
#     while i <= b:
#         answer += i
#         i+=1
# print(answer)

# 4번 문제
# 의 각 자리수를 큰것부터 작은 순으로 정렬하여 새로운 정수로 return 하라.
# 뭔가... 뭔가다... HelloWorld식으로 코드 작성하고 감탄할 준비 완료.

#2중 for문으로 쉽게 구할 수 있을 것 같긴 한데, 그걸 원하는 문제일까.

# def solution(n):
#     answer = 0
#     temp = str(n)
#     tempArr = []
#     for i in range(0, len(temp)):
#         tempArr.append(temp[i])
#     tempArr.sort(reverse=True)
#     tmp=""
#     for i in range(0, len(tempArr)):
#         tmp += tempArr[i]
#     answer = int(tmp)
#     return answer

# 5번 문제

# def solution(s):
#     answer = True
#     tmp = list(s)
#     if(len(tmp) != 4 and len(tmp) != 6):
#         answer = False
#         return answer
#     for i in range(0, len(tmp)):
#         try:
#             tmp[i] = int(tmp[i])
#         except:
#             answer = False
#             return answer
#     return answer
#
# print(solution("5524"))

# 6번 문제

# price = 3
# money = 20
# count = 4
#
# answer = -1
#
# for i in range(0, count):
#     if(price * (i+1) > money):
#         answer = money
#         break
#     money -= price * (i+1)
# print(money)

# 7번 문제
# 문자열 s에 나타나는 문자를 큰 것부터 작은 것으로. 대문자는 소문자보다 작은 것으로 간주한다.
# ASCII 코드 사용하는 문제인 것으로 보인다.

# s = "Zbcdefg"
#
# newArr = list(s)


# 8번 문제

# answer = [[]]
#
# arr1 = [[1,2],[2,3]]
# arr2 = [[3,4],[5,6]]
#
# for i in range(0, len(arr1)):
#     for j in range(0, len(arr1[0])):
#         answer[i][j].append(arr1[i][j]+arr2[i][j])

# Debugging

# def solution(brown, yellow):
#     answer = []
#     newArr = []
#     for i in range(yellow):
#         if yellow%(i+1)==0:
#             newArr.append(i+1)
#     newArr.sort(reverse=True)
#     temp = len(newArr)
#     if(yellow == 1):
#         answer = [3, 3]
#         return answer
#     for i in range(temp):
#         if i+1<temp:
#             for j in range(i+1, temp):
#                 if (newArr[i]*newArr[j]==yellow and 2*(newArr[i]+newArr[j]+2)==brown):
#                     answer.append(newArr[i]+2)
#                     answer.append(newArr[j]+2)
#     return answer
#
# print(solution(8, 1))

# n = 5000
#
# index = 0
# for i in range(0, n):
#     if n % 2 != 0:
#         n -= 1
#         index += 1
#     n = n // 2
#     if n == 1:
#         index+=1
#         break
# print(index)

# s = "3people unFollowed me"
# sol = list(s)
#
# index = 0
# targetStd = " "
# for i in range(len(sol)):
#     if index == 0:
#         sol[i] = sol[i].upper()
#         index+=1
#         continue
#     sol[i] = sol[i].lower()
#     index+=1
#     if sol[i] == targetStd:
#         index = 0
#         continue
# print(''.join(sol))






















