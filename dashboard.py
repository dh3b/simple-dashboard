import datetime
import random
import requests
import os 

R_QUOTES = (
    '“Don’t watch the clock; do what it does. Keep going.” – Sam Levenson',
    '“The secret of getting ahead is getting started.” – Mark Twain',
    '“It always seems impossible until it’s done.” – Nelson Mandela',
    '“You don’t have to be great to start, but you have to start to be great.” – Zig Ziglar',
    '“Success is the sum of small efforts, repeated day in and day out.” – Robert Collier',
    '“Action is the foundational key to all success.” – Pablo Picasso',
    '“Do something today that your future self will thank you for.” – Sean Patrick Flanery',
    '“Push yourself, because no one else is going to do it for you.” – Unknown',
    '“Great things never came from comfort zones.” – Unknown',
    '“Dream big. Start small. Act now.” – Robin Sharma',
    '“If you get tired, learn to rest, not quit.” – Banksy',
    '“You miss 100% of the shots you don’t take.” – Wayne Gretzky',
    '“The best way to predict the future is to invent it.” – Alan Kay',
    '“Start where you are. Use what you have. Do what you can.” – Arthur Ashe',
    '“Don’t limit your challenges. Challenge your limits.” – Unknown',
    '“If opportunity doesn’t knock, build a door.” – Milton Berle',
    '“The way to get started is to quit talking and begin doing.” – Walt Disney',
    '“Small deeds done are better than great deeds planned.” – Peter Marshall',
    '“Success doesn’t come from what you do occasionally. It comes from what you do consistently.” – Marie Forleo',
    '“Discipline is choosing between what you want now and what you want most.” – Abraham Lincoln (attrib.)',
    '“Stay afraid, but do it anyway.” – Carrie Fisher',
    '“Believe you can and you’re halfway there.” – Theodore Roosevelt',
    '“Fall seven times, stand up eight.” – Japanese Proverb',
    '“The only limit to our realization of tomorrow is our doubts of today.” – Franklin D. Roosevelt',
    '“Hard choices, easy life. Easy choices, hard life.” – Jerzy Gregorek',
    '“Success is not final, failure is not fatal: it is the courage to continue that counts.” – Winston Churchill'
)

API_URL = f"https://newsapi.org/v2/top-headlines"
API_KEY = f"your-api-key-here"

t_date = datetime.datetime.now()
t_timestamp = t_date.strftime("%Y-%m-%d_%H-%M-%S")
log_name = f"dashbrd_log_{t_timestamp}.txt"

with open(log_name, "w") as f:
    f.write(f"dashboard started, {t_timestamp}\n")
    print(f"Basic info dashboard\n")

    day = int(t_date.strftime("%d"))
    t_date_day = f"{day}{'th' if 11<=day<=13 else {1:'st', 2:'nd', 3:'rd'}.get(day%10, 'th')}"
    print(f"Today is {t_date.strftime("%A")}\n{t_date_day} of {t_date.strftime("%b")}, {t_date.strftime("%Y")}")
    f.write(f"printed data info\n")

    random.seed()
    print(f"Random quote: {random.choice(R_QUOTES)}")
    f.write(f"printed random quote\n")

    params = {
        "country": "us",
        "apiKey": API_KEY
    }

    print(f"Latest: ", end="")
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        av = data["totalResults"]
        ar_num = random.randrange(len(data["articles"]))
        f.write(f"news id: {ar_num}\n")

        print(f"{data["articles"][ar_num]["title"]} - {data["articles"][ar_num]["author"]}")
        desc = data["articles"][ar_num]["description"]
        print(desc[:253] + "..." if len(desc) > 256 else desc)

        f.write(f"printed api news\n")
    else:
        print(f"Sorry! No news for today")
        f.write(f"News api error: {response.status_code}\n")
    
    print(f"Currently working in: {os.getcwd()}\nHave a nice day!")
    f.write(f"printed os info, quitting...")
