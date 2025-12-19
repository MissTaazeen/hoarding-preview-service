from ratio_service import suggest_boards_for_image

res = suggest_boards_for_image("image.jpg", max_diff=0.3, top_k=5)
for r in res:
    print(r)
