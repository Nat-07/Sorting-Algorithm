import random

l = []
dupeCheck = 0

# get 1000 non duplicate random values
for i in range(1000):
    dupeCheck = random.randrange(0, 390, 1)
    
    if dupeCheck in l:
        pass
    else:
        l.append(dupeCheck)

# show list prior to sort
print(l)

run = True
while run:
    # run thorugh as many times as elements
    for x in range(len(l)):
        for i in range(len(l)):
            try:
                if l[i] > l[i + 1]:

                    # swap elements
                    l[i],l[i+1] = l[i+1],l[i]

            except IndexError:
                pass

    # stop the while loop
    run = False
    
# show list post sort
print(l)
