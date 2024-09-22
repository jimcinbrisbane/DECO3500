import pygame
import time
import threading

# Initialize pygame
pygame.init()

# Set up the mixer
pygame.mixer.init()

# Load the drum sound and the trigger sound
drum_sound = pygame.mixer.Sound("kick.wav")
one = pygame.mixer.Sound("1.1.wav")
five = pygame.mixer.Sound("5.2.wav")
eight = pygame.mixer.Sound("8.1.wav")

# Set the BPM for the drum beat
bpm = 33
beat_duration = 60 / bpm  # Duration of one beat in seconds

# Define the number of beats for continuous playback
num_beats = 33

def play_drum_beat():
    while running:
        for _ in range(num_beats):
            drum_sound.play()
            time.sleep(beat_duration)

# Set up the display (optional)
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Press 'x' to play trigger sound")

# Start drum beat in a separate thread
running = True
drum_thread = threading.Thread(target=play_drum_beat, daemon=True)
drum_thread.start()

# Run the game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                one.play()
            if event.key == pygame.K_5:
                five.play()
            if event.key == pygame.K_8:
                eight.play()

# Stop the drum beat and clean up
running = False
drum_thread.join()
pygame.quit()

