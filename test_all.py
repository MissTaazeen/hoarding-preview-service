# test_all.py
from overlay import generate_preview_for_image

result = generate_preview_for_image("image.jpg", max_diff=0.3)
print(result)
