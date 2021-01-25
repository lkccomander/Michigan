

def triple(value):
    return 3*value

def tripleStuff(a_list):
    new_seq = map(triple, a_list)
    return list(new_seq)

def quadrupleStuff(a_list):
    new_seq = map(lambda value: 4*value, a_list)
    return list(new_seq)

things = [2, 5, 9]
things3 = tripleStuff(things)
print(things3)
things4 = quadrupleStuff(things)
print(things4)



things = [2, 5, 9]

things4 = map((lambda value: 4*value), things)
print(list(things4))

# or all on one line
print(list(map((lambda value: 5*value), [1, 2, 3])))

things5 = map((lambda value: 7*value),things)
print(list(things5))

# lambda

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

greeting_doubled = map((lambda value: 2*value),lst)

print(greeting_doubled)


abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]

abbrevs_upper = map((lambda values : values.upper()), abbrevs)
print(list(abbrevs_upper))

# https://docs.microsoft.com/en-us/users/cloudskillschallenge/collections/67pku71drej4?WT.mc_id=cloudskillschallenge_8351edfe-a67a-46d4-81cd-6439844b72ac




