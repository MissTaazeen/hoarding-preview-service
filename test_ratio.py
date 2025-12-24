# test_ratio.py (you already have this, just fix the path + indent)
from ratio_service import suggest_boards_for_image

test_image = "image.jpg"  # or any real creative path in this folder
results = suggest_boards_for_image(test_image, max_diff=0.3, top_k=5)

for r in results:
    print(r)
