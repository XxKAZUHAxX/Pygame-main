import pygame
import cv2
import mediapipe as mp
import random

# Pygame initialization
pygame.init()
screen_width = 1280
screen_height = 720
game_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Balloon Pop")

# Font initialization
font = pygame.font.SysFont("Arial", 36)

# Mediapipe initialization for hand tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
cap = cv2.VideoCapture(0)

# Balloon class
class Balloon:
    def __init__(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.radius = random.randint(30, 60)
        self.x = random.randint(self.radius, screen_width - self.radius)
        self.y = screen_height + self.radius
        self.speed = random.randint(6, 10)
        self.popped = False

    def move(self):
        self.y -= self.speed

    def draw(self):
        pygame.draw.circle(game_screen, self.color, (self.x, self.y), self.radius)

# Initialize balloons list
balloons = []

# Initialize score and timer
score = 0
time_left = 60 # in seconds

# Game loop
running = True
start_time = pygame.time.get_ticks() // 1000
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Pygame screen setup
    game_screen.fill((255, 255, 255))

    # Capture video frame
    ret, frame = cap.read()

    # Flip the frame horizontally for a mirror effect
    frame = cv2.flip(frame, 1)

    # Convert the BGR frame to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hands
    results = hands.process(rgb)

    # Draw balloons
    for balloon in balloons:
        balloon.move()
        if balloon.y < -balloon.radius:
            balloons.remove(balloon)
        if not balloon.popped:
            balloon.draw()

    # Pop balloons on finger inside
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            x, y = int(index_finger_tip.x * screen_width), int(index_finger_tip.y * screen_height)
            for balloon in balloons:
                if not balloon.popped and (balloon.x - x)**2 + (balloon.y - y)**2 <= balloon.radius**2:
                    balloon.popped = True
                    score += 1
            # Display finger position
            pygame.draw.circle(game_screen, (255, 0, 0), (x, y), 10)

    # Spawn new balloons
    if random.randint(0, 30) == 0:
        balloons.append(Balloon())

    # Display score
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    game_screen.blit(score_text, (10, 10))

    # Display timer
    time_elapsed = (pygame.time.get_ticks() // 1000) - start_time
    time_left = 60 - time_elapsed
    if time_left < 0:
        time_left = 0
    time_text = font.render("Time: " + str(time_left), True, (0, 0, 0))
    game_screen.blit(time_text, (700, 10))
    
    # Update the Pygame display
    pygame.display.update()
    
# Release the video capture
cap.release()

# Close Pygame
pygame.quit()