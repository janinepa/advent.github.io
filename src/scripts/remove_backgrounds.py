import os
import re

doors_dir = 'src/doors'
generator_script = 'src/scripts/generate_doors.py'

print("Starting removal of background images...")

# 1. Update all door files
for filename in os.listdir(doors_dir):
    if filename.startswith('day-') and filename.endswith('.html'):
        filepath = os.path.join(doors_dir, filename)
        with open(filepath, 'r') as f:
            content = f.read()

        original_content = content
        
        # Remove background line in body style
        # Matches: background: url('../assets/images/background.webp') center/cover no-repeat;
        # We'll use a regex to be safe about whitespace
        content = re.sub(r'\s*background:\s*url\([\'"].*?background\.webp[\'"]\).*?;', '', content)

        if content != original_content:
            with open(filepath, 'w') as f:
                f.write(content)
            print(f"Removed background from {filename}")
        else:
            print(f"No background found in {filename}")

# 2. Update generator script
with open(generator_script, 'r') as f:
    content = f.read()

original_content = content
content = re.sub(r'\s*background:\s*url\([\'"].*?background\.webp[\'"]\).*?;', '', content)

if content != original_content:
    with open(generator_script, 'w') as f:
        f.write(content)
    print(f"Updated {generator_script}")
else:
    print(f"No changes needed for {generator_script}")

print("Batch update complete.")
