# Text-to-Speech API

A Python-based text-to-speech service using Google's gTTS (Google Text-to-Speech) with FastAPI backend.

## Demo: "Hello How Are You"

This repository demonstrates text-to-speech conversion with the phrase **"hello how are you"** as a test case.

## Features

- 🎯 **FastAPI Backend**: RESTful API for text-to-speech conversion
- 🔊 **Google TTS Integration**: High-quality speech synthesis
- 🌐 **CORS Enabled**: Web browser compatibility
- ⚡ **Speed Control**: Normal and slow speech options
- 📁 **File Management**: Automatic audio file generation and downloads
- 🛡️ **Error Handling**: Robust error handling and logging

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the API Server

```bash
python3 "google(Text-to-Speech).py"
```

The server will start on `http://localhost:8005`

### 3. Test with "Hello How Are You"

#### Using cURL:
```bash
curl -X POST "http://localhost:8005/text-to-speech" \
     -H "Content-Type: application/json" \
     -d '{"text": "hello how are you", "language": "en"}'
```

#### Using the Demo Script:
```bash
python3 simple_demo.py
```

## API Endpoints

### POST `/text-to-speech`
Convert text to speech

**Request Body:**
```json
{
  "text": "hello how are you",
  "language": "en"
}
```

**Response:**
```json
{
  "status": "success",
  "filepath": "audio_files/hello_20250720_060000_12345678.mp3",
  "filename": "hello_20250720_060000_12345678.mp3",
  "download_url": "/download/hello_20250720_060000_12345678.mp3",
  "message": "Audio file created successfully (2340 bytes)"
}
```

### GET `/download/{filename}`
Download generated audio file

### GET `/`
API health check and usage information

## Demo Scripts

### 1. Simple Demo (`simple_demo.py`)
Creates a complete demo showing the TTS workflow for "hello how are you" without requiring network connectivity.

```bash
python3 simple_demo.py
```

### 2. Speed Test (`speed.py`)
Demonstrates different speech speeds for the phrase "hello how are you".

```bash
python3 speed.py
```

### 3. Complete Demo (`demo_hello.py`)
Full integration test with server startup, API calls, and file downloads.

```bash
python3 demo_hello.py
```

### 4. Client Script (`download_audio.py`)
Interactive client for text-to-speech conversion and downloads.

```bash
python3 download_audio.py
```

## File Structure

```
text_to_speech/
├── google(Text-to-Speech).py  # FastAPI server
├── download_audio.py          # Client script
├── speed.py                   # Speed control utility
├── simple_demo.py            # Offline demo script
├── demo_hello.py             # Complete integration demo
├── test_hello.py             # Basic TTS test
├── requirements.txt          # Dependencies
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

## Supported Languages

The API supports all languages supported by Google Text-to-Speech:
- `en` - English
- `es` - Spanish
- `fr` - French
- `de` - German
- And many more...

## Configuration

### CORS Origins
The API is configured to accept requests from:
- `http://127.0.0.1:5500`
- `http://127.0.0.1:3000`
- `http://127.0.0.1:5173`
- `https://voiceassistant.finsocial.tech`

### Audio Storage
Generated audio files are stored in the `audio_files/` directory and can be downloaded via the `/download/` endpoint.

## Example Usage

### Python Client
```python
import requests

# Start the server first: python3 "google(Text-to-Speech).py"

response = requests.post("http://localhost:8005/text-to-speech", json={
    "text": "hello how are you",
    "language": "en"
})

if response.status_code == 200:
    data = response.json()
    download_url = f"http://localhost:8005{data['download_url']}"
    # Download the audio file
    audio = requests.get(download_url)
    with open("hello.mp3", "wb") as f:
        f.write(audio.content)
```

### JavaScript/Web
```javascript
fetch('http://localhost:8005/text-to-speech', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        text: 'hello how are you',
        language: 'en'
    })
})
.then(response => response.json())
.then(data => {
    console.log('Success:', data);
    // Use data.download_url to get the audio file
});
```

## Dependencies

- `gtts>=2.5.4` - Google Text-to-Speech
- `fastapi>=0.116.1` - Web framework
- `uvicorn>=0.35.0` - ASGI server
- `requests>=2.31.0` - HTTP library
- `pydantic>=2.11.0` - Data validation

## Error Handling

The API includes comprehensive error handling for:
- Network connectivity issues
- Invalid text input
- File system errors
- Language code validation

## Development

To contribute or modify the code:

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run tests: `python3 test_hello.py`
4. Start the server: `python3 "google(Text-to-Speech).py"`
5. Test the API endpoints

## License

This project is open source and available under the MIT License.

## Demo Output

The phrase **"hello how are you"** is used throughout this repository as a demonstration of the text-to-speech capabilities. When you run any of the demo scripts, they will generate audio files containing this greeting in high-quality speech synthesis.