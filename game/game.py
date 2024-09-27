import pygame as pg

class Game():
    def __init__(self,fps):
        pg.init()

        self.screen = pg.display.set_mode((1280,720))
        self.clock = pg.time.Clock()

        self.max_fps = fps

    def update_globals(self):
        self.events = pg.event.get()
        self.dt = self.clock.get_fps()

    def check_game(self):
        for event in self.events:
            if event.type == pg.QUIT:
                pg.quit()
                exit()

    def draw_to_screen(self):
        self.screen.fill("cyan")

    def update_screen(self):
        pg.display.flip()
        
        self.clock.tick(self.max_fps)

    def main(self):
        while True:
            self.update_globals()
            self.check_game()

            self.draw_to_screen()
            self.update_screen()
        

        