"""Remove all duplicate items in list
input:
old_list = [{'key1':'value1'},{},{},{'key1':'value1'},{'key2':'value2'}]
output:
new_list = [{'key1':'value1'},{},{'key2':'value2'}]
"""
x = [{'key1':'value1'},{},{},{'key1':'value1'},{'key2':'value2'}]
y = []
for i in x:
    if x.count(i)>1:
        y.append(i)
        x.remove(i)
    else:
        y.append(i)
        print(y)
