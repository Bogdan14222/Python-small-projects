import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "By Myself - The Grey Room _ Clark Sims.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP!")

            #initializing the module for playing songs (mixer is the module)
            pygame.mixer.init()

            #loading the file
            pygame.mixer.music.load(sound_file)

            #playing the song
            pygame.mixer.music.play()

            #if the song is still playing (is busy)
            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False

        time.sleep(1)

if __name__=="__main__":
    alarm_time = input("Enter the alarm time(HH:MM:SS): ")
    set_alarm(alarm_time)

