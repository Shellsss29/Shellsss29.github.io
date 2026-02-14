from PIL import Image, ImageDraw, ImageFont
import os

# Create vibrant LinkedIn thumbnail
width, height = 1200, 630
image = Image.new('RGB', (width, height), '#ffffff')
draw = ImageDraw.Draw(image)

# Vibrant gradient background - blue to purple
for y in range(height):
    ratio = y / height
    r = int(59 + (139 - 59) * ratio)   # 59 to 139
    g = int(130 - (80) * ratio)         # 130 to 50
    b = int(246 - (12) * ratio)         # 246 to 234
    draw.rectangle([(0, y), (width, y + 1)], fill=(r, g, b))

# Large colorful accent circles
draw.ellipse([(-150, -150), (350, 350)], fill='#FF3B30')      # Apple Red
draw.ellipse([(850, -100), (1400, 450)], fill='#FF9500')      # Apple Orange
draw.ellipse([(-100, 300), (300, 700)], fill='#34C759')       # Apple Green
draw.ellipse([(900, 400), (1350, 850)], fill='#FFD60A')       # Apple Yellow

# White content card
overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
overlay_draw = ImageDraw.Draw(overlay)
overlay_draw.rounded_rectangle([(100, 80), (1100, 550)], radius=30, fill=(255, 255, 255, 245))
image.paste(overlay, (0, 0), overlay)

# Add shadow
shadow_overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
shadow_draw = ImageDraw.Draw(shadow_overlay)
shadow_draw.rounded_rectangle([(100, 80), (1100, 550)], radius=30, fill=(0, 0, 0, 40))
image.paste(shadow_overlay, (5, 5), shadow_overlay)

# White card on top
draw.rounded_rectangle([(100, 80), (1100, 550)], radius=30, fill='#ffffff')

# Colorful top bar
draw.rounded_rectangle([(100, 80), (1100, 130)], radius=30, fill='#007AFF')
draw.rectangle([(100, 110), (1100, 130)], fill='#007AFF')  # Fill bottom

# Load fonts
try:
    title_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 52)
    emoji_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 80)
    subtitle_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 28)
    author_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 26)
except:
    title_font = ImageFont.load_default()
    emoji_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()
    author_font = ImageFont.load_default()

# Top bar text
draw.text((600, 105), "APPLE PHOTOS PROBLEM", font=subtitle_font, fill='#ffffff', anchor='mm')

# Large visual story in center
y_center = 280

# 1 person
draw.text((250, y_center), "1", font=emoji_font, fill='#007AFF', anchor='mm')
draw.text((320, y_center), "👤", font=emoji_font, anchor='mm')

# Arrow
draw.text((480, y_center), "→", font=title_font, fill='#86868b', anchor='mm')

# 5 people
draw.text((620, y_center), "5", font=emoji_font, fill='#FF3B30', anchor='mm')
draw.text((720, y_center - 30), "👥", font=subtitle_font, anchor='mm')
draw.text((720, y_center), "👥", font=subtitle_font, anchor='mm')
draw.text((720, y_center + 30), "👥", font=subtitle_font, anchor='mm')
draw.text((780, y_center - 15), "👥", font=subtitle_font, anchor='mm')
draw.text((780, y_center + 15), "👥", font=subtitle_font, anchor='mm')

# Question mark
draw.text((920, y_center), "❓", font=emoji_font, anchor='mm')

# Main title below
draw.text((600, 390), "Why This Happens", font=title_font, fill='#1d1d1f', anchor='mm')
draw.text((600, 445), "& How to Fix It", font=title_font, fill='#1d1d1f', anchor='mm')

# Bottom section with colorful boxes
# Key insight box
draw.rounded_rectangle([(150, 480), (580, 530)], radius=15, fill='#34C759')
draw.text((365, 505), "💡 Solution from Research", font=author_font, fill='#ffffff', anchor='mm')

# Author box
draw.rounded_rectangle([(620, 480), (1050, 530)], radius=15, fill='#5856D6')
draw.text((835, 505), "👤 by Shailly Bhati", font=author_font, fill='#ffffff', anchor='mm')

# Save
output_path = 'images/blog-thumbnail.png'
image.save(output_path, 'PNG', quality=95)

print(f"✅ Vibrant LinkedIn thumbnail created!")
print(f"📐 Size: {width}x{height}px")
print(f"🎨 Super colorful with Apple red, orange, green, yellow, blue, purple!")
print(f"✨ This will definitely stand out on LinkedIn!")
