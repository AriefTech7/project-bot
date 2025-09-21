import random
from datetime import datetime
from prompt import my_prompt
import calendar

start_bot = True
chatbot = "bot: "

def greeting():
    greeting = ["Hai bro!", "Halo, sob!", " Hey you"]
    random.shuffle(greeting)
    return random.choice(greeting)

# fungsi untuk menampilkan waktu dan tanggal

def date_time(waktu):
    if "jam" in waktu:
        time_now = datetime.now()
        return time_now.strftime("%I:%M %p")
    
    elif "hari" in waktu:
        date_now = datetime.now()
        return date_now.strftime("%A")
        
    
    elif "tanggal" in waktu:
        tgl_now = datetime.now()
        return tgl_now.strftime("%d")
    
    elif "bulan" in waktu:
        bulan_now = datetime.now()
        return bulan_now.strftime("%B")
    
    elif "tahun" in waktu:
        tahun_now = datetime.now()
        return tahun_now.strftime("%Y")
    
prompt = []

while start_bot:
    user = input("user: ").lower()
    # ls_user = user.split()

    if "hello" in user:
        print(f"{{}}{greeting()}".format(chatbot))
    elif "jam" in user:
        print(f"{{}}sekarang jam {date_time(user)}".format(chatbot))
    elif "hari" in user:
        print(f"{{}}sekarang hari {date_time(user)}".format(chatbot))
    elif "tanggal" in user:
        print(f"{{}}sekarang hari {date_time(user)}".format(chatbot))
    elif "bulan" in user:
        print(f"{{}}sekarang hari {date_time(user)}".format(chatbot))
    elif "tahun" in user:
        print(f"{{}}sekarang hari {date_time(user)}".format(chatbot))
    elif "bye" in user:
        print("{}sampai jumpa".format(chatbot))
        start_bot = False
    else:
        prompt.append(user)
        print(prompt)
        print("{}saya tidak mengerti".format(chatbot))

