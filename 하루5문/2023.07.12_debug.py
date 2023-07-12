# 1번 문제
# def solution(n):
#     answer = 0
#     sol = 0
#     index = 0
#     for i in range(1, n+1):
#         if n == 1:
#             index = 1
#             break
#         try:
#             sol = i
#             if sol == n:
#                 index+=1
#                 break
#             for j in range(i+1, n+1):
#                 sol += j
#                 if(sol > n):
#                     sol = 0
#                     break
#                 elif(sol == n):
#                     index += 1
#                     sol = 0
#                     break
#                 else:
#                     continue
#         except:
#             answer = 1
#     answer = index
#     return answer
#
# print(solution(2))
# print(solution(3))
# print(solution(4))
# print(solution(5))
# print(solution(6))
# print(solution(7))
# print(solution(8))
# print(solution(9))
# print(solution(10))

# 2번 문제 ="(())()"
# def solution(s):
#     answer = True
#     stack = []
#     for i in s:
#         if i == "(":
#             stack.append(i)
#         elif stack.pop() != "(" or None:
#             return False
#     if stack:
#         return False
#     else:
#         return True
#
# print(solution("(()((()(())))())"))

# if stack : 스택이 비어있지 않다면
# if not stack : 스택이 비어있다면

# 몇 번이더라

food = [1, 3, 4, 6]

answer = ''

i = 0
while i < len(food):
    if i == 0:
        answer += str(i)
        i+=1
        continue
    answer = str(i) * (food[i]//2) + answer + str(i) * (food[i]//2)
    i+=1
print(answer)







































