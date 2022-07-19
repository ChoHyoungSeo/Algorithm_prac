def solution(array, commands):
    answer = []
    for n_commands in commands:
        n_array = array[n_commands[0]-1:n_commands[1]]
        n_array.sort()
        answer.append(n_array[n_commands[2]-1])
    return answer