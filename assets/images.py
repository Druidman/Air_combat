import pygame as pg
import os

current_dir = os.path.dirname(__file__)
images_path = os.path.join(current_dir, "Pictures")


images = {
    "Planes":{
        "F-14": pg.image.load(f"{images_path}/f-14-px.png").convert_alpha(),
        "F-16": pg.image.load(f"{images_path}/f-16-px.png").convert_alpha(),
        "Su-27": pg.image.load(f"{images_path}/su-27-px.png").convert_alpha()
    },
    "Other":{
        "Bullet": pg.image.load(f"{images_path}/bullet.png").convert_alpha(),
        "Cloud": pg.image.load(f"{images_path}/cloud.png").convert_alpha()
    }
}