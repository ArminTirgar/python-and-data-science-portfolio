def minion_game(input_string):
    possible_vowels_list = []
    possible_constant_list = []
    
    for i in range(len(input_string)):
        if input_string[i] in ('A', 'E', 'I', 'O', 'U'):
            for j in range(i+1,len(input_string)+1):
                possible_vowels_list.append(input_string[i:j])
        else:
            for j in range(i+1,len(input_string)+1):
                possible_constant_list.append(input_string[i:j])
                
    if len(possible_constant_list)>len(possible_vowels_list):
        print("Stuart",len(possible_constant_list))
    else:
        print("Kevin",len(possible_vowels_list))
    

minion_game(input())


def minion_game(input_string):
    Stuart_score = 0
    Kevin_score = 0
    
    for i in range(input_string):
        if input_string[i] in "AEIOU":
            Kevin_score += len(input_string) - i
        else:
            Stuart_score += len(input_string) - i
        
        
    if Stuart_score > Kevin_score
        print("Stuart", Stuart_score)
    elif Kevin_score > Stuart_score:
        print("Kevin", Kevin_score)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)