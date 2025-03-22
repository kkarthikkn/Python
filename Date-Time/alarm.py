import time
import datetime as dt
import pygame       # to access the audio file

def set_alarm(alarm):
    print(f"Alarm Set for time {alarm}")
    sound_file=r"Risen - Density & Time.mp3"  # audio file should be same directory
    is_running=True

    while is_running:
        current_time=dt.datetime.now().strftime("%I:%M:%S")
        print(current_time)
        if current_time==alarm:
            print("Wake Up!")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():        # get_busy(): checks whether music is playing,
                                                        # it won't stop until the  music ends
                time.sleep(1)

            is_running=False
        time.sleep(1)

if __name__=="__main__":
    alarm=input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm)