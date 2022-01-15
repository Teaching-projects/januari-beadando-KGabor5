import random

def meg_van_e_fejtve(rejtett_szo, tippelt_betuk):
    for betu in rejtett_szo:
        if betu not in tippelt_betuk:
            return False
    return True


def eletek_kiirasa_szimbolumokkal(eletek_szama, max_elet):
    print(" ♥ " * eletek_szama + " 💀 " * (max_elet-eletek_szama))


def feldvany_kiirasa(rejtett_szo, tippelt_betuk):
    for betu in rejtett_szo:
        if betu in tippelt_betuk:
            print(betu, end=" ")
        else:
            print("_", end=" ")
    print()



def jatekallas_kiiras(rejtett_szo, tippelt_betuk, eletek_szama, max_elet):
    eletek_kiirasa_szimbolumokkal(eletek_szama, max_elet)
    feldvany_kiirasa(rejtett_szo, tippelt_betuk)

def veletlenszeru_feladvany(szolista):
    return random.choice(szolista)


szolista=[]
with open ("szavak.txt") as file:
    for sor in file:
        szolista.append(sor.strip())


feladvany = veletlenszeru_feladvany(szolista) 
eletszam=int(input("Hány élettel szeretnél játszani(max 10 élet):"))
eletek=eletszam
max=eletek
tippek=[]

print("""
   X     X X      X     XXXXX XXXXXX XXXXXXX XXXXXXX XXXX    X
  X X    XX      X X    XX       X      X    X     X X      X X
 XXXXX   X X    XXXXX      XX   X       X    X     X XXX   XXXXX
X     X  X  x  X     X XXXXX  XXXXXX    X    XXXXXXX X    X     X
""")


while not meg_van_e_fejtve(feladvany,tippek) and eletek > 0: 
    jatekallas_kiiras(feladvany,tippek,eletek,max)
    uj=input("Adj meg egy betut (csak ékezet néküli betűket írj!): ")
    if uj not in feladvany:
        eletek-=1

    if not uj in tippek:
        tippek.append(uj)
    else:
        print("Ez a betű már volt")


    # 9 eletnel
    if eletek==9:
        print("XXXXXXX")

    # 8 eletnel
    if eletek==8:
        print("""
            X
            X
            X
            X
            X
         XXXXXXX""")

    # 7 eletnel
    if eletek==7:
        print("""
      XXXXXXX
            X
            X
            X
            X
         XXXXXXX""")

    # 6 eletnel
    if eletek==6:
        print("""
      XXXXXXX
           XX
            X
            X
            X
         XXXXXXX""")

    # 5 eletnel
    if eletek==5:
        print("""
      XXXXXXX
      I    XX
            X
            X
            X
         XXXXXXX""")


    # 4 eletnel
    if eletek==4:
        print("""
      XXXXXXX
      I    XX
      O     X
            X
            X
         XXXXXXX""")

    # 3 eletnel
    if eletek==3:
        print("""
      XXXXXXX
      I    XX
      O     X
      I     X
            X
         XXXXXXX""")
    
    # 2 eletnel
    if eletek==2:
        print("""
      XXXXXXX
      I    XX
      O     X
      I     X
      ^     X
         XXXXXXX""")
    
    # 1 eletnel
    if eletek==1:
        print("""
      XXXXXXX
      I    XX
      O     X
     /I     X
      ^     X
         XXXXXXX""")
    
 
if eletek > 0:
    jatekallas_kiiras(feladvany,tippek,eletek,max)
    print("GRATULALOK, megfejtetted! 🎉🎉🎉") 
else:
    print("""
      XXXXXXX
      I    XX
      O     X
     /I\    X
      ^     X
         XXXXXXX""")

    print("VESZTETTÉL! 😭😭😭 VÉGE A JÁTÉKNAK", feladvany ,"volt a szó!")
