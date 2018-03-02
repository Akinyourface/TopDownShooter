from Globals import *
from Engine import *

class Camera:
    CameraX = 0
    CameraY = 0
    VelocityX = 0
    VelocityY = 0
    CameraWidth = SCREEN_WIDTH
    CameraHeight = SCREEN_HEIGHT
    CameraDir = 0
    CameraZoom = 1 #default is 0
    CameraEntSpeed = 4
    @staticmethod
    def Update_Keypressed(event):
        if event.key == pygame.K_LEFT:
            Camera.VelocityX = -1
        if event.key == pygame.K_RIGHT:
            Camera.VelocityX = 1
        if event.key == pygame.K_UP:
            Camera.VelocityY = 1
        if event.key == pygame.K_DOWN:
            Camera.VelocityY = -1

    @staticmethod
    def Update_Keyup(event):
        if event.key == pygame.K_LEFT:
            Camera.VelocityX = 0
        if event.key == pygame.K_RIGHT:
            Camera.VelocityX = 0
        if event.key == pygame.K_UP:
            Camera.VelocityY = 0
        if event.key == pygame.K_DOWN:
            Camera.VelocityY = 0

    @staticmethod
    def Update():
        Camera.CameraX += Camera.VelocityX
        Camera.CameraY += Camera.VelocityY

    @staticmethod
    def Camera_Transform(player, isRunning):
        if player.rect.y + 16 >= SCREEN_HEIGHT / 4 * 3 + 10:
            for ent in GroupManager.camera_group:
                ent.rect.y -= Camera.CameraEntSpeed
        if player.rect.y + 16 <= SCREEN_HEIGHT / 4 * 3 - 250:
            for ent in GroupManager.camera_group:
                ent.rect.y += Camera.CameraEntSpeed
        if player.rect.x + 16 >= SCREEN_WIDTH / 4 * 3 + 10:
            for ent in GroupManager.camera_group:
                ent.rect.x -= Camera.CameraEntSpeed
        if player.rect.x + 16 <= SCREEN_WIDTH / 4 * 3 - 350:
            for ent in GroupManager.camera_group:
                ent.rect.x += Camera.CameraEntSpeed

    @staticmethod
    def Camera_Zoom(event):
        if event.key == pygame.K_i:
            Camera.CameraZoom += 1
        if event.key == pygame.K_l:
            if Camera.CameraZoom > 1:
                Camera.CameraZoom -= 1
            else:
                Camera.CameraZoom = 1
        print(Camera.CameraZoom)
