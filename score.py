import pygame.font
from moiraine import Moiraine
from heart import Heart
from pygame.sprite import Group

class Score():
    """print info"""
    def __init__(self, screen, statistics):
        """score inicialization"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.statistics = statistics
        self.text_color = 232, 157, 16
        self.font = pygame.font.SysFont(None, 36)
        self.render_score()
        self.render_high_score()
        self.view_lives()

    def render_score(self):
        self.print_score = self.font.render(str(self.statistics.score),
                                            True,
                                            self.text_color,
                                            (22, 22, 26))
        self.view_text = self.print_score.get_rect()
        self.view_text.right = self.screen_rect.right - 40
        self.view_text.top = 20

    def render_high_score(self):
        self.print_high_score = self.font.render(str(self.statistics.high_score),
                                                 True,
                                                 self.text_color,
                                                 (22, 22, 26))
        self.view_high_score_text = self.print_high_score.get_rect()
        self.view_high_score_text.centerx = self.screen_rect.centerx
        self.view_high_score_text.top = self.screen_rect.top + 20

    def view_lives(self):
        """counts of live"""
        self.moirainlives = Group()
        for moiraine_live_count in range(self.statistics.moiraine_lives):
            moiraine_live = Heart(self.screen)
            moiraine_live.rect.x = 15 + moiraine_live_count * moiraine_live.rect.width
            moiraine_live.rect.y = 20
            self.moirainlives.add(moiraine_live)

    def show_score(self):
        self.screen.blit(self.print_score, self.view_text)
        self.screen.blit(self.print_high_score, self.view_high_score_text)
        self.moirainlives.draw(self.screen)


