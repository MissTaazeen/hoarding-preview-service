# Hoarding Preview Service
Given a creative image, this service:

1. Reads the image size and computes its aspect ratio.
2. Compares it with configured board sizes taken from media plan PPTs.
3. Selects the best-fitting board based on aspect ratio.
4. Overlays the creative onto the board photo to generate a preview.

## Tech stack
- Python 3
- FastAPI (backend API)
- Uvicorn (ASGI server)
- Pillow (image processing)

## Setup
pip install -r requirements.txt


## Run the API
uvicorn app:app --reload


Then open `http://127.0.0.1:8000/docs` in a browser:

1. Use `POST /preview`.
2. Click **Try it out** and upload a creative image.
3. Execute and download the returned preview image.

## Configuration

- `boards/` contains board/hoarding photos.
- `boards_config.json` defines, for each board:
  - `file`: path to the board image.
  - `x, y, w, h`: rectangle where the creative is pasted.

Then commit and push:
git add README.md
git commit -m "Add README with setup and usage"
git push
