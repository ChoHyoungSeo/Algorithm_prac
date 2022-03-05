#11723
import sys

def add(S: set, num: int) -> None:
    if num not in S:
        S.add(num)

def remove(S: set, num: int) -> None:
    if num in S:
        S.remove(num)

def check(S:set, num:int) -> int:
    if num in S:
        print(1)
    else:
        print(0)
       
def toggle(S:set, num:int) -> None:
    if num in S:
        remove(S, num)
    else:
        add(S, num)
       
def all() -> set:
    S = {x for x in range(1,21)}
    return S
   
def empty() -> set:
    S = set()
    return S
   
if __name__ == '__main__':
    tot = int(sys.stdin.readline().strip())
    S = set()
   
    for i in range(tot):
        command = list(sys.stdin.readline().strip().split())
       
        if len(command) == 1:
            com = str(command[0])
           
        else:
            com, num = str(command[0]), int(command[1])
        if com == "empty":
            S = empty()
        elif com == "all":
            S = all()
        elif com == "add":
            add(S, num)
        elif com == "remove":
            remove(S, num)
        elif com == "check":
            check(S, num)
        else:
            toggle(S, num)