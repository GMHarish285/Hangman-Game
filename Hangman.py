import pygame, sys, random

pygame.init()


class Hang:
    def __init__(self):
        self.hang_surf_list = ["0.png", "1.png", "2.png", "3.png", "4.png", "5.png", "6.png"]
        self.hang_surf_list_index = 0
        self.game_state = "game"

    def draw_hang(self):
        screen.blit(pygame.image.load(self.hang_surf_list[self.hang_surf_list_index]), (0, 0))

    def game_over_decision(self):
        if word.answer_list == ["_" for i in range(len(word.answer_list))]:
            self.game_state = "over_win"
        elif hang.hang_surf_list_index == 6:
            self.game_state = "over_lose"

    def game_over_screen(self):
        screen.fill(black)
        screen.blit(font_small.render("Press Space to restart.", True, white), (0, 100))
        if self.game_state == "over_win":
            screen.blit(font_large.render("You win!", True, white), (0, 0))
            screen.blit(font_small.render(f'The correct answer is {word.answer}', True, white), (0, 200))
        elif self.game_state == "over_lose":
            screen.blit(font_large.render("You lose!", True, white), (0, 0))
            screen.blit(font_small.render(f'The correct answer is {word.answer}', True, white), (0, 200))


class Word:
    def __init__(self):
        self.words_list = '''ant baboon badger bat bear beaver camel cat clam cobra cougar coyote
        crow
        deer
        dog
        donkey
        duck
        eagle
        ferret
        fox
        frog
        goat
        goose
        harish
        hawk
        lion
        lizard
        llama
        mole
        monkey
        moose
        mouse
        mule
        newt
        otter
        owl
        panda
        parrot
        pigeon
        python
        rabbit
        ram
        rat
        raven
        rhino
        salmon
        seal
        shark
        sheep
        skunk
        sloth
        snake
        spider
        stork
        swan
        tiger
        toad
        trout
        turkey
        turtle
        weasel
        whale
        wolf
        wombat
        zebra'''.split()
        self.answer = random.choice(self.words_list).upper()
        self.answer_list = list(self.answer)
        self.answer_length = len(self.answer)
        self.word_rect_list = []
        self.word_display_list = []

    def make_word(self):
        for i in range(self.answer_length):
            self.word_rect_list.append(pygame.Rect(i * 80, 500, 64, 64))
            self.word_display_list.append("_")

    def draw_word(self):
        for i, j in enumerate(self.word_rect_list):
            screen.blit(font_large.render(self.word_display_list[i], True, red), j)


class Button:
    def __init__(self):
        self.button_rect_list = []
        self.button_rect_distance_x = 40
        self.button_rect_distance_y = 40
        self.button_content_list = []
        self.button_colour_list = []
        self.button_active_list = []

    def make_buttons(self):
        for i in range(1, 27):
            self.button_rect_list.append(pygame.Rect(400 + self.button_rect_distance_x, 50 + self.button_rect_distance_y, 40, 40))
            self.button_rect_distance_x += 80
            if i % 5 == 0:
                self.button_rect_distance_x = 40
                self.button_rect_distance_y += 60

            self.button_content_list.append(chr(64+i))
            self.button_colour_list.append(blue_dark)
            self.button_active_list.append(True)

    def draw_buttons(self):
        for i, j in enumerate(self.button_rect_list):
            pygame.draw.rect(screen, self.button_colour_list[i], j)
            screen.blit(font_small.render(self.button_content_list[i], True, red), j)


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hangman")
icon_window = pygame.image.load("icon_32_hangman.png")
pygame.display.set_icon(icon_window)
clock = pygame.time.Clock()

red = (255, 0, 0)
blue_dark = (0, 0, 255)
blue_light = (102, 178, 255)
gray = (128, 128, 128)
black = (0, 0, 0)
white = (255, 255, 255)
font_small = pygame.font.Font("freesansbold.ttf", 40)
font_large = pygame.font.Font("freesansbold.ttf", 64)

hang = Hang()
word = Word()
button = Button()

word.make_word()
button.make_buttons()

while True:
    mouse = pygame.mouse.get_pos()

    if hang.game_state == "game":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                print(event)

            for i, j in enumerate(button.button_rect_list):
                if button.button_active_list[i]:
                    if j.collidepoint(mouse):
                        button.button_colour_list[i] = blue_light
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            button.button_active_list[i] = False
                            if button.button_content_list[i] in word.answer_list:
                                for k in range(word.answer_list.count(button.button_content_list[i])):
                                    word.word_display_list[word.answer_list.index(button.button_content_list[i])] = button.button_content_list[i]
                                    word.answer_list[word.answer_list.index(button.button_content_list[i])] = "_"
                            else:
                                if hang.hang_surf_list_index < 6:
                                    hang.hang_surf_list_index += 1
                    else:
                        button.button_colour_list[i] = blue_dark
                else:
                    button.button_colour_list[i] = gray

        screen.fill(white)
        hang.draw_hang()
        word.draw_word()
        button.draw_buttons()
        hang.game_over_decision()

    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    hang.game_state = "game"
                    hang.__init__()
                    word.__init__()
                    button.__init__()
                    word.make_word()
                    button.make_buttons()

        hang.game_over_screen()

    pygame.display.update()
    clock.tick(120)
