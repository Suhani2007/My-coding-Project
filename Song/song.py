import pygame
import time
import sys

def run_song():
    pygame.mixer.init()
    
    try:
        pygame.mixer.music.load("pal pal.mp3")
        pygame.mixer.music.play()
    except:
        print("Error: music.mp3 file sapdli nahi!")
        return

    # 1. INTRO DELAY: Gaana suru jalyavar lyrics kiti seconds nantar suru vhavet?
    # Jar 'Pal Pal' ushira yet asel, tar ha number vadhav (e.g., 5.0 kiwa 10.0)
    # Jar 'Pal Pal' lavkar yet asel, tar ha number kami kar.
    time.sleep(1.0) 

    # 2. LYRICS DATA: (Lyrics chi line, Pudhchi line yenyapurvi kiti thambayche)
    lyrics_data = [
        ("Music........", 6.7),
        ("Tera mera afsana",3.5),
        ("Poora hua na, jaana",1.5),
        ("Music........", 0.7),
        ("Pal-pal jeena muhaal mera tere bina", 1.0),
        ("Yeh saare nashe bekaar teri aankhon ke siva", 1.7),
        ("Ghar nahi jaata, main bahar, rehta tera intezaar", 0.9),
        ("Mere khwabon mein aa na karke 16 singhaar", 0),
        ("Main ab kyun hosh mein aata nahi?", 0),
        ("Sukoon yeh dil kyun paata nahi?", 0),
        ("Kyun todun khud se jo the waade?",0),
        ("Ke ab yeh ishq nibhana nahi",0),
        ("Main modun tumse jo yeh chehra",0),
        ("Dobara nazar milana nahi",0),
        ("Yeh duniya jaane mera dard",0),
        ("Tujhe yeh nazar kyun aata nahi?",0)
    ]

    for line, pause in lyrics_data:
        # Akshar type honyacha speed (Typewriter effect)
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.08)
        
        print()
        
        # Line samplyavar gaana break (pause) karayche asel tar ithe logic vapru shakto
        # Sadhyasathi ha pause line-to-line sync sathi ahe
        time.sleep(pause)
    pygame.mixer.music.stop()

if __name__ == "__main__":
    run_song()