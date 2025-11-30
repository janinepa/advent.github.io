import os
import re

doors_dir = 'src/doors'
generator_script = 'src/scripts/generate_doors.py'

print("Starting batch update for posters...")

# 1. Update all door files
for filename in os.listdir(doors_dir):
    if filename.startswith('day-') and filename.endswith('.html'):
        filepath = os.path.join(doors_dir, filename)
        day_str = filename.replace('day-', '').replace('.html', '')
        
        with open(filepath, 'r') as f:
            content = f.read()

        original_content = content
        
        # Add poster attribute and change preload
        # Find <video ...>
        # We want to add poster="../assets/images/posters/day-XX.jpg"
        # And change preload="auto" (or true) to preload="metadata"
        
        if 'poster=' not in content:
            poster_attr = f'poster="../assets/images/posters/day-{day_str}.jpg"'
            content = re.sub(r'(<video[^>]*?)>', f'\\1 {poster_attr}>', content)
            print(f"  Added poster to {filename}")

        if 'preload="auto"' in content:
            content = content.replace('preload="auto"', 'preload="metadata"')
            print(f"  Updated preload to metadata in {filename}")
        elif 'preload="true"' in content:
            content = content.replace('preload="true"', 'preload="metadata"')
            print(f"  Updated preload to metadata in {filename}")

        if content != original_content:
            with open(filepath, 'w') as f:
                f.write(content)
            print(f"Saved updates to {filename}")
        else:
            print(f"No changes needed for {filename}")

# 2. Update generator script
with open(generator_script, 'r') as f:
    content = f.read()

original_content = content

# Update template video tag
# Look for the line with <video ...>
if 'poster=' not in content:
    # We need to insert poster attribute dynamically
    # The template likely has {day_str} available
    content = re.sub(r'(<video[^>]*?)>', r'\1 poster="../assets/images/posters/day-{day_str}.jpg">', content)

if 'preload="auto"' in content:
    content = content.replace('preload="auto"', 'preload="metadata"')

if content != original_content:
    with open(generator_script, 'w') as f:
        f.write(content)
    print(f"Updated {generator_script}")
else:
    print(f"No changes needed for {generator_script}")

print("Batch update complete.")
