# Lichess YouTube Automation V2

Automated pipeline that converts Lichess puzzles into chess tactic videos and YouTube Shorts.

Pipeline:

Lichess Puzzle → Stockfish validation → Board animation → Script → Voice → Video → Thumbnail → YouTube Upload

## Features

- Fetch puzzles from Lichess
- Render animated chess boards
- Validate tactics using Stockfish
- Generate narration
- Build long videos and Shorts
- Automated GitHub Actions execution

## Repository layout

- `scripts/` contains the canonical implementation of each pipeline stage and the executable `scripts/pipeline.py` entrypoint.
- `.github/workflows/daily_generation.yml` schedules the pipeline; no other root-level workflow files are maintained.
- Supporting artifacts such as generated videos/shorts/thumbnails are excluded via `.gitignore`.

## Setup

1. Install dependencies

   ```sh
   pip install -r requirements.txt
   ```

2. Install Stockfish

   Download Stockfish and place the binary in `engine/stockfish`.

3. Configure environment

   ```sh
   cp .env.example .env
   ```

## Running the pipeline

Invoke the only supported entrypoint:

```sh
python scripts/pipeline.py
```
