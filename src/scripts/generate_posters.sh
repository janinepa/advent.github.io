#!/bin/bash

# Directory containing videos
VIDEO_DIR="../assets/videos"
# Directory to save posters
POSTER_DIR="../assets/images/posters"

# Create poster directory if it doesn't exist
mkdir -p "$POSTER_DIR"

echo "Generating posters..."

for video in "$VIDEO_DIR"/*.mp4; do
    if [ -f "$video" ]; then
        filename=$(basename -- "$video")
        name="${filename%.*}"
        poster="$POSTER_DIR/$name.jpg"

        # Extract first frame as jpg
        # -ss 00:00:00 : Seek to start
        # -vframes 1 : Output 1 frame
        # -q:v 2 : High quality jpg
        ffmpeg -y -i "$video" -ss 00:00:00 -vframes 1 -q:v 2 "$poster" >/dev/null 2>&1

        if [ $? -eq 0 ]; then
            echo "Created poster: $poster"
        else
            echo "Failed to create poster for $filename"
        fi
    fi
done

echo "Poster generation complete."
