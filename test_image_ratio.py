from PIL import Image
from ratio_matcher import find_best_boards_for_image

img_path = "image.jpg"  # make sure image.jpg is in the MMX folder
img = Image.open(img_path)
w, h = img.size
print("Image size:", w, h)

boards = [
    ("RABALE_4x4", 4, 4),
    ("RABALE_8x4", 8, 4),
    ("RABALE_18x4", 18, 4),
    ("VASHI_30x15", 30, 15),
    ("NERUL_30x15", 30, 15),
    ("KALYAN_40x40", 40, 40),
    ("PANVEL_40x35", 40, 35),
    ("DME_60x20", 60, 20),
    ("JANSPATH_20x20", 20, 20),
]

results = find_best_boards_for_image(w, h, boards, max_diff=0.3)
for r in results:
    print(r)
