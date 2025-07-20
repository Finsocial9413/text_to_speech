#!/usr/bin/env python3
"""
Speed control utility for Text-to-Speech
Demonstrates different speech speeds for "hello how are you"
"""

from gtts import gTTS
import os
from datetime import datetime

def create_hello_with_speed(slow=False, output_dir="speed_test"):
    """Create 'hello how are you' audio with different speeds"""
    
    text = "hello how are you"
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate filename with speed indicator
    speed_name = "slow" if slow else "normal"
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"hello_{speed_name}_{timestamp}.mp3"
    filepath = os.path.join(output_dir, filename)
    
    try:
        print(f"Creating {speed_name} speed audio: {filepath}")
        
        # Create TTS with specified speed
        tts = gTTS(text=text, lang='en', slow=slow)
        tts.save(filepath)
        
        file_size = os.path.getsize(filepath)
        print(f"✅ Created: {filepath} ({file_size} bytes)")
        
        return filepath
        
    except Exception as e:
        print(f"❌ Error creating {speed_name} speed audio: {e}")
        return None

def main():
    """Demo function to create both normal and slow speed versions"""
    
    print("Speed Test for 'hello how are you'")
    print("="*40)
    
    # Create normal speed version
    normal_file = create_hello_with_speed(slow=False)
    
    # Create slow speed version  
    slow_file = create_hello_with_speed(slow=True)
    
    print("\nSpeed test completed!")
    if normal_file:
        print(f"Normal speed: {normal_file}")
    if slow_file:
        print(f"Slow speed: {slow_file}")

if __name__ == "__main__":
    main()