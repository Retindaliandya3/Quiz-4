listGPA = [2.1, 2.5, 4, 3]

def hadiah (GPA):
    Bonus = 500000
    hadiah = GPA * Bonus
    return hadiah

for GPA in listGPA:
    if GPA > 2.5:
        print("Selamat! Anda mendapatkan bonus : Rp", hadiah(GPA))
    else :
        print("Maaf, Tidak ada Bonus")