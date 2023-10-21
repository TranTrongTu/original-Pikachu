           

# import pygame
# import sys

# pygame.init()

# # Tạo một cửa sổ Pygame
# screen = pygame.display.set_mode((400, 400))

# # Tạo một surface cho hình chữ nhật
# rect_surface = pygame.Surface((400, 400))
# rect_surface.fill((0, 0, 0))  # Điền màu nền đen vào surface

# # Tạo màu gradient từ bên phải qua trái (đỏ đến xanh dương)
# for x in range(600):
#     color = (255 - x/3, 0, x/3)  # RGB color
#     pygame.draw.line(rect_surface, color, (x, 0), (x/3, 30))

# # Vòng lặp chính
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     screen.fill((255, 255, 255))  # Điền màu nền trắng
#     screen.blit(rect_surface, (0, 0))  # Vẽ hình chữ nhật với màu gradient từ bên phải qua trái lên màn hình

#     pygame.display.flip()

# pygame.quit()
# sys.exit()

a = 10

def cal(x):
    x = 20

cal(a)
print(a)