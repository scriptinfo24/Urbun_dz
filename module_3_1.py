calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(n):
    count_calls()
    my_set = (n)
    string_inf = ()
    kolvo = len(my_set)
    litl= my_set.lower()
    up = my_set.upper()
    string_inf = (kolvo, up, litl)

    return string_inf

def is_contains(n, list_to_search):
    count_calls()
    for n in [n.lower() in list_to_search]:
        if list_to_search == n:
            print('TRUE')
        else:
            print('FALSE')



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)