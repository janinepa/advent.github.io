#!/bin/bash

# Directory containing videos
VIDEO_DIR="src/assets/videos"

echo "Compressing videos in $VIDEO_DIR for mobile optimization..."

for file in "$VIDEO_DIR"/*.mp4; do
    if [ -f "$file" ]; then
        echo "Processing $file..."
        temp_file="${file%.mp4}_temp.mp4"
        
        # Compress using H.264 with CRF 28 (good quality, smaller size)
        # -preset medium: balance between encoding speed and compression
        # -movflags +faststart: optimize for web streaming
        # -pix_fmt yuv420p: ensure compatibility
        ffmpeg -y -i "$file" -vcodec libx264 -crf 28 -preset medium -movflags +faststart -pix_fmt yuv420p "$temp_file" < /dev/null
        
        if [ $? -eq 0 ]; then
            # Check if new file is actually smaller
            orig_size=$(stat -f%z "$file")
            new_size=$(stat -f%z "$temp_file")
            
            if [ $new_size -lt $orig_size ]; then
                mv "$temp_file" "$file"
                echo "Compressed $file: $orig_size -> $new_size bytes"
            else
                echo "New file not smaller, keeping original: $file"
                rm "$temp_file"
            fi
        else
            echo "Error processing $file"
            rm "$temp_file"
        fi
    fi
done

echo "Compression complete!"
