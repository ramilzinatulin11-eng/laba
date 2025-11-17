def draw_rectangle(a, b, m, n, rectangle_color, background_color):
    image = []
    for i in range(m):
        row = []
        for j in range(n):
            # Проверяем, находится ли пиксель внутри прямоугольника
            start_i = (m - b) // 2
            start_j = (n - a) // 2
            if (start_i <= i < start_i + b) and (start_j <= j < start_j + a):
                row.append(rectangle_color)
            else:
                row.append(background_color)
        image.append(row)
    return image

def draw_ellipse(a, b, m, n, ellipse_color, background_color):
    image = []
    center_i = m // 2
    center_j = n // 2
    for i in range(m):
        row = []
        for j in range(n):
            # Проверяем, находится ли пиксель внутри эллипса
            x = j - center_j
            y = i - center_i
            if (x*x)/(a*a) + (y*y)/(b*b) <= 1:
                row.append(ellipse_color)
            else:
                row.append(background_color)
        image.append(row)
    return image

# Тесты
print("Прямоугольник 5x3 на изображении 7x7:")
rect = draw_rectangle(5, 3, 7, 7, (255, 0, 0), (0, 0, 0))
for row in rect:
    print(' '.join(str(pixel) for pixel in row))

print("\nЭллипс с осями 5x3 на изображении 7x7:")
ellipse = draw_ellipse(5, 3, 7, 7, (0, 255, 0), (0, 0, 0))
for row in ellipse:
    print(' '.join(str(pixel) for pixel in row))