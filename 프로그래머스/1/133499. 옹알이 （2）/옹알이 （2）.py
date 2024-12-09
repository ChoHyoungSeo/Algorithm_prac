def solution(babbling):
    answer = 0
    basic_sound = ['aya', 'ye', 'woo', 'ma']
    
    for word in babbling:
        prev_word = ''
        current_word = word
        
        while current_word:
            found = False
            for sound in basic_sound:
                if current_word.startswith(sound) and prev_word != sound:
                    prev_word = sound
                    current_word = current_word[len(sound):]
                    found = True
                    break
                    
            if not found:
                break
                
        if not current_word:
            answer += 1
        
    return answer