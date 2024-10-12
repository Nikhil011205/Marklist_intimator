import pymysql 
import webbrowser as wb
import pyautogui as py 
import time
dm = input("Enter dm/grp : ")
cnx = pymysql.connect(host="localhost",user="root",password="12345",database="work")
cur = cnx.cursor()
qry = "select names,kannada,english,maths,evs from markslist;"
cur.execute(qry)
out1= cur.fetchall()
names = [] ; kannada = [] ; english = [] ; maths = [] ; evs = []
for i in out1 : 
    name,kan,eng,math,ev = i 
    names.append(name)
    kannada.append(kan)
    english.append(eng)
    maths.append(math)
    evs.append(ev)
wb.open('https://web.whatsapp.com/')
time.sleep(10)
py.click(x=180,y=150)
time.sleep(3)
py.typewrite(dm)
time.sleep(2)
py.click(x=143,y=278)
time.sleep(3)
py.click(x=550,y=686)
for i in range(len(names)): 
    py.write(names[i]+ ":")
    py.keyDown('shift')
    py.press('enter')
    py.keyUp('shift')
    if kannada[i] == 0.0 : 
        kan_mar = 'Ab'
    else : 
        kan_mar = kannada[i]
    py.write("  Kannada : "+str(kan_mar))
    py.keyDown('shift')
    py.press('enter')
    py.keyUp('shift')
    if english[i] == 0.0 : 
        eng_mar = 'Ab'
    else : 
        eng_mar = english[i]
    py.write("  English : "+str(eng_mar))
    py.keyDown('shift')
    py.press('enter')
    py.keyUp('shift')
    if maths[i] == 0.0 : 
        math_mar = 'Ab'
    else : 
        math_mar = maths[i]
    py.write("  Mathematics : "+str(math_mar))
    py.keyDown('shift')
    py.press('enter')
    py.keyUp('shift')
    if evs[i] == 0.0 : 
        evs_mar = 'Ab'
    else : 
        evs_mar = evs[i]
    py.write("  EVS : "+str(evs_mar))
    py.press('enter')
    py.click(x=550,y=686)
kan_max = max(kannada) 
kann = kannada.copy()
kan_toppers = []
a = 0
for i in range(kannada.count(kan_max)) : 
    A = kann.index(kan_max)
    kan_toppers.append(names[A+a])
    kann.pop((A))
    a+=1
eng_max = max(english) 
engg = english.copy()
eng_toppers = []
a = 0
for i in range(english.count(eng_max)) : 
    A = engg.index(eng_max) 
    eng_toppers.append(names[A+a])
    engg.pop(A)
    a+=1
evs_max = max(evs) 
evss = evs.copy()
evs_toppers = []
a = 0
for i in range(evs.count(evs_max)) : 
    A = evss.index(evs_max)
    evs_toppers.append(names[A+a])
    evss.pop(A)
    a+=1

math_max = max(maths) 
mathh = maths.copy()
math_toppers = []
a = 0
for i in range(maths.count(math_max)) : 
    A = mathh.index(math_max)
    math_toppers.append(names[A+a])
    mathh.pop(A)
    a+=1
py.click(x=550,y=686)
py.write("kannada toppers : ")
py.keyDown('shift')
py.press('enter')
py.keyUp('shift')
for i in kan_toppers :
    py.write(i+" : "+str(kan_max))
    py.keyDown('shift')
    py.press('enter') 
    py.keyUp('shift')
py.press('enter')
py.click(x=550,y=686)
py.write("English toppers : ")
py.keyDown('shift')
py.press('enter')
py.keyUp('shift')
for i in eng_toppers :
    py.write(i+" : "+str(eng_max)) 
    py.keyDown('shift')
    py.press('enter')
    py.keyUp('shift')
py.press('enter')
py.click(x=550,y=686)
py.write("Maths toppers : ")
py.keyDown('shift')
py.press('enter')
py.keyUp('shift')
for i in math_toppers :
    py.write(i+" : "+str(math_max)) 
    py.keyDown('shift')
    py.press('enter')
    py.keyUp('shift')
py.press('enter')
py.click(x=550,y=686)
py.write("EVS toppers : ")
py.keyDown('shift')
py.press('enter')
py.keyUp('shift')
for i in evs_toppers :
    py.write(i+" : "+str(evs_max)) 
    py.keyDown('shift')
    py.press('enter')
    py.keyUp('shift')
py.press('enter')