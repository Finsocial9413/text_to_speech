from gtts import gTTS
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import uuid
from datetime import datetime

app = FastAPI(title="Text-to-Speech API", description="An API that converts text to speech using Google's TTS")

# Configure CORS
origins = [
    "http://127.0.0.1:5500",  # Your specified origin
    "http://127.0.0.1:3000",  # Your specified origin
    "http://127.0.0.1:5173",  # Your specified origin
    "https://voiceassistant.finsocial.tech",
    # Add more allowed origins here if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Define the request model
class TextToSpeechRequest(BaseModel):
    text: str
    language: str = "en"  # Default language is English

# Define the response model
class TextToSpeechResponse(BaseModel):
    status: str
    filepath: str
    filename: str
    download_url: str
    message: str

# Define the output directory for audio files
AUDIO_DIR = "audio_files"
os.makedirs(AUDIO_DIR, exist_ok=True)

@app.post("/text-to-speech", response_model=TextToSpeechResponse)
async def text_to_speech(request: TextToSpeechRequest):
    try:
        # Generate a unique filename
        filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}.mp3"
        filepath = os.path.join(AUDIO_DIR, filename)
        
        # Convert text to speech
        speech = gTTS(text=request.text, lang=request.language)
        speech.save(filepath)
        
        # Return the file path and download URL
        return {
            "status": "success", 
            "filepath": filepath,
            "filename": filename,
            "download_url": f"/download/{filename}",
            "message": "Audio file created successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating speech: {str(e)}")

@app.get("/download/{filename}")
async def download_file(filename: str):
    filepath = os.path.join(AUDIO_DIR, filename)
    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(
        filepath, 
        media_type="audio/mpeg", 
        filename=filename,
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )

@app.get("/")
async def root():
    return {"message": "Welcome to the Text-to-Speech API", "usage": "POST /text-to-speech with JSON body {\"text\": \"Your text here\"}"}

# For testing purposes if run directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8005)