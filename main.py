import edge_tts
import asyncio
import time
from pathlib import Path


LANGUAGES = {
    "1": ("English", "en"),
    "2": ("Spanish", "es"),
}


def prompt(message, default=None):
    suffix = f" [{default}]" if default else ""
    value = input(f"{message}{suffix}: ").strip()
    return value or (default or "")


def pick_language():
    print("\n🌐 Select a language:")
    for key, (name, _) in LANGUAGES.items():
        print(f"  {key}. {name}")
    while True:
        choice = prompt("Enter choice", "1")
        if choice in LANGUAGES:
            return LANGUAGES[choice][1]
        print("❌ Invalid choice. Try again.")


async def pick_voice(language_prefix):
    print(f"\n🔎 Fetching {language_prefix.upper()} voices...")
    all_voices = await edge_tts.list_voices()
    voices = sorted(
        [v for v in all_voices if v["Locale"].lower().startswith(language_prefix + "-")],
        key=lambda v: (v["Locale"], v["ShortName"]),
    )

    if not voices:
        raise RuntimeError(f"No voices found for language '{language_prefix}'.")

    print(f"\n🎙️ Available voices ({len(voices)}):")
    for idx, v in enumerate(voices, start=1):
        gender = v.get("Gender", "")
        print(f"  {idx:>3}. {v['ShortName']:<40} ({v['Locale']}, {gender})")

    while True:
        choice = prompt("Enter voice number", "1")
        if choice.isdigit() and 1 <= int(choice) <= len(voices):
            return voices[int(choice) - 1]["ShortName"]
        print("❌ Invalid choice. Try again.")


def pick_script_file():
    txt_files = sorted(Path(".").glob("*.txt"))
    if txt_files:
        print("\n📄 Available .txt files:")
        for idx, f in enumerate(txt_files, start=1):
            print(f"  {idx}. {f.name}")
        print("  0. Enter a custom path")
        while True:
            choice = prompt("Select a file", "1")
            if choice == "0":
                break
            if choice.isdigit() and 1 <= int(choice) <= len(txt_files):
                return txt_files[int(choice) - 1]
            print("❌ Invalid choice. Try again.")

    while True:
        path = prompt("Enter path to .txt file")
        p = Path(path)
        if p.exists() and p.is_file():
            return p
        print("❌ File not found. Try again.")


def pick_output_name():
    name = prompt("Enter output name (without extension)", "voiceover")
    if not name.lower().endswith(".mp3"):
        name += ".mp3"
    return name


async def generate_voiceover():
    language_prefix = pick_language()
    voice = await pick_voice(language_prefix)
    script_file = pick_script_file()
    output_file = pick_output_name()

    text = script_file.read_text(encoding="utf-8").strip()
    if not text:
        print(f"❌ Error: {script_file} is empty!")
        return

    print("\n📝 Script loaded successfully")
    print(f"📊 Text length: {len(text)} characters")
    print(f"🎯 Voice: {voice}")
    print(f"📁 Output: {output_file}")
    print("🎙️ Generating voiceover...")

    start_time = time.time()
    try:
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output_file)
    except Exception as e:
        print(f"❌ TTS Error: {e}")
        return

    elapsed_time = time.time() - start_time
    print(f"\n✅ Voiceover generated successfully!")
    print(f"📁 Saved to: {output_file}")
    print(f"⏱️ Time taken: {elapsed_time:.2f} seconds")


def main():
    print("=" * 50)
    print("🎤 Edge TTS Voiceover Generator")
    print("=" * 50)

    try:
        asyncio.run(generate_voiceover())
    except KeyboardInterrupt:
        print("\n\n⚠️ Cancelled by user.")
    except Exception as e:
        print(f"\n❌ Error occurred: {str(e)}")

    print("=" * 50)


if __name__ == "__main__":
    main()
