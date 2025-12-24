# MMX Billboard Preview Service

An automated FastAPI-based microservice that allows media planners to visualize advertisements (creatives) on real-world hoardings. The system automatically matches a creative's aspect ratio to the most suitable physical hoarding and generates a high-quality overlay preview.

## 🚀 Key Features
- **Automatic Board Selection**: Uses a ratio-matching algorithm to find the best hoarding for any artwork.
- **Precise Coordinate Mapping**: Leverages a JSON-based configuration to place ads exactly on billboard surfaces.
- **Instant Previews**: Generates realistic "site-in-situ" photos in seconds.
- **Scalable Design**: Add new hoarding sites simply by updating a configuration file.

## 🧠 The Logic
The system operates on three main pillars:
1. **Geometric Ratio Matching**: It calculates the aspect ratio ($W \div H$) of the uploaded file and compares it against the physical dimensions of available hoardings (e.g., 20x10, 4x4).
2. **Coordinate Transformation**: Using the `Pillow` library, it resizes the creative to fit the specific pixel coordinates $(x, y, w, h)$ of the target hoarding area in the site photo.
3. **API Orchestration**: A FastAPI backend handles the image upload, processing, and delivery of the final preview image.

## 🛠️ Tech Stack
- **Backend**: FastAPI (Python)
- **Image Processing**: Pillow (PIL)
- **Web Server**: Uvicorn
- **Data Storage**: JSON (Metadata & Configuration)

## 📂 Project Structure

MMX_Final/
├── app.py # FastAPI entrypoint & API routes
├── overlay.py # Image processing and overlay logic
├── ratio_service.py # Core logic for board matching
├── ratio_matcher.py # Helper algorithm for ratio calculation
├── boards_config.json # Hoarding metadata (paths & coordinates)
├── boards/ # Directory for hoarding site photos
├── uploads/ # Temporary storage for user uploads
└── requirements.txt # Project dependencies


## ⚙️ Installation & Setup

1. **Clone the repository:**
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd MMX_Final


2. **Install dependencies:**
pip install fastapi uvicorn Pillow

3. **Run the server:**
uvicorn app:app --reload


## 📖 Usage
1. Open your browser and go to `http://127.0.0.1:8000/docs`.
2. Use the **POST `/preview`** endpoint to upload your advertisement image.
3. The system will return the name of the selected board.
4. Go to the **GET `/download-preview`** endpoint to view your realistic billboard preview.

## 🤝 Contribution
This project was developed during an internship for the MMX project. Contributions to improve the matching algorithm or UI are welcome!
