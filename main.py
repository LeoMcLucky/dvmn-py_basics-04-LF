from PIL import Image

image = Image.open('monro.jpg')
red, green, blue = image.split()

coordinates_red_left = (50, 0, red.width, red.height)
cropped_red_left = red.crop(coordinates_red_left)

coordinates_red_mid = (25, 0, red.width - 25, red.height)
cropped_red_mid = red.crop(coordinates_red_mid)

blend_red = Image.blend(cropped_red_left, cropped_red_mid, 0.3)

coordinates_blue_left = (0, 0, blue.width - 50, blue.height)
cropped_blue_left = blue.crop(coordinates_blue_left)

coordinates_blue_mid = (25, 0, blue.width - 25, blue.height)
cropped_blue_mid = blue.crop(coordinates_blue_mid)

blend_blue = Image.blend(cropped_blue_left, cropped_blue_mid, 0.3)

coordinates_green_mid = (25, 0, green.width - 25, green.height)
cropped_green_mid = green.crop(coordinates_green_mid)

retro_img = Image.merge("RGB", (blend_red, cropped_green_mid, blend_blue))
retro_img.save("retro_monro.jpg")
retro_img.thumbnail((80, 80))
retro_img.save("retro_monro_avatar.jpg")
