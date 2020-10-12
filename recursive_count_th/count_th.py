'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    def check_th_rec(str_input):
        if 'th' not in str_input:
            return

        nonlocal count
        count += 1
        str_input = str_input[str_input.find('th')+1:]
        check_th_rec(str_input)
    check_th_rec(word)
    return count