from faker import Faker

import random


for _ in range(100):
    fk = Faker()
    first_name = fk.first_name()
    last_name = fk.last_name()

    dot = ["",".","_"]
    dt = random.choice(dot)

    emailservice = ["gmail.com","yahoo.com", "hotmail.com","outlook.com", "me.com","icloud.com"]
    es = random.choice(emailservice)

    randnum = random.randint(1,199)
    email = first_name.lower()+dt+last_name.lower()+str(randnum)+"@"+es

    print(email)