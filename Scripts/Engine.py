from Globals import *
from Player import *
from Camera import *
from TileMap import *
from planet import *
from enemy_bullet import *
from player_bullet import *
from SoundManager import *
from GameStateManager import *



class Engine:
    pygame.init()
    soundManager = SoundManager()
    gamestateManager = GameStateManager()
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480
    display = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.mixer.init()
    theme = pygame.mixer.music.load(soundManager.sounds[0])
    pygame.mixer.music.play()
    isRunning = True
    player = Player(10, 10)


    #player.init_inventory()
    tm = TileMap()

    Gamefont = pygame.font.SysFont("monospace", 10)
    playerFont = pygame.font.SysFont("monospace", 10)
    #font = Gamefont.render("test", True, (255, 255, 255))

    clock = pygame.time.Clock()
    GroupManager.player_sprite.add(player)
    background = pygame.Surface([SCREEN_WIDTH, SCREEN_HEIGHT])
    backgroundS = pygame.image.load("../Images/background.png")
    background.blit(backgroundS, (0, 0))
    backgroundX = 0
    #eb = Enemybullet(10, 10, 2,player)


    GroupManager.all_sprite.add(player)

    tm.draw_map(display)

    player.walls = GroupManager.wall_sprite
    player.bullet = GroupManager.bullet_sprite
    player.enemy = GroupManager.enemy_sprite

    @staticmethod
    def update():



        #GroupManager.enemy_sprite.add(eb)
        while Engine.isRunning:
            #game loop
            #
            mousePos = pygame.mouse.get_pos()
            Engine.gamestateManager.startState("game")
            Engine.gamestateManager.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        Engine.tm.reload_map(Engine.display)
                    Engine.player._update_keypressed(event)
                    if event.key == pygame.K_ESCAPE:
                        Engine.isRunning = False
                    if event.key == pygame.K_SPACE:
                        pass
                    """
                        for ent in GroupManager.player_sprite:
                            eb = playerBullet(ent.rect.x, ent.rect.y, 10, mousePos)
                            GroupManager.player_bullet.add(eb)
                    """
                if event.type == pygame.KEYUP:
                    Engine.player._update_keyup(event)
                if event.type == pygame.QUIT:
                    Engine.isRunning = False
            Engine.display.fill([255, 255, 255])



            if Engine.backgroundX <= -480:
                Engine.backgroundX = 480
            else:
                Engine.backgroundX -= 0.08
            Engine.player.update_rotation(mousePos)
            Engine.background.blit(Engine.backgroundS, (0, int(Engine.backgroundX)))
            Camera.Camera_Transform(Engine.player, Engine.isRunning)
            GroupManager.all_sprite.update()
            Engine.display.blit(Engine.background, (0, 0))
            GroupManager.planet_sprite.update()
            #Engine.eb.update(Engine.player)
            for ent in GroupManager.bullet_sprite:
                ent._update(Engine.player)
            for ent in GroupManager.player_bullet:
                ent._update(Engine.player)
            for ent in GroupManager.level_exit:
                ent._update(Engine.tm)

            GroupManager.healthpack_sprite.update()
            GroupManager.blood_sprite.update()
            GroupManager.corpse_sprite.update()
            GroupManager.barnacle_group.update()
            GroupManager.weapon_group.update()
            GroupManager.planet_sprite.draw(Engine.display)
            GroupManager.rocket_bullet.draw(Engine.display)

            GroupManager.grass_sprite.draw(Engine.display)
            GroupManager.level_exit.draw(Engine.display)
            GroupManager.blood_sprite.draw(Engine.display)
            GroupManager.all_sprite.draw(Engine.display)
            GroupManager.rocket_bullet.draw(Engine.display)

            GroupManager.enemy_sprite.draw(Engine.display)
            GroupManager.bullet_sprite.draw(Engine.display)
            GroupManager.player_bullet.draw(Engine.display)
            GroupManager.door1_sprite.draw(Engine.display)
            Engine.player.Render_health(Engine.Gamefont, Engine.display)
            GroupManager.healthpack_sprite.draw(Engine.display)
            GroupManager.corpse_sprite.draw(Engine.display)
            for ent in GroupManager.enemy_sprite:
                ent._Render_health(Engine.playerFont, Engine.display)
                ent._update(Engine.player)
            GroupManager.barnacle_group.draw(Engine.display)
            for ent in GroupManager.barnacle_group:
                ent._draw(Engine.display)
            GroupManager.weapon_group.draw(Engine.display)
            pygame.display.update()

            Engine.clock.tick(60)
        pygame.quit()
