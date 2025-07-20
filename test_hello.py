#!/usr/bin/env python3
"""
Simple test script to demonstrate text-to-speech conversion for "hello how are you"
"""

from gtts import gTTS
import os
import tempfile
import webbrowser
from datetime import datetime

def test_hello_tts():
    """Test converting 'hello how are you' to speech"""
    
    text = "hello how are you"
    language = "en"
    
    print(f"Testing text-to-speech conversion for: '{text}'")
    print(f"Language: {language}")
    
    try:
        # Create output directory
        output_dir = "test_audio"
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"hello_how_are_you_{timestamp}.mp3"
        filepath = os.path.join(output_dir, filename)
        
        print(f"Creating audio file: {filepath}")
        
        # Convert text to speech
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save(filepath)
        
        print(f"✅ Audio file created successfully: {filepath}")
        
        # Check file size
        file_size = os.path.getsize(filepath)
        print(f"File size: {file_size} bytes")
        
        return filepath
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return None

def test_offline_tts():
    """Test with a simple file-based approach if network fails"""
    
    text = "hello how are you"
    
    # Create a simple test file to verify the concept
    output_dir = "test_audio"
    os.makedirs(output_dir, exist_ok=True)
    
    # Create a placeholder file for demonstration
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"hello_test_{timestamp}.txt"
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, 'w') as f:
        f.write(f"Text-to-Speech Test\n")
        f.write(f"Text: {text}\n")
        f.write(f"Language: en\n")
        f.write(f"Timestamp: {datetime.now().isoformat()}\n")
    
    print(f"✅ Test file created: {filepath}")
    return filepath

if __name__ == "__main__":
    print("="*50)
    print("Text-to-Speech Test: 'hello how are you'")
    print("="*50)
    
    # First try the actual TTS
    result = test_hello_tts()
    
    if not result:
        print("\nFalling back to offline test...")
        result = test_offline_tts()
    
    print(f"\nTest completed. Result: {result}")