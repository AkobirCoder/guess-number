import random

def sontop(x):
    
    tasodifiy_son = random.randint(1, x)
    _taxminlar_ = 0
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?")
    
    while True:
        
        _taxminlar_ += 1
        _taxmin_ = input("\n>>>")
        _taxmin_ = int(_taxmin_)
        
        if _taxmin_ < tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kattaroq. Yana harakat qiling:")
            
        elif _taxmin_ > tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kichikroq. Yana harakat qiling:")
            
        else:
            break
    
    print(f"Tabriklaymiz. {_taxminlar_} ta taxmin bilan topdingiz!!!\n")
    return _taxminlar_
    

def sontop_pc(x):
    
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
    
    upper_taxmin = x
    lower_taxmin = 1
    _taxminlar_ = 0
    
    while True:
        
        _taxminlar_ += 1
        
        if upper_taxmin != lower_taxmin:
            _taxmin_ = random.randint(lower_taxmin, upper_taxmin)
        
        else:
            _taxmin_ = lower_taxmin
            
        question = f"Siz {_taxmin_} sonini o'yladingiz: to'g'ri (T), men o'ylagan son bundan kattaroq (+), yoki kichikroq(-): "
        answer = input(question)
        
        if answer == 'T':
            print(f"Topdim, siz o'ylagan son {_taxmin_}!")
            break
        
        elif answer == '+':
            lower_taxmin = _taxmin_ + 1
            
        elif answer == '-':
            upper_taxmin = _taxmin_ - 1
            
        else:
            print("Iltimos, faqat 'T', '+' yoki '-' javobini kiriting.")
            
    print(f"Topdim, {_taxminlar_} ta taxmin bilan! Siz o'ylagan son {_taxmin_}!!!")
    return _taxminlar_
      

def play(x):
    
    javob = True
    
    while javob:
        
        _taxminlar__user = sontop(x)
        _taxminlar__pc = sontop_pc(x)
        
        if _taxminlar__user > _taxminlar__pc:
            print(f"Men {_taxminlar__pc} ta taxmin bilan yutdim!!!")
        
        elif _taxminlar__user < _taxminlar__pc:
            print(f"Siz {_taxminlar__user} ta taxmin bilan yutdingiz!!!")
        else:
            print("Durrang!!!")
            
        savol = "\nYana o'ynaysizmi? (yes(1) / no(0)) "
        javob = int(input(savol))
        
        # if javob != 1:
        #     javob = False
    
