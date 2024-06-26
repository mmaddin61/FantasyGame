import pygame
import pygame_gui
import data_parser
from pygame_gui.core import ObjectID

def main():
    pygame.init() # Initialize all imported pygame modules
    pygame.display.set_caption("Text Game") # Set the window's title
    screen = pygame.display.set_mode((1280, 720)) # Initialize the window and set its size to 1280x720
    background = pygame.Surface((1280, 720))
    background.fill(pygame.Color('#222222'))
    manager = pygame_gui.UIManager((800, 600))
    clock = pygame.time.Clock() # Create clock object to track time
    running = True # Set the running flag to true so the main loop will run

    manager = pygame_gui.UIManager((1280, 720), theme_path="themes/defaults.json")
    manager.get_theme().load_theme("themes/buttons.json")
    manager.get_theme().load_theme("themes/labels.json")

    scene_title_rect = pygame.Rect(0, 0, 1280, 200)
    scene_title = pygame_gui.elements.UILabel(relative_rect=scene_title_rect,
                                              text='Fantasy Game',
                                              manager=manager,
                                              object_id=ObjectID(class_id='@heading', object_id='#h1'))
    scene_body = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(0, 200, 1280, 400),
                                             text='Sample body text. This is where the scene is described in detail to give players context on what is going on.',
                                             manager=manager,
                                             object_id=ObjectID(class_id='@body', object_id='#p'))
    
    hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(0, 600, 1280, 120),
                                             text='Say Hello',
                                             manager=manager)
    
    data = data_parser.load_json_data('resources/dialogue/scene_test2.json')
    characters = data_parser.parse_characters(data)
    character = characters[0]
    print(character.get_name())
    print(character.get_guid())

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