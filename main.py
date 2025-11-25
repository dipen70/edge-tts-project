
import edge_tts
import asyncio
import time
from pathlib import Path

async def generate_voiceover():
    """
    Generate voiceover from script.txt using Edge TTS with Brian multilingual voice
    """
    # Start timing
    start_time = time.time()
    
    # Read the script file
    script_file = Path("script.txt")
    
    if not script_file.exists():
        print("❌ Error: script.txt file not found!")
        return
    
    with open(script_file, 'r', encoding='utf-8') as f:
        text = f.read().strip()
    
    if not text:
        print("❌ Error: script.txt is empty!")
        return
    
    print("📝 Script loaded successfully")
    print(f"📊 Text length: {len(text)} characters")
    print("🎙️  Generating voiceover with Brian multilingual voice...")
    
    # Voice: en-US-BrianMultilingualNeural
    voice = "en-US-BrianMultilingualNeural"
    
    # Output file
    output_file = "voiceover.mp3"
    
    # Generate speech
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)
    
    # End timing
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    # Display results
    print(f"\n✅ Voiceover generated successfully!")
    print(f"📁 Saved to: {output_file}")
    print(f"⏱️  Time taken: {elapsed_time:.2f} seconds")
    print(f"🎯 Voice used: {voice}")

def main():
    """
    Main function to run the voiceover generator
    """
    print("=" * 50)
    print("🎤 Edge TTS Voiceover Generator")
    print("=" * 50)
    
    try:
        # Run the async function
        asyncio.run(generate_voiceover())
    except Exception as e:
        print(f"\n❌ Error occurred: {str(e)}")
    
    print("=" * 50)

if __name__ == "__main__":
    main()