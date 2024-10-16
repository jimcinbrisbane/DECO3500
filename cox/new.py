import pygame
import random
import threading
import time
import serial

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Create a dictionary to store lists of sounds
sounds = {
    1: [
        pygame.mixer.Sound("1.1.wav"),
        pygame.mixer.Sound("1.2.wav"),
        pygame.mixer.Sound("1.3.wav"),
        pygame.mixer.Sound("1.4.wav")
    ],
    2: [
        pygame.mixer.Sound("2.1.wav"),
        pygame.mixer.Sound("2.2.wav"),
        pygame.mixer.Sound("2.3.wav"),
        pygame.mixer.Sound("2.4.wav")
    ],
    3: [
        pygame.mixer.Sound("3.1.wav"),
        pygame.mixer.Sound("3.2.wav")
    ],
    4: [
        pygame.mixer.Sound("4.1.wav"),
        pygame.mixer.Sound("4.2.wav"),
        pygame.mixer.Sound("4.3.wav")
    ],
    5: [
        pygame.mixer.Sound("5.1.wav"),
        pygame.mixer.Sound("5.2.wav")
    ],
    6: [
        pygame.mixer.Sound("6.1.wav"),
        pygame.mixer.Sound("6.2.wav")
    ],
    7: [
        pygame.mixer.Sound("7.1.wav"),
        pygame.mixer.Sound("7.2.wav"),
        pygame.mixer.Sound("7.3.wav"),
        pygame.mixer.Sound("7.4.wav")
    ],
    8: [
        pygame.mixer.Sound("8.1.wav"),
        pygame.mixer.Sound("8.2.wav")
    ],
    9: [
        pygame.mixer.Sound("9.1.wav"),
        pygame.mixer.Sound("9.2.wav")
    ],
    10: [
        pygame.mixer.Sound("10.1.wav"),
        pygame.mixer.Sound("10.2.wav")
    ],
    11: [
        pygame.mixer.Sound("11.1.wav"),
        pygame.mixer.Sound("10.2.wav")
    ],
    12: [
        pygame.mixer.Sound("12.1.wav"),
    ]
}
# Function to play random sound from a specified group

def play_random_sound(group):
    if group in sounds:
        sound = random.choice(sounds[group])
        sound.play()

# time based triggers
def timer_30s():
    time.sleep(30)
    if not pygame.mixer.get_busy():
        print("30-second timer finished!")
        pygame.mixer.Sound("6.1.wav").play()

def timer_1min():
    time.sleep(60)
    if not pygame.mixer.get_busy():
        print("finished!")
        pygame.mixer.Sound("6.2.wav").play()

# Threaded timers
threading.Thread(target=timer_30s, daemon=True).start()
threading.Thread(target=timer_1min, daemon=True).start()

## working context-aware cox
# Initialize serial connections
arduino1 = serial.Serial('COM5', 9600, timeout=1)
arduino2 = serial.Serial('COM6', 9600, timeout=1)
time.sleep(2)  # Allow time for connection

# Function to read speeds from serial
def read_speed(serial_connection):
    try:
        data = serial_connection.readline().decode().strip()
        return float(data)
    except (ValueError, serial.SerialException):
        return None
one = pygame.mixer.Sound("1.1.wav")
two = pygame.mixer.Sound("2.4.wav")
three = pygame.mixer.Sound("3.1.wav")
four = pygame.mixer.Sound("4.1.wav")
five = pygame.mixer.Sound("5.1.wav")
six = pygame.mixer.Sound("6.1.wav")
seven = pygame.mixer.Sound("7.1.wav")
eight = pygame.mixer.Sound("8.1.wav")
nine = pygame.mixer.Sound("9.1.wav")
zero = pygame.mixer.Sound("10.1.wav")
drop = pygame.mixer.Sound("1.4.wav")
drop2 = pygame.mixer.Sound("5.1.wav")
drop3 = pygame.mixer.Sound("5.2.wav")
half = pygame.mixer.Sound("6.1.wav")
done = pygame.mixer.Sound("6.2.wav")
out =  pygame.mixer.Sound("OUTTATIME.mp3")
# Function to handle Arduino data reading in a thread
outSync = 0
def monitor_speeds():
    counter = 0 # move the number up if people are really good and know what they are doing
    #counter as encouragement
    outSync = 0 # to do: make the out of sync trigger based on the distance of the ultrasound sensor.

    while running:
            # Read speed data from both Arduinos
        speed1 = read_speed(arduino1)
        # timestamp1 = "" to do for more better out of sync trigger
        speed2 = read_speed(arduino2)
        # timestamp2 = ""
        # if speed1 != 
        # Ensure both speeds are valid before comparison
        if speed1 is not None and speed2 is not None:
            print(f"5:({speed1}), 6:({speed2})")


            if speed1 > speed2:
                if (speed1 - speed2) > 11:
                    print(f"Arduino 1 is faster by {speed1 - speed2:.2f}")
                    if not pygame.mixer.get_busy():
                        out.play()
                else:
                    print(f"same")
                    if counter == 1:
                        if not pygame.mixer.get_busy():
                            four.play()
                            counter = 0
                    else:
                        counter = 1

                # else:
                #     counter = counter + 1
            elif speed2 > speed1:
                if (speed2 - speed1) > 11:
                    print(f"Arduino 2 is faster by {speed2 - speed1:.2f}")
                    if not pygame.mixer.get_busy():
                        out.play()
                else:
                    print(f"same")
                    if not pygame.mixer.get_busy():
                        four.play()

                # else:
                #     counter = counter + 1
            else:
                print(f"same")
                # if not pygame.mixer.get_busy():
                #         four.play()
                # counter = counter + 1
            if speed1 > 30 or speed2 > 30:
                    print("really fast")
                    if not pygame.mixer.get_busy():
                        nine.play()
            elif speed1 < 20 or speed2 < 20:
                    print("really slow")
                    if not pygame.mixer.get_busy():
                        two.play()
            # if people are really bad at staying in sync uncomment this
            # else:
            #     print("good work")
            #     if counter == 1:
            #         if not pygame.mixer.get_busy():
            #             four.play()
            #             counter = 0
            #     else:
            #         counter = 1
                
                
                

        # Wait a bit before reading the next set of values
        time.sleep(0.5)
# Set up Pygame display, when the display close, the session is closed.
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Press 'x' to play trigger sound")
running = True
threading.Thread(target=monitor_speeds, daemon=True).start()

#addtional sound pad triggers
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Key mappings for playing sounds
            if event.key == pygame.K_1: play_random_sound(1)
            elif event.key == pygame.K_2: play_random_sound(2)
            elif event.key == pygame.K_3: play_random_sound(3)
            elif event.key == pygame.K_4: play_random_sound(4)
            elif event.key == pygame.K_5: play_random_sound(5)
            elif event.key == pygame.K_6: play_random_sound(6)
            elif event.key == pygame.K_7: play_random_sound(7)
            elif event.key == pygame.K_8: play_random_sound(8)
            elif event.key == pygame.K_9: play_random_sound(9)
            elif event.key == pygame.K_0: play_random_sound(10)
            elif event.key == pygame.K_q: play_random_sound(11)
            elif event.key == pygame.K_w: play_random_sound(12)


# Start monitoring speeds in a separate thread


pygame.quit()
