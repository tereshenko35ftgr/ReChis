import random as rn
a = rn.randint(1,100)
trye = 1
print("Привет, ты попал в угадай число от 1 до 100. У тебя 10 попыток. Приступай!")
while True:
    u = int(input("Попытка " + str(trye) + ": "))
    trye += 1
    if a == u:
        print("Ты выиграл!")
        break
    elif a <= u:
     print("Загаданное число меньше.")
    elif a >= u:
        print("Загаданное число больше.")
    else:
        print("Не понял.")
    if trye == 11:
        print("Ты истратил все 10 попыток. Загаданное число: " + str(a))
        break
