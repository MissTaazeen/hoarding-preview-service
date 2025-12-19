from typing import List, Tuple, Dict

def compute_aspect_ratio(width: float, height: float) -> float:
    return float(width) / float(height)

def find_best_boards_for_image(
    img_width: int,
    img_height: int,
    boards: List[Tuple[str, float, float]],
    max_diff: float = 0.2
) -> List[Dict]:
    """
    boards: list of (board_name, board_width, board_height) using the PPT sizes, e.g. ("Vashi_30x15", 30, 15).
    max_diff: max allowed |ratio_board - ratio_image| to consider it a good fit.
    """
    r_img = compute_aspect_ratio(img_width, img_height)
    results = []

    for name, bw, bh in boards:
        r_board = compute_aspect_ratio(bw, bh)
        diff = abs(r_board - r_img)
        fits = diff <= max_diff
        results.append({
            "name": name,
            "board_width": bw,
            "board_height": bh,
            "board_ratio": r_board,
            "image_ratio": r_img,
            "ratio_diff": diff,
            "fits": fits,
        })

    # sort by smallest ratio_diff (best first)
    results.sort(key=lambda x: x["ratio_diff"])
    return results

from ratio_matcher import find_best_boards_for_image

boards = [
    ("Vashi_30x15", 30, 15),
    ("Kalyan_40x40", 40, 40),
    ("Station_20x10", 20, 10),
]

print(find_best_boards_for_image(1920, 1080, boards))
