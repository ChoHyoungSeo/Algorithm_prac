def solution(arr):
    target = min(arr)
    del arr[arr.index(target)]
    if arr:
        return arr
    else:
        return [-1]