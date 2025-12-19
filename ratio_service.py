from typing import List, Tuple, Dict
from PIL import Image
from ratio_matcher import find_best_boards_for_image

# put all your real boards here once, instead of repeating in many files
BOARDS: List[Tuple[str, float, float]] = [
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

def suggest_boards_for_image(
    img_path: str,
    max_diff: float = 0.3,
    top_k: int = 5
) -> List[Dict]:
    """
    Given an image path, return top_k boards sorted by ratio match,
    each with 'fits' == True/False.
    """
    img = Image.open(img_path)
    w, h = img.size
    results = find_best_boards_for_image(w, h, BOARDS, max_diff=max_diff)

    # optionally keep only top_k best matches
    return results[:top_k]