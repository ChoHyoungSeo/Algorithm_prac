def solution(sizes):
    max_width = max(max(size) for size in sizes)
    max_height = max(min(size) for size in sizes)
    
    return max_width * max_height