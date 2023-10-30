import pygame as pg

pg.init()

# Tạo cửa sổ Pygame
screen = pg.display.set_mode((400, 400))

# Load ảnh
image = pg.image.load("your_image.png")
image_rect = image.get_rect()

# Khởi tạo độ trong suốt ban đầu
alpha = 0  # Bắt đầu từ không (hoàn toàn trong suốt)

# Tốc độ tỏ dần
fade_speed = 2

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Tăng độ trong suốt
    alpha += fade_speed

    # Đặt giới hạn, nếu độ trong suốt vượt quá 255, đặt lại về 255
    if alpha > 255:
        alpha = 255

    # Tạo một bản sao hình ảnh với độ trong suốt hiện tại
    faded_image = image.copy()
    faded_image.set_alpha(alpha)

    screen.fill((255, 255, 255))
    screen.blit(faded_image, (100, 100))
    pg.display.flip()

    # Dừng khi độ trong suốt đạt 255
    

pg.quit()
