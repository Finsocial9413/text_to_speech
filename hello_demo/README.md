# Text-to-Speech Demo: "hello how are you"

## Overview
This demo shows the text-to-speech conversion process for the phrase "hello how are you".

## Files Generated
- **Input Text**: input_20250720_060455.txt
- **API Request**: api_request_20250720_060455.json
- **API Response**: api_response_20250720_060455.json

## Process Flow
1. Input text: "hello how are you"
2. Language: English (en)
3. Processing: Google Text-to-Speech (gTTS)
4. Output: MP3 audio file
5. Access: Via download URL

## Usage
To use the actual TTS API:

```bash
# Start the server
python3 "google(Text-to-Speech).py"

# Make a request
curl -X POST "http://localhost:8005/text-to-speech" \
     -H "Content-Type: application/json" \
     -d '{"text": "hello how are you", "language": "en"}'
```

## Demo Generated
- Date: 2025-07-20
- Time: 06:04:55
- Text: "hello how are you"
