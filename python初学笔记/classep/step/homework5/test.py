import random
def random_index(rate):
    start = 0
    index = 0
    randnum = random.randint(1,sum(rate))
    for index,scope in enumerate(rate):
        start += scope
        if randnum <= start:
            break
    return index
a = random_index([10,90])
print(a)