def perm_gen_lex(string_input):
    """ Takes an input string that consists 0 or more unique
        lower-case letters in alphabetical order and returns
        a list containing all possible permutations of the
        input string in lexicographic order.
    """
    perms = [] #list to store all permutations

    if len(string_input) == 0: # for if the string is empty
        return perms

    elif len(string_input) == 1: # returns base case of 1 character as a list
        perms.append(string_input)
        return perms
        
    else:
        for idx,letter in enumerate(string_input): #iterates through each character in the input string
            temp = '' # variable for shortened string
            
            for val in string_input:
                if val != letter: # adds all letters that aren't the letter intended to be removed to temp string
                    temp += val 

            cur_perms = perm_gen_lex(temp) #recursive step: input is new shrotened string

            for i in range(len(cur_perms)): #length of cur_perms determines how many permutations require the addition of removed character
                perms.append(letter + ''.join(cur_perms[i])) # adds removed character to each item in cur_perms list and appends to perms list

        return perms









