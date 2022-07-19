# #딕셔너리로 남아잇는지 아닌지 방법이 있겠고, set을 이용한 방법(퇴근후에는 다시 출근하지 않는다는 가정)
# 가정이 맞지 않는것인가,, 17% error
# a = int(input())
# emp_in = set()
# emp_out = set()

# for i in range(a):
#     name, log = map(str, input().split())
#     if log == "enter":
#         emp_in.add(name)
#     else:
#         emp_out.add(name)

# tmp = sorted(list(emp_in - emp_out), reverse=True)
# for i in range(len(tmp)):
#     print(tmp[i])



#정답
a = int(input())
emp_dict = {}
for _ in range(a):
    name, log = map(str, input().split())

    if log == "enter":
        emp_dict[name] = "enter"
    else:
        del emp_dict[name]

tmp = sorted(emp_dict, reverse=True)
for i in range(len(tmp)):
    print(tmp[i])