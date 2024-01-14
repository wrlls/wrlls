from victory import victory_game

print("ZDAROVO")
print("KAK TEBYA ZOVUT")
user_name = input()
print("GOTOV LI TI(yes or no)")
user_answer = input()
if user_answer=="yes":
    print("pognali")
elif user_answer=="no":
    print("poshel nahutor")
else:
    print("UDALI SERVIS")
while user_answer == "yes":
    victory_game()