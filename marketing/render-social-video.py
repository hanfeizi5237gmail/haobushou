"""Build a short, silent portrait demo from the approved social cards.

The source cards already contain the Chinese copy and real product screenshots;
this script only adds timing and restrained cross-fades. No product UI is
generated or rewritten.
"""

from pathlib import Path

import cv2
import numpy as np


ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
OUTPUT = ROOT / "video" / "haobushou-social-24s-silent.mp4"
SIZE = (1080, 1920)
FPS = 30
SECONDS_PER_CARD = 4
FADE_FRAMES = 12
CARD_NAMES = (
    "douyin-cover.png",
    "xhs-workflow.png",
    "xhs-proof.png",
    "xhs-export.png",
    "xhs-pricing.png",
    "xhs-cover.png",
)


def read_card(name: str) -> np.ndarray:
    image = cv2.imread(str(ASSETS / name), cv2.IMREAD_COLOR)
    if image is None:
        raise FileNotFoundError(ASSETS / name)
    height, width = image.shape[:2]
    scale = min(SIZE[0] / width, SIZE[1] / height)
    resized = cv2.resize(
        image,
        (round(width * scale), round(height * scale)),
        interpolation=cv2.INTER_AREA,
    )
    # Match the card's background and letterbox without distorting screenshots.
    canvas = np.empty((SIZE[1], SIZE[0], 3), dtype=np.uint8)
    canvas[:] = image[0, 0]
    left = (SIZE[0] - resized.shape[1]) // 2
    top = (SIZE[1] - resized.shape[0]) // 2
    canvas[top : top + resized.shape[0], left : left + resized.shape[1]] = resized
    return canvas


def main() -> None:
    cards = [read_card(name) for name in CARD_NAMES]
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    writer = cv2.VideoWriter(
        str(OUTPUT),
        cv2.VideoWriter_fourcc(*"avc1"),
        FPS,
        SIZE,
    )
    if not writer.isOpened():
        raise RuntimeError("OpenCV could not open an H.264 MP4 writer")

    still_frames = SECONDS_PER_CARD * FPS - FADE_FRAMES
    for index, card in enumerate(cards):
        for _ in range(still_frames):
            writer.write(card)
        if index == len(cards) - 1:
            for _ in range(FADE_FRAMES):
                writer.write(card)
            continue
        next_card = cards[index + 1]
        for step in range(1, FADE_FRAMES + 1):
            amount = step / FADE_FRAMES
            blended = cv2.addWeighted(card, 1 - amount, next_card, amount, 0)
            writer.write(blended.astype(np.uint8))
    writer.release()
    print(f"Created {OUTPUT}")


if __name__ == "__main__":
    main()
