
#1

#campiled - dasturlash tilida birinchi hamma kodni kampiyuter tiliga o'tqizadi va tezroq ishlidi 
# keyin run bo'ladi. ularga c, c++ kiradi 
#Interpreted - dasturlash tillari esa kodni bajarish jarayonida, 
#ya'ni har bir buyruq bajarilganda, 
# kodini o'qiydi va bajaradi, bu tilarga py, ruby, javascriptlar kiradi, 
# campiled tilar Interpreted tilardan tezroq ishlaydi.

#2

#pythonda 8 ta maluot turlari mavjud.
#1. Integer (int) - Butun sonlar, masalan:  5 ,  -3 ,  42 . 
#2. Float (float) - O'nlik sonlar, masalan:  3.14 ,  -0.001 ,  2.0 . 
#3. String (str) - Matnlar, masalan:  "Hello, World!" . 
#4. Boolean (bool) - Mantiqiy qiymatlar,  True  yoki  False . 
#5. List - Ro'yxatlar, bir nechta elementlarni saqlash imkonini beradi, masalan:  [1, 2, 3] ,  ['apple', 'banana', 'cherry'] . 
#6. Tuple - O'zgarmas ro'yxatlar, masalan:  (1, 2, 3) ,  ('a', 'b', 'c') . 
#7. Set - Takrorlanmaydigan elementlar to'plami, masalan:  {1, 2, 3} ,  {'apple', 'banana'} . 
#8. Dictionary (dict) - Kalit-qiymat juftliklari, masalan:  {'name': 'bekzod', 'age': 15} 

#3.
#tuple - o'zgarmaslik. Tartibli, o'zgarmas  elementlar to'plami.
# list - tartabli, va uni qiymatlarni o'zgartsa bo'ladi 
# set - tartibsiz. elmentlar to'plami , va 1 ta qiymatni 2 marta olmaydi 
# dictionary - kalit so'z orqali qiymatlarni olish mumkin


#4 

#iterative , raqamlar yig'indisi
def iterative(n):
    result = 0
    for i in range(0, n + 1, 1):
        result += i
    return result

print(iterative(2)) 

#recusive faktarial
def recursive(n):
    if n == 1:
        return 1
    else:
        return n * recursive(n - 1)
print(recursive(5))
#lambda funksiya , kvadrat chiqarish 
kvadrat = lambda x: x ** 2
print(kvadrat(3))  

#5 
def qosh(a, b):
    try:
        natija = a / b
    except TypeError:
        print("Xatolik: raqam kiriting! (exception)")
    else:
        print(f"Natija: {natija}")


qosh(10, 2)  # Natija: 12
qosh(10, 'a')  # Xatolik: raqam kiritish kereak bu exception!

#6

# Faylga 
with open('example.txt', 'w') as file:
    file.write('Salom, dunyo!')


with open('example.txt', 'r') as file:
    content = file.read()
    print("fili ishladi")
#json
import json

data = {
    "ism": "Ali",
    "yosh": 25,
    "shahar": "Toshkent"
}

with open('data.json', 'w') as json_file:
    json.dump(data, json_file)


with open('data.json', 'r') as json_file:
    loaded_data = json.load(json_file)
    print(loaded_data)
    
#7 

import json
from abc import ABC, abstractmethod

class Telefon(ABC):
    def __init__(self, brendi, modeli, narxi, tezkor_xotira_hajmi):
        self.__id = id(self)  # unique identifier
        self._narxi = narxi    # protected attribute
        self.tezkor_xotira_hajmi = tezkor_xotira_hajmi  # public attribute
        self.brendi = brendi
        self.modeli = modeli

    @abstractmethod
    def id_sini_korish(self):
        pass

    @abstractmethod
    def narx_qoyish(self, narx):
        pass

    @abstractmethod
    def narxini_korish(self):
        pass

class IPhone(Telefon):
    def id_sini_korish(self):
        return self.__id

    def narx_qoyish(self, narx):
        self._narxi = narx

    def narxini_korish(self):
        return self._narxi

class Samsung(Telefon):
    def id_sini_korish(self):
        return self.__id

    def narx_qoyish(self, narx):
        self._narxi = narx

    def narxini_korish(self):
        return self._narxi

def telefonlarni_faylga_yoz(telefonlar, filename='telefonlar.json'):
    with open(filename, 'w') as f:
        json.dump([{
            'brendi': t.brendi,
            'modeli': t.modeli,
            'narxi': t._narxi,
            'tezkor_xotira_hajmi': t.tezkor_xotira_hajmi,
            'id': t.id_sini_korish()
        } for t in telefonlar], f)

def telefonlarni_fayldan_oq(filename='telefonlar.json'):
    try:
        with open(filename, 'r') as f:
            telefonlar_data = json.load(f)
            return [
                (IPhone(data['brendi'], data['modeli'], data['narxi'], data['tezkor_xotira_hajmi']) 
                 if data['brendi'] == "iPhone" 
                 else Samsung(data['brendi'], data['modeli'], data['narxi'], data['tezkor_xotira_hajmi']))
                for data in telefonlar_data
            ]
    except FileNotFoundError:
        return []

def main():
    telefonlar = telefonlarni_fayldan_oq()
    
    while True:
        print("0. Chiqish")
        print("1. Telefon qo'shish")
        print("2. Telefonlarni ko'rish")
        print("3. Telefon ustida amallar")
        tanlov = input("Tanlovni kiriting: ")

        if tanlov == '0':
            break
        elif tanlov == '1':
            brendi = input("Brendini kiriting: ")
            modeli = input("Modelini kiriting: ")
            narxi = float(input("Narxini kiriting: "))
            tezkor_xotira_hajmi = input("Tezkor xotira hajmini kiriting: ")
            if brendi.lower() == "iphone":
                telefonlar.append(IPhone(brendi, modeli, narxi, tezkor_xotira_hajmi))
            else:
                telefonlar.append(Samsung(brendi, modeli, narxi, tezkor_xotira_hajmi))
            telefonlarni_faylga_yoz(telefonlar)
        elif tanlov == '2':
            for t in telefonlar:
                print(f"{t.brendi} {t.modeli} (ID: {t.id_sini_korish()})")
        elif tanlov == '3':
            telefon_id = int(input("ID ni kiriting: "))
            telefon = next((t for t in telefonlar if t.id_sini_korish() == telefon_id), None)
            if telefon:
                print(f"1. ID ko'rsatish: {telefon.id_sini_korish()}")
                yangi_narx = float(input("Yangi narxni kiriting: "))
                telefon.narx_qoyish(yangi_narx)
                print(f"Yangi narxi: {telefon.narxini_korish()}")
            else:
                print("Telefon topilmadi.")

if __name__ == "__main__":
    main()