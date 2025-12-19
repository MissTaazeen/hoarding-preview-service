from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import shutil
import uuid
import os

from overlay import generate_preview_for_image

app = FastAPI()

os.makedirs("uploads", exist_ok=True)


@app.post("/preview", response_class=FileResponse)
async def preview_board(file: UploadFile = File(...)):
    # 1) save uploaded creative temporarily
    ext = os.path.splitext(file.filename)[1] or ".jpg"
    tmp_name = f"{uuid.uuid4()}{ext}"
    tmp_path = os.path.join("uploads", tmp_name)

    with open(tmp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 2) generate preview
    out_path = "preview.png"  # always overwrite for now
    result = generate_preview_for_image(tmp_path, max_diff=0.3, output_path=out_path)

    # 3) optionally delete original creative
    os.remove(tmp_path)

    # 4) return the preview image
    return FileResponse(
        path=out_path,
        media_type="image/png",
        filename="preview.png",
    )
