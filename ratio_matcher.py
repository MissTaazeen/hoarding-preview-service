from typing import List, Tuple, Dict


def compute_aspect_ratio(width: float, height: float) -> float:
    return float(width) / float(height)


def find_best_boards_for_image(
    img_width: int,
    img_height: int,
    boards: List[Tuple[str, float, float]],
    max_diff: float = 0.2,
) -> List[Dict]:
    r_img = compute_aspect_ratio(img_width, img_height)
    results: List[Dict] = []

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

    results.sort(key=lambda x: x["ratio_diff"])
    return results
