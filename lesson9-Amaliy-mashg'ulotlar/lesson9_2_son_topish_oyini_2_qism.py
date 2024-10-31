import random as R

def find_number(n):
    
    number = R.randint(1, n)
    while True:
        question = f"1 dan {n} gacha son o'yladim topa olasizmi?\n>>>"
        answer = int(input(question))
        if answer < number:
            print("Xato, men o'ylagan son bundan kattaroq. Yana harakat qiling:\n>>>")
            
        elif answer > number:
            print("Xato, men o'ylagan son bundan kichikroq. Yana harakat qiling:\n>>>")
            
        elif answer == number:
            print("Topdingiz! {answer} sonini o'ylagan edim.")
            break
    return answer
            
def find_number_pc(x):
    
    lower = 1
    upper = x
    
    print(f"1 dan {x} gacha son o'ylang. Men topishga harakat qilib ko'raman!")
    while True:
        
        number2 = R.randint(lower, upper)
    
        answer1 = input(f"Siz {number2} sonini o'yladingiz: to'g'ri (T), kattaroq (+), kichikroq (-)??\n>>> ").strip()
        
        if answer1 == "T":
            print(f"Topdim! Siz o'ylagan son {number2}")
            break
        elif answer1 == "+":
            lower = number2 + 1
        elif answer1 == "-":
            upper = number2 - 1
        else:
            print("Iltimos, faqat 'T', '+' yoki '-' javobini kiriting.")
            
    return number2
            
        
        
    