import requests
import os
import webbrowser

def generate_and_download_audio(text, language="en", api_url="http://localhost:8005"):
    """
    Generate an audio file from text and download it using the Text-to-Speech API
    
    Args:
        text (str): The text to convert to speech
        language (str, optional): The language code. Defaults to "en".
        api_url (str, optional): The base URL of the API. Defaults to "http://localhost:8005".
        
    Returns:
        str: Path to the downloaded audio file
    """
    # Prepare the request payload
    payload = {
        "text": text,
        "language": language
    }
    
    print(f"Converting text to speech: '{text}'")
    
    # Send request to the API
    response = requests.post(f"{api_url}/text-to-speech", json=payload)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Speech generated successfully: {data['message']}")
        
        # Get the download URL
        download_url = data.get("download_url")
        if not download_url:
            print("Error: Download URL not found in the response")
            return None
            
        # Convert relative URL to absolute URL
        full_download_url = f"{api_url}{download_url}"
        print(f"Download URL: {full_download_url}")
        
        # Create downloads directory if it doesn't exist
        download_dir = "downloads"
        os.makedirs(download_dir, exist_ok=True)
        
        # Download the file
        filename = data.get("filename")
        download_path = os.path.join(download_dir, filename)
        
        print(f"Downloading audio file to {download_path}...")
        audio_response = requests.get(full_download_url)
        
        with open(download_path, "wb") as f:
            f.write(audio_response.content)
            
        print(f"Audio file downloaded successfully to {download_path}")
        
        # Optionally open the file
        print("Opening the audio file...")
        webbrowser.open(download_path)
        
        return download_path
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

if __name__ == "__main__":
    # Example usage
    text = input("Enter the text to convert to speech: ")
    language = input("Enter language code (default is 'en', leave blank for English): ")
    
    if not language:
        language = "en"
        
    generate_and_download_audio(text, language)
