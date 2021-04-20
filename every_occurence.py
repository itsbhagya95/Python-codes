##Index of every occurence of a substring
d='ABCABCZZZZABCAB'
subs=input('Enter a substring to search')
i=d.find(subs)
ct=0
if i==-1:
    print('Substring not found')
while i!=-1:
    ct+=1
    print('{} is present at index {}'.format(subs,i))
    i=d.find(subs,i+len(subs),len(d))
print('Count is :',d.count(subs))