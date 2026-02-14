from PIL import Image, ImageDraw, ImageFont
import os

# Create image with modern design
width, height = 1200, 630
image = Image.new('RGB', (width, height), '#ffffff')
draw = ImageDraw.Draw(image)

# Modern gradient background - vibrant electric blue to purple
for y in range(height):
    # Create smooth gradient
    ratio = y / height
    r = int(79 + (147 - 79) * ratio)  # 79 to 147
    g = int(70 + (51 - 70) * ratio)   # 70 to 51
    b = int(229 + (234 - 229) * ratio) # 229 to 234
    draw.rectangle([(0, y), (width, y + 1)], fill=(r, g, b))

# Add large decorative circles for depth
# Top left - bright cyan
draw.ellipse([(-150, -150), (400, 400)], fill='#06b6d4')
# Top right - yellow/orange
draw.ellipse([(850, -100), (1350, 400)], fill='#fbbf24')
# Bottom left - pink
draw.ellipse([(-100, 350), (350, 800)], fill='#ec4899')
# Bottom right - green
draw.ellipse([(900, 350), (1400, 850)], fill='#10b981')

# Add white card overlay for content
overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
overlay_draw = ImageDraw.Draw(overlay)
# Rounded rectangle effect with shadow
overlay_draw.rectangle([(80, 80), (1120, 550)], fill=(255, 255, 255, 250))
image.paste(overlay, (0, 0), overlay)

# Add subtle shadow effect
shadow = Image.new('RGBA', (width, height), (0, 0, 0, 0))
shadow_draw = ImageDraw.Draw(shadow)
shadow_draw.rectangle([(85, 85), (1125, 555)], fill=(0, 0, 0, 30))
image.paste(shadow, (0, 0), shadow)

# Final white card
draw.rectangle([(80, 80), (1120, 550)], fill='#ffffff')

# Add colorful accent bar at top
draw.rectangle([(80, 80), (1120, 100)], fill='#3b82f6')

# Load fonts
try:
    title_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 68)
    number_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 110)
    subtitle_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 34)
    author_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 30)
    tag_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 22)
except:
    title_font = ImageFont.load_default()
    number_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()
    author_font = ImageFont.load_default()
    tag_font = ImageFont.load_default()

# Eye-catching emoji and number
draw.text((200, 230), "👤", font=number_font, anchor='mm')
draw.text((380, 230), "→", font=subtitle_font, fill='#6b7280', anchor='mm')
draw.text((600, 230), "5", font=number_font, fill='#3b82f6', anchor='mm')
draw.text((700, 230), "👥", font=number_font, anchor='mm')
draw.text((950, 230), "❓", font=number_font, anchor='mm')

# Main title
draw.text((600, 350), "Why Apple Photos", font=title_font, fill='#0f172a', anchor='mm')
draw.text((600, 420), "Thinks You're 5 People", font=title_font, fill='#1e293b', anchor='mm')

# Bottom section with gradient text effect
draw.text((200, 500), "📸 Facial Recognition Problem", font=tag_font, fill='#6366f1', anchor='lm')
draw.text((750, 500), "💡 Context-Aware Solution", font=tag_font, fill='#8b5cf6', anchor='lm')

# Author badge at bottom right
draw.rectangle([(850, 465), (1080, 525)], fill='#f3f4f6', outline='#3b82f6', width=2)
draw.text((965, 495), "Shailly Bhati", font=author_font, fill='#0f172a', anchor='mm')

# Save image
output_path = '/Users/shailly/Desktop/portfolio-website/images/blog-thumbnail.png'
image.save(output_path, 'PNG', quality=95)

print(f"✅ Professional LinkedIn thumbnail created: {output_path}")
print(f"📐 Size: {width}x{height}px")
print(f"🎨 Modern design with vibrant colors and emojis")
print(f"✨ Perfect for standing out in LinkedIn feed!")
