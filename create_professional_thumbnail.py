from PIL import Image, ImageDraw, ImageFont
import os

# Create professional blue/black LinkedIn thumbnail
width, height = 1200, 630
image = Image.new('RGB', (width, height), '#0f172a')  # Dark background
draw = ImageDraw.Draw(image)

# Subtle blue gradient background
for y in range(height):
    ratio = y / height
    r = int(15 + (0) * ratio)
    g = int(23 + (99) * ratio)
    b = int(42 + (213) * ratio)
    draw.rectangle([(0, y), (width, y + 1)], fill=(r, g, b))

# Large blue accent circle (subtle)
draw.ellipse([(-100, -100), (400, 400)], fill='#1e3a8a')  # Dark blue
draw.ellipse([(800, 200), (1400, 800)], fill='#1e40af')   # Medium blue

# Clean white card
draw.rounded_rectangle([(100, 100), (1100, 530)], radius=20, fill='#ffffff')

# Blue header bar
draw.rounded_rectangle([(100, 100), (1100, 180)], radius=20, fill='#2563eb')
draw.rectangle([(100, 160), (1100, 180)], fill='#2563eb')  # Fill bottom

try:
    title_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 48)
    emoji_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 70)
    subtitle_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 26)
    small_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 22)
except:
    title_font = ImageFont.load_default()
    emoji_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()
    small_font = ImageFont.load_default()

# Header text
draw.text((600, 140), "Apple Photos Problem", font=title_font, fill='#ffffff', anchor='mm')

# Main visual - clean and simple
y_center = 310

# Left: 1 person
draw.ellipse([(200, y_center-60), (360, y_center+60)], fill='#dbeafe', outline='#2563eb', width=4)
draw.text((280, y_center), "1", font=emoji_font, fill='#1e40af', anchor='mm')

# Arrow
draw.text((480, y_center), "→", font=title_font, fill='#64748b', anchor='mm')

# Right: 5 people
positions = [
    (620, y_center-70, 720, y_center-10),
    (620, y_center-25, 720, y_center+35),
    (620, y_center+20, 720, y_center+80),
    (750, y_center-50, 850, y_center+10),
    (750, y_center+5, 850, y_center+65)
]

for x1, y1, x2, y2 in positions:
    draw.ellipse([(x1, y1), (x2, y2)], fill='#fef2f2', outline='#dc2626', width=3)

draw.text((950, y_center), "❌", font=emoji_font, anchor='mm')

# Bottom text
draw.text((600, 450), "Why This Happens & How to Fix It", font=subtitle_font, fill='#1e293b', anchor='mm')

# Footer boxes
draw.rounded_rectangle([(150, 485), (550, 520)], radius=8, fill='#1e40af')
draw.text((350, 502), "Facial Recognition Research", font=small_font, fill='#ffffff', anchor='mm')

draw.rounded_rectangle([(650, 485), (1050, 520)], radius=8, fill='#334155')
draw.text((850, 502), "by Shailly Bhati", font=small_font, fill='#ffffff', anchor='mm')

# Save
output_path = 'images/apple-photos-og-image.png'
image.save(output_path, 'PNG', quality=95)

print(f"✅ Professional blue/black thumbnail created!")
print(f"📐 Size: {width}x{height}px")
print(f"🎨 Clean design: Blue header, white card, dark background")
print(f"✨ Professional and subtle!")
