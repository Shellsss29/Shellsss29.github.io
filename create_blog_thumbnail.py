from PIL import Image, ImageDraw, ImageFont
import os

# Create image with vibrant gradient background
width, height = 1200, 630
image = Image.new('RGB', (width, height), '#ffffff')

# Create gradient effect with vibrant colors
draw = ImageDraw.Draw(image)

# Vibrant gradient background - blue to purple
for i in range(height):
    r = int(59 + (139 - 59) * (i / height))
    g = int(130 - (38) * (i / height))
    b = int(246 - (0) * (i / height))
    draw.rectangle([(0, i), (width, i + 1)], fill=(r, g, b))

# Add accent shapes for visual interest
# Top left circle
draw.ellipse([(-100, -100), (300, 300)], fill='#06b6d4', outline=None)
# Bottom right circle
draw.ellipse([(900, 400), (1350, 850)], fill='#f59e0b', outline=None)

# Semi-transparent overlay for readability
overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
overlay_draw = ImageDraw.Draw(overlay)
overlay_draw.rectangle([(50, 100), (1150, 530)], fill=(255, 255, 255, 240))
image.paste(overlay, (0, 0), overlay)

# Add text
try:
    title_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 65)
    subtitle_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 32)
    author_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 28)
    tag_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 24)
except:
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()
    author_font = ImageFont.load_default()
    tag_font = ImageFont.load_default()

# Main title (multi-line with vibrant color)
title_line1 = "Why Apple Photos"
title_line2 = "Thinks You're"
title_line3 = "5 Different People"

draw.text((600, 180), title_line1, font=title_font, fill='#1e293b', anchor='mm')
draw.text((600, 260), title_line2, font=title_font, fill='#1e293b', anchor='mm')
draw.text((600, 340), title_line3, font=title_font, fill='#3b82f6', anchor='mm')

# Emoji/Icon indicator
draw.text((150, 340), "📸", font=title_font, anchor='mm')
draw.text((1050, 340), "🤔", font=title_font, anchor='mm')

# Subtitle with accent color
draw.text((600, 420), "Facial Recognition Problem & Solution", font=subtitle_font, fill='#6366f1', anchor='mm')

# Author name
draw.text((600, 480), "by Shailly Bhati", font=author_font, fill='#0f172a', anchor='mm')

# Tags at bottom
tag_text = "#FacialRecognition  #MachineLearning  #ComputerVision"
draw.text((600, 520), tag_text, font=tag_font, fill='#8b5cf6', anchor='mm')

# Decorative accents
# Top accent bar
draw.rectangle([(50, 130), (1150, 135)], fill='#3b82f6')
# Bottom accent bar
draw.rectangle([(50, 495), (1150, 500)], fill='#8b5cf6')

# Save image
output_path = '/Users/shailly/Desktop/portfolio-website/images/blog-thumbnail.png'
image.save(output_path, 'PNG', quality=95)

print(f"✅ Vibrant blog thumbnail created: {output_path}")
print(f"📐 Size: {width}x{height}px (Perfect for LinkedIn)")
print(f"🎨 Using bright gradient with blue, purple, cyan, and orange accents")
