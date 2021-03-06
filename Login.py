import pygame
import sys


def username_check(username):
    file = open("Database1.txt", "r")
    lines = file.readlines()
    for i in range(0, len(lines)):
        if lines[i][:-1] == username:
            return i
    return "Username not found."


def password_check(pass_line, password):
    file = open("Database2.txt", "r")
    lines = file.readlines()
    if lines[pass_line][:-1] == password:
        return "Password is correct."
    return "Wrong password."


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption('Login')
base_font = pygame.font.Font(None, 40)
user_text = ''
wrong_user = base_font.render("Username not Found", False, (255, 0, 0))
long = base_font.render("Username too long", False, (255, 0, 0))
ui1 = base_font.render("Username:", False, (0, 255, 0))
ui2 = base_font.render("Press END button to continue", False, (0, 0, 0))
input_rect = pygame.Rect(370, 200, 250, 40)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('gray15')
color = color_passive
active = False
len_flag = 0
len_flag2 = 0
wrong_user_flag = 0
while_flag1 = 0
while_flag2 = 0
while while_flag1 == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
        if event.type == pygame.KEYDOWN:
            if active:
                if len(user_text) <= 20:
                    len_flag = 0
                if len_flag == 0 and len_flag2 == 1:
                    len_flag2 = 0
                    screen.blit(wrong_user, (20000, 20000))
                    pygame.display.flip()
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_END:
                    check = username_check(user_text)
                    if check == "Username not found.":
                        wrong_user_flag = 1
                    else:
                        while_flag1 = 1
                        wrong_user_flag = 0
                        screen.blit(wrong_user, (20000, 20000))
                elif len(user_text) > 20:
                    len_flag = 1
                    len_flag2 = 1
                else:
                    user_text += event.unicode
    if active:
        color = color_active
    else:
        color = color_passive
    screen.fill((28, 28, 28))
    if len_flag == 1:
        screen.blit(long, (350, 100))
    if wrong_user_flag == 1:
        screen.blit(wrong_user, (350, 150))
    screen.blit(ui1, (200, 200))
    screen.blit(ui2, (270, 300))
    pygame.draw.rect(screen, color, input_rect, 2)
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    input_rect.w = max(200, text_surface.get_width() + 10)
    pygame.display.flip()
    clock.tick()
screen.fill((28, 28, 28))
color = color_passive
active = False
len_flag = 0
len_flag2 = 0
wrong_pass_flag = 0
user_text = ''
wrong_pass = base_font.render("Wrong password.", False, (255, 0, 0))
long = base_font.render("Password too long.", False, (255, 0, 0))
ui1 = base_font.render("Password:", False, (0, 255, 0))
input_rect = pygame.Rect(370, 200, 250, 40)
while while_flag2 == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
        if event.type == pygame.KEYDOWN:
            if active:
                if len(user_text) <= 20:
                    len_flag = 0
                if len_flag == 0 and len_flag2 == 1:
                    len_flag2 = 0
                    screen.blit(wrong_pass, (20000, 20000))
                    pygame.display.flip()
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_END:
                    check2 = password_check(check, user_text)
                    if check2 == "Wrong password.":
                        wrong_pass_flag = 1
                    else:
                        proved = open("Database3.txt", "w")
                        proved.write(str(check))
                        while_flag2 = 1
                        screen.blit(wrong_pass, (20000, 20000))
                        wrong_pass_flag = 0
                elif len(user_text) > 20:
                    len_flag = 1
                    len_flag2 = 1
                else:
                    user_text += event.unicode
    if active:
        color = color_active
    else:
        color = color_passive
    screen.fill((28, 28, 28))
    if len_flag == 1:
        screen.blit(long, (350, 100))
    if wrong_pass_flag == 1:
        screen.blit(wrong_pass, (350, 150))
    screen.blit(ui1, (200, 200))
    screen.blit(ui2, (270, 300))
    pygame.draw.rect(screen, color, input_rect, 2)
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    input_rect.w = max(200, text_surface.get_width() + 10)
    pygame.display.flip()
    clock.tick()