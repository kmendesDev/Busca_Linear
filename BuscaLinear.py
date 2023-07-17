import random
random_list=random.sample(range(1000),100)
print(random_list)
number = int(input("Digite o numero procurado: "))
i=0
while i<len(random_list):
    if random_list[i] == number:
        print("Seu número foi encontrado na posição "+str(i+1) )
        break
    elif i == (len(random_list)-1):
        print("-1")
    i+=1