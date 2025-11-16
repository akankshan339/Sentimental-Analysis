#to remove puncation marks from a string
#[my,name -is = akanksha's !negi`s}>
st=input("Enter any string containing puncation marks: ")
punc='''\!@#$%^&*()_+-=~`;""<>,./?:{}[]|'''
newst=""
for ch in st:
    if ch not in punc:
        newst=newst+ch
print(newst)

