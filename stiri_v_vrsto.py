ZMAGA_PLAVI = "pl"
ZMAGA_ORANZNI ="or"
IZENACENO ="iz"
NAPREJ = "NAP"
ZACETEK = "zac"



class Igra():
    def __init__(self):
        self.stanje = ZACETEK
        self.stevec = 0
        self.matrika = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

    def ali_je_stiri_v_vrsto(self):
        matrika = self.matrika
        for vrstica in matrika:
            for i in range(0, 4):
                if vrstica[i] != 0  and vrstica[i] == vrstica[i+1] == vrstica[i+2] == vrstica[i+3]:
                    return True
        for j in range(0, 3):
            for i in range(0, 7):
                if  matrika[j][i]  != 0 and matrika[j][i] == matrika[j+1][i] == matrika[j+2][i] == matrika[j+3][i]:
                    return True
        for j in range(0, 4):
            for i in range(0, 3):
                if matrika[i][j] != 0 and matrika[i][j]== matrika[i+1][j+1]== matrika[i+2][j+2] == matrika[i+3][j+3]:
                    return True
        for j in range(0, 4):
            for i in range(0, 3):
                if matrika[i][6-j] != 0 and matrika[i][6-j]== matrika[i+1][5-j]== matrika[i+2][4-j] == matrika[i+3][3-j]:
                    return True
        else:
            return False
    
    def ali_je_izenaceno(self):
        vsota = 0
        for vrstica in self.matrika:
            vsotka = 0
            for stevilka in vrstica:
                vsotka += stevilka
            vsota += vsotka
        if vsota ==63:
            return True
        else:
            return False


    def potek(self,n):
        self.stevec
        stevec = 0
        matrika = self.matrika
        if self.ali_je_stiri_v_vrsto() == True:
            stevec =6
        if stevec != 6:
            while matrika[stevec][n] != 0:
                stevec += 1
                if stevec >= 6:
                    break
        if stevec < 6:
            matrika[stevec][n] = ((self.stevec) % 2 + 1)
            self.stevec += 1
        # if krog % 2 == 1:
        #     barva = "O"
        # else:
        #     barva = "R"
        # platno.create_oval(2 + 90*n , 2 + 90 * (5-stevec), 92+ 90*n, 92 + 90 * (5-stevec), fill = barva)
        if self.ali_je_stiri_v_vrsto() == True:
            if self.stevec % 2 == 0:
                self.stanje = ZMAGA_PLAVI
                return ZMAGA_PLAVI
            else:
                self.stanje = ZMAGA_ORANZNI
                return ZMAGA_ORANZNI
        if self.ali_je_izenaceno()== True:
            self.stanje = IZENACENO
            return IZENACENO
        self.stanje = NAPREJ
        #  platno.create_text(321,272,font = "Arial 27", activefill="orange",fill="black",text="It's a Draw,click Restart to play again!")
        return NAPREJ   
    def nova_igra(self):
        self.stanje = ZACETEK
        self.stevec = 0
        self.matrika = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
        
    #print(krog)
    #print(matrika)
    #print(stevec)








        
