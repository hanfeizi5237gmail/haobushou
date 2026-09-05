#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "$0")" && pwd)"
output_dir="$script_dir/video"

mkdir -p "$output_dir"
node "$script_dir/render-social-assets.mjs"
python3 "$script_dir/render-social-video.py"

printf 'Created %s\n' "$output_dir/haobushou-social-24s-silent.mp4"
