#!/usr/bin/python3
# -*- coding: utf-8 -*-
from fastapi import FastAPI, HTTPException, Response
import uvicorn

app = FastAPI()
book1 = """Kak veshnij den', tvoj lik prisnilsya snova, —
Znakomuyu privetstvuyu krasu,
I po volnam laskayushchego slova
YA obraz tvoj prelestnyj ponesu.
Somnenij net, neyasnoj net pechali,
Vsyo vyskazat' vo sne umeyu ya,
I mchit da mchit vsyo dalee i dale
S toboyu nas vozdushnaya lad'ya.
Pered toboj s kolenopreklonen'em
Stoyu, plenen volshebnoyu igroj,
A za toboj — koleblemyj dvizhen'em,
Neyasnyh zvukov otstayushchij roj."""

book2 = """Vot zastava — skoro k domu,
Slava bogu, nalegke!
Moj privet Kremlyu rodnomu,
Moj privet Moskve-reke! Ne uvizhu li, ne vstrechu l'
Golubyh ee ochej?
Dogadayus' li, zamechu l'
Po siyan'yu ih luchej
Dolgoj tajny neterpen'e,
Plamen' v devstvennoj krovi,
Vozrozhden'e, upoen'e
I doverchivost' lyubvi?"""

book3 = """CHernuyu urchu s prahom poeta
Plyushch obognul;
K broshennoj arfe devstvennyj poyas
Krepko pril'nul.Fakel ugasshij podle papira
Vechnogo spit;
Garpiya-zavist', kryl'ya raskinuv,
V prahe lezhit.No za Kocitom ty ulybnesh'sya,
Divnyj pevec;
K urne prizhalsya dar Apollona —
Svezhij venec!"""

book4 = """Pustynnaya YAjla dymitsya oblakami,
V tumannyj nebosklon ushla morskaya dal',
SHumit vnizu priboj, zaliv kipit volnami,
A zdes' — glubokij son i vechnaya pechal'.
Pust' v gorode zhivyh, u sinego zaliva,
Gremit i bleshchet zhizn'... Zadumchivoj tolpoj
Zdes' kiparisy zhdut — i strogo, molchalivo
Voskhodit Smert' syuda s dobychej rokovoj.
ZHizn' ne smushchaet ih, minutnaya, dnevnaya...
Lish' tol'ko kolokol vechernij s beregov
Pereklikaetsya, zvenya i zavyvaya,
S mogil'noj strazheyu beleyushchih krestov."""

book5 = """Svechi nagoreli, dolog zimnij vecher…
Sel ty na lezhanku, podnyal tihij vzglyad —
I zvuchit gitara udal'yu pechal'noj
Pesne bezzabotnoj, staroj pesne v lad.«Gde ty zakatilos', schast'e zolotoe?
Kto tebya razveyal po chistym polyam?
Ne vzojti nad step'yu solnyshku s zakata,
Net puti-dorogi k nevozvratnym dnyam!»Svechi nagoreli, dolog zimnij vecher…
Brovi ty pripodnyal, grusten tihij vzglyad…
Ne sud'ya tebe ya za grekhi bylogo!
Ne vorotish' zhizni prozhitoj nazad!"""

book6 = """Stemnelo.   Vdol'   allej,   nad   sonnymi   prudami,
Bredu ya naugad.
Osennej svezhest'yu, listvoyu i plodami
Blagouhaet sad.
Davno on poredel, - i zvezdnoe siyan'e
Beleet mezh vetvej.
Idu ya medlenno, - i mertvoe molchan'e
Carit vo t'me allej.
I   zvonok   kazhdyj   shag   sredi   nochnoj   prohlady.
I carstvennym gerbom
Goryat holodnye almaznye Pleyady
V bezmolvii nochnom."""

book7 = """V dveryah edema angel nezhnyj
Glavoj poniksheyu siyal,
A demon mrachnyj i myatezhnyj
Nad adskoj bezdnoyu letal.
Duh otrican'ya, duh somnen'ya
Na duha chistogo vziral
I zhar nevol'nyj umilen'ya
Vpervye smutno poznaval.
"Prosti, - on rek, - tebya ya videl,
I ty nedarom mne siyal:
Ne vse ya v nebe nenavidel,
Ne vse ya v mire preziral"."""

