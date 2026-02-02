import time
import sys

print("\nSong playing : For A Reason\n.")

lyrics = [
    "hass ke tu thik mera hal rakhda",
    "jivein kahaan, karen, naa sawaal rakhda",
    "chitt naa laggey taan nal-nal rakhda",
    "ve kinna mera, sohanas, khyal rakhda",
    "jivein tu akhaan nu milaai jaanen",
    "nasha jeha, nasha jeha karaayi jaanen",
    "jivein tu merinaa' langhai jaanen nede ton, nede hor aayi jaanen kinna tang kardi aan",
    "HA HA",
    "mathe 'te tiudi nahi jamaan",
    "pata mainu dedenga tujaan",
    "mainu tere naa'pyaar jata taan (tere naa'pyaar jata)",
    "tere naa pyaar jata taan",
    "mainu tere naa' pyaarjata taan",
    "THANKS 😊",
    "By Abhi_Verma",
    "YYYY",
]

timings =[0.7,0.7,0.7,0.7,0.7,1.2,1.5,0.8,0.9,0.9,0.9,0.7,0.7,0.7,0.7]

typing_speed=0.053

for line,delay in zip(lyrics,timings):
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(typing_speed)
    print()
    time.sleep(delay)
