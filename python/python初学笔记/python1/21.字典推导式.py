counts = {'MBP':268,'HP':125,'DELL':201,'lenovo':199,'acer':99}
dict1 = {value:  value for key,value in counts.items()  if value>= 200}
print(dict1)