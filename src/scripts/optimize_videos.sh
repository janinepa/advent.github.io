#!/bin/bash

# Directory containing videos
VIDEO_DIR="src/assets/videos"

echo "Optimizing videos in $VIDEO_DIR for web streaming (faststart)..."

for file in "$VIDEO_DIR"/*.mp4; do
    if [ -f "$file" ]; then
        echo "Processing $file..."
        temp_file="${file%.mp4}_temp.mp4"
        
        # Run ffmpeg to move moov atom to the front
        ffmpeg -y -i "$file" -c copy -movflags +faststart "$temp_file" < /dev/null
        
        if [ $? -eq 0 ]; then
            mv "$temp_file" "$file"
            echo "Successfully optimized $file"
        else
            echo "Error processing $file"
            rm "$temp_file"
        fi
    fi
done

echo "Optimization complete!"
