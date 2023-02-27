import pygame, controls
from moiraine import Moiraine
from pygame.sprite import Group
from score import Score
from statistics import Statistic

def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Moiraine's strike")
    bg_color = (22, 22, 26)
    moiraine = Moiraine(screen)
    fireballs = Group()
    trollocs = Group()
    controls.create_trollocs(screen, trollocs)
    statistics = Statistic()
    score = Score(screen, statistics)

    while True:
        controls.events(screen, moiraine, fireballs)
        if statistics.lives_marker:
            moiraine.update()
            controls.update_screen(bg_color, screen, statistics, score, moiraine, trollocs, fireballs)
            controls.update_fireballs(screen, statistics, score, trollocs, fireballs)
            controls.update_trollocs(statistics, screen, score, moiraine, trollocs, fireballs)

run()