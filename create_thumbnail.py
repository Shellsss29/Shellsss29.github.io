from PIL import Image, ImageDraw, ImageFont
import os

# Create image with gradient background
width, height = 1200, 630  # LinkedIn recommended size
image = Image.new('RGB', (width, height), '#0f172a')  # Dark blue background

# Create gradient effect
draw = ImageDraw.Draw(image)

# Draw gradient circles for visual effect
for i in range(0, width, 50):
    alpha = int(255 * (1 - i/width))
    color = f'#{hex(59)[2:].zfill(2)}{hex(130)[2:].zfill(2)}{hex(246)[2:].zfill(2)}'  # Blue

# Simple colored rectangles for design
# Top left accent
draw.rectangle([(0, 0), (400, 200)], fill='#3b82f6', outline=None)
draw.rectangle([(0, 0), (400, 200)], fill='#1e293b')  # Overlay

# Bottom right accent
draw.rectangle([(800, 430), (1200, 630)], fill='#8b5cf6', outline=None)
draw.rectangle([(800, 430), (1200, 630)], fill='#1e293b')  # Overlay

# Add text
try:
    # Try to use a system font
    title_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 80)
    subtitle_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 40)
    small_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 30)
except:
    # Fallback to default font
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()
    small_font = ImageFont.load_default()

# Main text
draw.text((600, 220), "SHAILLY BHATI", font=title_font, fill='#ffffff', anchor='mm')
draw.text((600, 310), "Software Engineer Portfolio", font=subtitle_font, fill='#94a3b8', anchor='mm')

# Tech stack
tech_text = "AI • ML • LLM • Python • FastAPI • MLOps"
draw.text((600, 380), tech_text, font=small_font, fill='#3b82f6', anchor='mm')

# URL
draw.text((600, 480), "shellsss29.github.io", font=subtitle_font, fill='#06b6d4', anchor='mm')

# Add decorative elements
# Top line
draw.rectangle([(200, 160), (1000, 165)], fill='#3b82f6')

# Bottom line
draw.rectangle([(200, 520), (1000, 525)], fill='#8b5cf6')

# Save image
output_path = '/Users/shailly/Desktop/portfolio-website/images/portfolio-thumbnail.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
image.save(output_path, 'PNG', quality=95)

print(f"✅ Thumbnail created: {output_path}")
print(f"📐 Size: {width}x{height}px (Perfect for LinkedIn)")
