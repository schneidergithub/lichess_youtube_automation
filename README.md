
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

## Setup

### 1 Install dependencies

pip install -r requirements.txt

### 2 Install Stockfish

Download Stockfish and place binary in:

engine/stockfish

### 3 Configure environment

cp .env.example .env

### 4 Run pipeline

python scripts/pipeline.py

### 5 Run automation

GitHub workflow automatically generates videos.

