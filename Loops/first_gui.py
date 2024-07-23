picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

fillpixel = '* '
emptypixel = '  '

# With additional for loop
for row in picture:
    pixelrow = []
    for pixel in row:
        pixelrow.append(fillpixel) if pixel else pixelrow.append(emptypixel)
    print(''.join(pixelrow))

# Using list comprehension
for pixelrow in picture:
    print(''.join([fillpixel if pixel else emptypixel for pixel in pixelrow]))
