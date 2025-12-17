#!/usr/bin/env python3
import asyncio
import edge_tts
import json
import os
from pathlib import Path

# Japanese female voice
VOICE = "ja-JP-NanamiNeural"

# Data files to process (non-template files)
DATA_FILES = [
    "meg-selv",
    "mat",
    "tog",
    "italia",
    "hiroshima",
    "daglige-rutiner",
    "hjemme",
    "skole",
    "jobb",
    "familie"
]

async def generate_audio_for_text(text: str, output_path: str):
    """Generate audio file for given text using Edge TTS."""
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(output_path)
    print(f"Generated: {output_path}")

async def process_data_file(category: str):
    """Process a single data file and generate audio for all sentences and words."""
    json_path = Path(f"src/data/{category}.json")

    if not json_path.exists():
        print(f"Skipping {category} - file not found")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Create category directory
    audio_dir = Path(f"public/audio/{category}")
    audio_dir.mkdir(parents=True, exist_ok=True)

    # Process each sentence
    for sentence in data.get('sentences', []):
        sentence_id = sentence['id']
        words = sentence['words']

        # Build full sentence text from kanji
        full_text = ''.join([word['kanji'] for word in words])

        # Generate audio for full sentence
        sentence_audio_path = audio_dir / f"{sentence_id}.mp3"
        if not sentence_audio_path.exists():
            await generate_audio_for_text(full_text, str(sentence_audio_path))

        # Generate audio for individual words
        for word_index, word in enumerate(words):
            word_text = word['kanji']
            romaji = word.get('romaji', '').lower()
            if word_text and romaji:  # Skip empty kanji or romaji
                word_audio_path = audio_dir / f"{sentence_id}-{romaji}.mp3"
                if not word_audio_path.exists():
                    await generate_audio_for_text(word_text, str(word_audio_path))

async def main():
    """Main function to generate all audio files."""
    print("Starting audio generation with voice:", VOICE)
    print("=" * 60)

    for category in DATA_FILES:
        print(f"\nProcessing category: {category}")
        print("-" * 60)
        await process_data_file(category)

    print("\n" + "=" * 60)
    print("Audio generation completed!")

if __name__ == "__main__":
    asyncio.run(main())
