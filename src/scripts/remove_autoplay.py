import os
import re

doors_dir = 'src/doors'
generator_script = 'src/scripts/generate_doors.py'

print("Starting removal of autoplay logic...")

# 1. Update all door files
for filename in os.listdir(doors_dir):
    if filename.startswith('day-') and filename.endswith('.html'):
        filepath = os.path.join(doors_dir, filename)
        with open(filepath, 'r') as f:
            content = f.read()

        original_content = content
        
        # Remove JS autoplay assignment
        # Pattern: video.autoplay = true;
        content = re.sub(r'\s*video\.autoplay\s*=\s*true;', '', content)
        
        # Remove video.play() if present (just in case)
        content = re.sub(r'\s*video\.play\(\)(\.catch\(.*?\))?;', '', content, flags=re.DOTALL)

        # Ensure video tag does NOT have autoplay attribute
        if 'autoplay' in content:
            content = re.sub(r'(<video[^>]*?)\s+autoplay', r'\1', content)

        if content != original_content:
            with open(filepath, 'w') as f:
                f.write(content)
            print(f"Removed autoplay from {filename}")
        else:
            print(f"No autoplay logic found in {filename}")

# 2. Update generator script
with open(generator_script, 'r') as f:
    content = f.read()

original_content = content
content = re.sub(r'\s*video\.autoplay\s*=\s*true;', '', content)
content = re.sub(r'(<video[^>]*?)\s+autoplay', r'\1', content)

if content != original_content:
    with open(generator_script, 'w') as f:
        f.write(content)
    print(f"Updated {generator_script}")
else:
    print(f"No changes needed for {generator_script}")

print("Batch update complete.")