book8 = """Ty videl devu na skale
V odezhde beloj nad volnami
Kogda, bushuya v burnoj mgle,
Igralo more s beregami,
Kogda luch molnij ozaryal
Ee vsechasno bleskom alym
I veter bilsya i letal
S ee letuchim pokryvalom?
Prekrasno more v burnoj mgle
I nebo v bleskah bez lazuri;
No ver' mne: deva na skale
Prekrasnej voln, nebes i buri."""

book9 = """Morfej, do utra daj otradu
Moej muchitel'noj lyubvi.
Pridi, zaduj moyu lampadu,
Moi mechty blagoslovi!
Sokroj ot pamyati unyloj
Razluki strashnyj prigovor!
Puskaj uvizhu milyj vzor,
Puskaj uslyshu golos milyj.
Kogda zh umchitsya nochi mgla
I ty moi pokinesh' ochi,
O, esli by dusha mogla
Zabyt' lyubov' do novoj nochi!"""

@app.get("/library")
def library_page():
    """<<START PAGE>>"""
    return "А.А.Фет; И.Бунин; А.С.Пушкин"

@app.get("/library/{author}")
def library_author(author):
    if author == "А.А.Фет":
        return "Во_cне; Возвращение; Арабеск"
    if author == "И.Бунин":
        return "Кипарисы; На_хуторе; Плеяды"
    if author == "А.С.Пушкин":
        return "Ангел; Буря; К Морфею"
    else:
        raise HTTPException(status_code=404, detail="such author exists")
    
@app.get("/library/{author}/{book}")
def library_author_book(author,book,begin: str = None, end:str = None):
    if author == "А.А.Фет":
        if book == "Во_сне":
            if begin != None:
                begin = book1.find(begin)
            if end != None:
                end = book1.find(end)
            if begin == None:
                begin = 0;
            if end == None:
                end = -1
            if begin == -1:
                begin = 0
            return Response(book1[begin:end])
        if book == "Возвращение":
            if begin != None:
                begin = book2.find(begin)
            if end != None:
                end = book2.find(end)
            if begin == None:
                begin = 0;
            if end == None:
                end = -1
            if begin == -1:
                begin = 0            
            return Response(book2[begin:end])
        if book == "Арабеск":
            if begin != None:
                begin = book3.find(begin)
            if end != None:
                end = book3.find(end)
            if begin == None:
                begin = 0;
            if end == None:
                end = -1
            if begin == -1:
                begin = 0            
            return Response(book3[begin:end])
        else:
            raise HTTPException(status_code=404, detail="no such book exists")
    if author == "И.Бунин":
        if book == "Кипарисы":
            if begin != None:
                begin = book4.find(begin)
            if end != None:
                end = book4.find(end)
            if begin == None:
                begin = 0;
            if end == None:
                end = -1
            if begin == -1:
                begin = 0            
            return Response(book4[begin:end])
        if book == "На_хуторе":
            if begin != None:
                begin = book5.find(begin)
            if end != None:
                end = book5.find(end)
            if begin == None:
                begin = 0;
            if end == None:
                end = -1
            if begin == -1:
                begin = 0            
            return Response(book5[begin:end])
        if book == "Плеяды":
            if begin != None:
                begin = book6.find(begin)
            if end != None:
                end = book6.find(end)
            if begin == None:
                begin = 0;
            if end == None:
                end = -1
            if begin == -1:
                begin = 0            
            return Response(book6[begin:end])
        else:
            raise HTTPException(status_code=404, detail="no such book exists")
    if author == "А.С.Пушкин":
        if book == "Ангел":
            if begin != None:
                begin = book7.find(begin)
            if end != None:
                end = book7.find(end)
            if begin == None:
                begin = 0;
            if end == None:
                end = -1
            if begin == -1:
                begin = 0            
            return Response(book7[begin:end])
        if book == "Буря":
            if begin != None:
                begin = book8.find(begin)
            if end != None:
                end = book8.find(end)
            if begin == None:
                begin = 0;
            if end == None:
                end = -1
            if begin == -1:
                begin = 0            
            return Response(book8[begin:end])
        if book == "К_Морфею":
            if begin != None:
                begin = book9.find(begin)
            if end != None:
                end = book9.find(end)
            if begin == None:
                begin = 0;
            if end == None:
                end = -1
            if begin == -1:
                begin = 0            
            return Response(book9[begin:end])
        else:
            raise HTTPException(status_code=404, detail="no such book exists")
    else:
        raise HTTPException(status_code=404, detail="such author exists")  
if __name__ == "__main__":
    uvicorn.run(app)