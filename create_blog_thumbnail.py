from PIL import Image, ImageDraw, ImageFont
import os

# Create image with gradient background
width, height = 1200, 630  # LinkedIn/Twitter recommended size
image = Image.new('RGB', (width, height), '#0f172a')  # Dark blue background

# Create gradient effect
draw = ImageDraw.Draw(image)

# Background rectangles for design
draw.rectangle([(0, 0), (500, 250)], fill='#3b82f6')  # Blue top left
draw.rectangle([(0, 0), (500, 250)], fill='#1e293b')  # Overlay

draw.rectangle([(700, 380), (1200, 630)], fill='#8b5cf6')  # Purple bottom right
draw.rectangle([(700, 380), (1200, 630)], fill='#1e293b')  # Overlay

# Add text
try:
    title_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 70)
    subtitle_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 35)
    small_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 28)
except:
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()
    small_font = ImageFont.load_default()

# Main title (multi-line)
title_line1 = "Why Apple Photos"
title_line2 = "Thinks You're"
title_line3 = "5 Different People"

draw.text((600, 180), title_line1, font=title_font, fill='#ffffff', anchor='mm')
draw.text((600, 260), title_line2, font=title_font, fill='#ffffff', anchor='mm')
draw.text((600, 340), title_line3, font=title_font, fill='#ffffff', anchor='mm')

# Subtitle
draw.text((600, 430), "Facial Recognition Problem & Solution", font=subtitle_font, fill='#94a3b8', anchor='mm')

# Author
draw.text((600, 520), "by Shailly Bhati", font=small_font, fill='#3b82f6', anchor='mm')

# Decorative line
draw.rectangle([(150, 140), (1050, 145)], fill='#3b82f6')
draw.rectangle([(150, 485), (1050, 490)], fill='#8b5cf6')

# Save image
output_path = '/Users/shailly/Desktop/portfolio-website/images/blog-thumbnail.png'
image.save(output_path, 'PNG', quality=95)

print(f"✅ Blog thumbnail created: {output_path}")
print(f"📐 Size: {width}x{height}px (Perfect for LinkedIn & Twitter)")
