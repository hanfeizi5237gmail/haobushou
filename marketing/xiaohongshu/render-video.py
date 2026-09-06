"""Render the XHS editorial cards only; no contact or sales assets are used."""

from pathlib import Path

import cv2
import numpy as np


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "haobushou-xhs-checklist-32s-silent.mp4"
CARDS = ("01-cover.png", "02-source.png", "03-local.png", "04-export.png")
SIZE = (1080, 1920)
FPS = 30
FRAMES_PER_CARD = 8 * FPS
FADE_FRAMES = 12


def load_card(path: Path) -> np.ndarray:
    card = cv2.imread(str(path), cv2.IMREAD_COLOR)
    if card is None:
        raise FileNotFoundError(path)
    if card.shape[:2] != (1440, 1080):
        raise ValueError(f"Expected a 1080x1440 editorial card: {path.name}")
    # Keep the complete 3:4 artwork above the lower platform controls.
    canvas = np.full((1920, 1080, 3), (233, 242, 245), dtype=np.uint8)
    canvas[180:1460, 60:1020] = cv2.resize(
        card, (960, 1280), interpolation=cv2.INTER_AREA
    )
    return canvas


def main() -> None:
    cards = [load_card(ROOT / name) for name in CARDS]
    writer = cv2.VideoWriter(str(OUTPUT), cv2.VideoWriter_fourcc(*"avc1"), FPS, SIZE)
    if not writer.isOpened():
        raise RuntimeError("H.264 writer unavailable")
    try:
        for index, card in enumerate(cards):
            for _ in range(FRAMES_PER_CARD - FADE_FRAMES):
                writer.write(card)
            for frame in range(FADE_FRAMES):
                if index == len(cards) - 1:
                    writer.write(card)
                else:
                    amount = (frame + 1) / FADE_FRAMES
                    writer.write(cv2.addWeighted(card, 1 - amount, cards[index + 1], amount, 0))
    finally:
        writer.release()
    print(f"Created {OUTPUT}")


if __name__ == "__main__":
    main()
