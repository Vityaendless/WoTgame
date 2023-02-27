import pygame, sys
from fireball import Fireball
from trolloc import Trolloc
import time

def events(screen, moiraine, fireballs):
    """event flow"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                moiraine.move_to_right = True
            elif event.key == pygame.K_a:
                moiraine.move_to_left = True
            elif event.key == pygame.K_SPACE:
                new_fireball = Fireball(screen, moiraine)
                fireballs.add(new_fireball)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                moiraine.move_to_right = False
            elif event.key == pygame.K_a:
                moiraine.move_to_left = False

def update_screen(bg_color, screen, statistics, score, moiraine, trollocs, fireballs):
    screen.fill(bg_color)
    score.show_score()
    for fireball in fireballs.sprites():
        fireball.draw_fireball()
    moiraine.output()
    trollocs.draw(screen)
    pygame.display.flip()

def update_fireballs(screen, statistics, score, trollocs, fireballs):
    """update fireballs positions"""
    fireballs.update()
    for fireball in fireballs.copy():
        if fireball.rect.bottom <= 0:
            fireballs.remove(fireball)

    collisions = pygame.sprite.groupcollide(fireballs, trollocs, True, True)
    if collisions:
        for trollocs in collisions.values():
            statistics.score += 1 * len(trollocs)
        score.render_score()
        check_score(statistics, score)
        score.view_lives()
    if len(trollocs) == 0:
        fireballs.empty()
        create_trollocs(screen, trollocs)

def moraine_killed(statistics, screen, score, moiraine, trollocs, fireballs):
    """moiraine is fall"""
    if statistics.moiraine_lives > 0:
        statistics.moiraine_lives -= 1
        score.view_lives()
        trollocs.empty()
        fireballs.empty()
        create_trollocs(screen, trollocs)
        moiraine.moraine_reborn()
        time.sleep(2)
    else:
        statistics.lives_marker = False
        sys.exit()

def update_trollocs(statistics, screen, score, moiraine, trollocs, fireballs):
    """update trollocs army"""
    trollocs.update()
    if pygame.sprite.spritecollideany(moiraine, trollocs):
        moraine_killed(statistics, screen, score, moiraine, trollocs, fireballs)
    trollocs_checking(statistics, screen, score, moiraine, trollocs, fireballs)

def trollocs_checking(statistics, screen, score, moiraine, trollocs, firewalls):
    """trollocs finished"""
    screen_rect = screen.get_rect()
    for trolloc in trollocs.sprites():
        if trolloc.rect.bottom >= screen_rect.bottom:
            moraine_killed(statistics, screen, score, moiraine, trollocs, firewalls)
            break

def create_trollocs(screen, trollocs):
    """created army of trolllocs"""
    trolloc = Trolloc(screen)
    trolloc_width = trolloc.rect.width
    row_of_trollocs = int((700 - 2 * trolloc_width) / trolloc_width)
    trolloc_height = trolloc.rect.height
    column_of_trollocs = int((800-150 - 2 * trolloc_height) / trolloc_height)

    for trolloc_in_column in range(column_of_trollocs):
        for trolloc_in_row in range(row_of_trollocs):
            trolloc = Trolloc(screen)
            trolloc.x = trolloc_width + (trolloc_width * trolloc_in_row)
            trolloc.y = trolloc_height + trolloc_height * trolloc_in_column
            trolloc.rect.x = trolloc.x
            trolloc.rect.y = trolloc.rect.height + trolloc.rect.height * trolloc_in_column
            trollocs.add(trolloc)

def check_score(statistics, score):
    if statistics.score > statistics.high_score:
        statistics.high_score = statistics.score
        score.render_high_score()
        with open('high_score.txt', 'w') as file:
            file.write(str(statistics.high_score))