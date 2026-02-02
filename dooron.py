import time
import sys

print("\n song playing: 🫸 Dooron Dooron🫷")

lyrics = [
    "Dooron dooron main vekhaan tenu soneyo,",
    "Kahaan tu,      kahaan main,",
    "Ki main karaan ke main aavaan nazar tenu,",
    "Laayak tere kivein hovan tu dass mainu,",
    "Kol tere mainu aan de sohni,",
    "Karaan main kitne jatan o sohni😉,",
    "Dooron dooron main vekhaan tenu soneyo🙂",
    "by Abhi_Verma😉",
    "Thank-U😁",
    "......"
    "......"
]

timings =[2.9, 3.2, 0.9, 0.6, 0.7, 1.1, 1.4, 2.0, 1.0, 1.0]

typing_speed=0.11

for line,delay in zip(lyrics,timings):
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(typing_speed)
    print()
    time.sleep(delay)
