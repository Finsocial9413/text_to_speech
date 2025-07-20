#!/usr/bin/env python3
"""
Demo script for Text-to-Speech functionality
Demonstrates converting "hello how are you" to speech
"""

import requests
import json
import time
import os
import threading
import subprocess
import sys
from datetime import datetime

class TextToSpeechDemo:
    def __init__(self, api_url="http://localhost:8005"):
        self.api_url = api_url
        self.server_process = None
        
    def start_server(self):
        """Start the FastAPI server"""
        print("Starting Text-to-Speech API server...")
        try:
            # Start the server as a subprocess
            self.server_process = subprocess.Popen([
                sys.executable, "google(Text-to-Speech).py"
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            # Wait a moment for server to start
            time.sleep(3)
            
            # Check if server is running
            try:
                response = requests.get(f"{self.api_url}/")
                if response.status_code == 200:
                    print("✅ Server started successfully!")
                    return True
            except:
                pass
                
            print("❌ Server failed to start properly")
            return False
            
        except Exception as e:
            print(f"❌ Error starting server: {e}")
            return False
    
    def stop_server(self):
        """Stop the FastAPI server"""
        if self.server_process:
            print("Stopping server...")
            self.server_process.terminate()
            self.server_process.wait()
            
    def test_hello_phrase(self):
        """Test converting 'hello how are you' to speech"""
        
        test_phrase = "hello how are you"
        print(f"\n{'='*60}")
        print(f"Testing Text-to-Speech with: '{test_phrase}'")
        print(f"{'='*60}")
        
        # Prepare the request
        payload = {
            "text": test_phrase,
            "language": "en"
        }
        
        try:
            print(f"Sending request to {self.api_url}/text-to-speech...")
            print(f"Payload: {json.dumps(payload, indent=2)}")
            
            response = requests.post(f"{self.api_url}/text-to-speech", json=payload)
            
            print(f"Response status: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                print("✅ Success! Response:")
                print(json.dumps(data, indent=2))
                
                # Try to download the file
                return self.download_audio_file(data)
                
            else:
                print(f"❌ Error: {response.status_code}")
                print(f"Response: {response.text}")
                return False
                
        except Exception as e:
            print(f"❌ Request failed: {e}")
            return False
    
    def download_audio_file(self, response_data):
        """Download the generated audio file"""
        
        try:
            download_url = response_data.get("download_url")
            filename = response_data.get("filename")
            
            if not download_url:
                print("❌ No download URL provided")
                return False
                
            full_url = f"{self.api_url}{download_url}"
            print(f"\nDownloading audio file from: {full_url}")
            
            # Create downloads directory
            download_dir = "downloads"
            os.makedirs(download_dir, exist_ok=True)
            
            # Download the file
            audio_response = requests.get(full_url)
            
            if audio_response.status_code == 200:
                local_path = os.path.join(download_dir, filename)
                
                with open(local_path, "wb") as f:
                    f.write(audio_response.content)
                
                file_size = len(audio_response.content)
                print(f"✅ Audio file downloaded: {local_path} ({file_size} bytes)")
                
                return True
            else:
                print(f"❌ Download failed: {audio_response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ Download error: {e}")
            return False
    
    def test_api_health(self):
        """Test if the API is healthy"""
        try:
            response = requests.get(f"{self.api_url}/")
            if response.status_code == 200:
                data = response.json()
                print("✅ API Health Check:")
                print(json.dumps(data, indent=2))
                return True
            else:
                print(f"❌ API health check failed: {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ API health check error: {e}")
            return False
    
    def run_demo(self):
        """Run the complete demo"""
        print("Text-to-Speech Demo")
        print("Phrase: 'hello how are you'")
        print(f"Timestamp: {datetime.now().isoformat()}")
        
        try:
            # Start server
            if not self.start_server():
                return False
                
            # Test API health
            if not self.test_api_health():
                return False
                
            # Test the hello phrase
            success = self.test_hello_phrase()
            
            return success
            
        finally:
            # Always try to stop the server
            self.stop_server()

def main():
    demo = TextToSpeechDemo()
    
    print("Starting Text-to-Speech Demo for 'hello how are you'")
    print("="*60)
    
    success = demo.run_demo()
    
    print("\n" + "="*60)
    if success:
        print("✅ Demo completed successfully!")
        print("The phrase 'hello how are you' was converted to speech.")
    else:
        print("❌ Demo failed!")
        print("Check the error messages above for details.")
    print("="*60)
    
    return 0 if success else 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)