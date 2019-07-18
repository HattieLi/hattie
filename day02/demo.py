
f = open('test','w+')

f.write('hello world')
f.flush()

data = f.read()

print(data)

f.close()