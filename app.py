import os
import uuid
import shutil
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from overlay import generate_preview_for_image

app = FastAPI(title="MMX Billboard Preview Service")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/preview")
async def get_preview(file: UploadFile = File(...)):
    file_ext = os.path.splitext(file.filename)[1]
    temp_name = f"{uuid.uuid4()}{file_ext}"
    temp_path = os.path.join(UPLOAD_DIR, temp_name)

    try:
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save file: {str(e)}")

    try:
        result = generate_preview_for_image(temp_path)
        
        return {
            "status": "success",
            "board_name": result["board"]["name"],
            "ratio_diff": result["board"]["ratio_diff"],
            "preview_url": "/download-preview"
        }
    except Exception as e:
        if os.path.exists(temp_path):
            os.remove(temp_path)
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/download-preview")
async def download_preview():
    """
    Endpoint to download the generated preview image.
    """
    preview_path = "preview.png"
    if os.path.exists(preview_path):
        return FileResponse(preview_path, media_type="image/png")
    raise HTTPException(status_code=404, detail="Preview image not found. Please generate one first.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
