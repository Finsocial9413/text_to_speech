#!/usr/bin/env python3
"""
Simple offline demo for "hello how are you" text-to-speech functionality
This script demonstrates the TTS workflow without requiring network connectivity
"""

import os
import json
from datetime import datetime

def create_hello_demo():
    """Create a demo showing the TTS workflow for 'hello how are you'"""
    
    text = "hello how are you"
    
    print("Text-to-Speech Demo: 'hello how are you'")
    print("="*50)
    
    # Create demo output directory
    demo_dir = "hello_demo"
    os.makedirs(demo_dir, exist_ok=True)
    
    # Create demo files
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # 1. Create text input file
    input_file = os.path.join(demo_dir, f"input_{timestamp}.txt")
    with open(input_file, 'w') as f:
        f.write(text)
    
    print(f"✅ Input text saved: {input_file}")
    
    # 2. Create API request demo
    api_request = {
        "text": text,
        "language": "en",
        "timestamp": datetime.now().isoformat(),
        "expected_output": "MP3 audio file"
    }
    
    request_file = os.path.join(demo_dir, f"api_request_{timestamp}.json")
    with open(request_file, 'w') as f:
        json.dump(api_request, f, indent=2)
    
    print(f"✅ API request demo saved: {request_file}")
    
    # 3. Create expected response demo
    api_response = {
        "status": "success",
        "filepath": f"audio_files/hello_20250720_060000_{timestamp[:8]}.mp3",
        "filename": f"hello_20250720_060000_{timestamp[:8]}.mp3",
        "download_url": f"/download/hello_20250720_060000_{timestamp[:8]}.mp3",
        "message": "Audio file created successfully (2340 bytes)",
        "input_text": text,
        "language": "en"
    }
    
    response_file = os.path.join(demo_dir, f"api_response_{timestamp}.json")
    with open(response_file, 'w') as f:
        json.dump(api_response, f, indent=2)
    
    print(f"✅ API response demo saved: {response_file}")
    
    # 4. Create README for the demo
    readme_content = f"""# Text-to-Speech Demo: "hello how are you"

## Overview
This demo shows the text-to-speech conversion process for the phrase "hello how are you".

## Files Generated
- **Input Text**: {os.path.basename(input_file)}
- **API Request**: {os.path.basename(request_file)}
- **API Response**: {os.path.basename(response_file)}

## Process Flow
1. Input text: "{text}"
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
curl -X POST "http://localhost:8005/text-to-speech" \\
     -H "Content-Type: application/json" \\
     -d '{{"text": "{text}", "language": "en"}}'
```

## Demo Generated
- Date: {datetime.now().strftime('%Y-%m-%d')}
- Time: {datetime.now().strftime('%H:%M:%S')}
- Text: "{text}"
"""
    
    readme_file = os.path.join(demo_dir, "README.md")
    with open(readme_file, 'w') as f:
        f.write(readme_content)
    
    print(f"✅ Demo README saved: {readme_file}")
    
    print(f"\n📁 Demo files created in: {demo_dir}/")
    print(f"🎯 Target phrase: '{text}'")
    print("✨ Demo completed successfully!")
    
    return demo_dir

def main():
    """Main function to run the demo"""
    
    print("Starting 'hello how are you' TTS Demo")
    print("Timestamp:", datetime.now().isoformat())
    print()
    
    demo_dir = create_hello_demo()
    
    print(f"\n{'='*50}")
    print("Demo Summary:")
    print(f"- Phrase: 'hello how are you'")
    print(f"- Demo directory: {demo_dir}")
    print(f"- Files created: 4 (input, request, response, README)")
    print("- Status: ✅ Complete")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()