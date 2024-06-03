import pygame
import pygame_gui

def main():
    pygame.init() # Initialize all imported pygame modules
    pygame.display.set_caption("Text Game") # Set the window's title
    screen = pygame.display.set_mode((1280, 720)) # Initialize the window and set its size to 1280x720
    background = pygame.Surface((1280, 720))
    background.fill(pygame.Color('#000000'))
    manager = pygame_gui.UIManager((800, 600))
    clock = pygame.time.Clock() # Create clock object to track time
    running = True # Set the running flag to true so the main loop will run

    manager = pygame_gui.UIManager((800, 600), theme_path="src/themes/quick_start.json")
    hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                             text='Say Hello',
                                             manager=manager)

    # Main loop
    while running:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get(): # Loop through each event in the queue
            if event.type == pygame.QUIT: # Check if the event is a quit event
                running = False # Set running flag to false to terminate the main loop on the next iteration
            manager.process_events(event)

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == hello_button:
                    print('Hello World!')

        manager.update(time_delta)

        screen.fill("purple") # Clear everything from the screen by filling it with a single color

        # Rendering code goes here
        screen.blit(background, (0, 0))
        manager.draw_ui(screen)

        pygame.display.update() # Paint the screen with changes made above

    pygame.quit() # Quit pygame once the main loop breaks

if __name__ == "__main__":
    main()