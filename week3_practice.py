

abrv = ['cr77','f66t','fggf','agga','fggf','gffg','rggr','rgggr','rrgg','ggrr']
#new_lst = []


def transformer(st):
    return st.upper()

new_lst = map(transformer,abrv)
new_lst = map(lambda abrv: abrv[:2].upper(),abrv)
print(new_lst)
print(list(new_lst))
