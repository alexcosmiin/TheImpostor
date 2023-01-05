import pygame
from time import sleep

def start_adventure():

    # Set the font
    font = pygame.font.Font("font.ttf", 32)

    # Set the button labels
    button_labels = ["Option 1", "Option 2"]

    # Set the button areas
    button_rects = [
      pygame.Rect(100, 500, 200, 50),
      pygame.Rect(500, 500, 200, 50)
    ]

    # Set the selected button
    selected_button = 0

    # Set the running state
    running = True

    pygame.mixer.init()
    sound_kitchen = pygame.mixer.Sound("kitchennoises.mp3")
    sound_kitchen.set_volume(0.3)
    sound_police = pygame.mixer.Sound("police.mp3")
    sound_police.set_volume(0.3)

    bg_image1 = pygame.image.load("image1.jpg")
    bg_image2 = pygame.image.load("image2.jpg")
    bg_image3 = pygame.image.load("image3.jpg")
    bg_image4 = pygame.image.load("image4.jpg")
    bg_verybadending = pygame.image.load("verybadending.jpg")
    bg_badendingpolice = pygame.image.load("badendingpolice.jpg")
    x = bg_image1
    h = 0
    while running:
      screen.blit(x, (0, 0))
      # Draw the buttons
      for i, label in enumerate(button_labels):
        # Render the button label
        text_surface = font.render(label, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = button_rects[i].center
        # Draw the button
        if i == selected_button:
          pygame.draw.rect(screen, (255, 255, 255), button_rects[i], 2)
        screen.blit(text_surface, text_rect)
        # Check for events
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            running = False
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
              # Select the previous button
              selected_button = (selected_button - 1) % len(button_labels)
            if event.key == pygame.K_RIGHT:
              # Select the next button
              selected_button = (selected_button + 1) % len(button_labels)
            if event.key == pygame.K_RETURN:
              h=h+1
              screen.fill((0, 0, 0))
              # Execute the selected button
              if selected_button == 1:
                if h==1:
                  screen.blit(bg_verybadending, (0, 0))
                  pygame.display.flip()
                  sleep(30)
                  return
                elif h == 2:
                  x = bg_image3
                elif h == 3:
                  x = bg_image4

              elif selected_button == 0:
                if h == 1:
                  x = bg_image2
                  sound_kitchen.play()
                elif h == 2:
                  screen.blit(bg_verybadending, (0, 0))
                  pygame.display.flip()
                  sleep(30)
                  return
                elif h == 3:
                    screen.blit(bg_badendingpolice, (0, 0))
                    sound_police.play()
                    pygame.display.flip()
                    sleep(30)
                    return









      # Update the display
      pygame.display.flip()

    # Quit Pygame
    pygame.quit()




# Initialize Pygame
pygame.init()

# Set the window size
window_size = (800, 600)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the window title
pygame.display.set_caption("The Impostor")

# Load the image
image = pygame.image.load("menu_background.jpg")

# Load the music
pygame.mixer.music.load("menu_music.mp3")

# Set the volume (0.0 to 1.0)
pygame.mixer.music.set_volume(0.1)

# Play the music
pygame.mixer.music.play(-1)

# Set the font
font = pygame.font.Font(None, 32)

# Set the menu options
menu_options = ["Start New Game", "How to play", "Stats", "Quit"]

# Set the selected option
selected_option = 0

# Set the running state
running = True

while running:
  # Check for events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        selected_option = (selected_option - 1) % len(menu_options)
      elif event.key == pygame.K_DOWN:
        selected_option = (selected_option + 1) % len(menu_options)
      elif event.key == pygame.K_RETURN:
        if menu_options[selected_option] == "Start New Game":
          start_adventure()
        elif menu_options[selected_option] == "How to play":
          load_saved_game()
        elif menu_options[selected_option] == "Stats":
          game_options()
        elif menu_options[selected_option] == "Quit":
          running = False

  # Clear the screen
  screen.fill((0, 0, 0))

  # Draw the image on the screen
  screen.blit(image, (0, 0))

  # Draw the menu options
  for i, option in enumerate(menu_options):
    text_surface = font.render(option, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.center = (400, 300 + i * 50)
    screen.blit(text_surface, text_rect)

  # Draw a rectangle around the selected option
  pygame.draw.rect(screen, (255, 255, 255), (150, 275 + selected_option * 50, 500, 50), 2)

  # Update the display
  pygame.display.flip()

# Quit Pygame
pygame.quit()








