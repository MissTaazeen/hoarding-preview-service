from ratio_service import suggest_boards_for_image
from overlay import place_creative_on_board

creative = "image.jpg"

# 1) get best boards by ratio
matches = suggest_boards_for_image(creative, max_diff=0.3, top_k=1)
best = matches[0]
print("Best board:", best)

board_name = best["name"]

# 2) create preview
out_path = "preview.png"
place_creative_on_board(board_name, creative, out_path)
print("Saved preview to", out_path)
