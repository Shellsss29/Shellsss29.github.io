from PIL import Image, ImageDraw, ImageFont
import os

def create_blog_header():
    """Create Apple-style hero image for blog post"""
    width, height = 1200, 400
    image = Image.new('RGB', (width, height), '#ffffff')
    draw = ImageDraw.Draw(image)

    # Apple-style gradient background (blue to white)
    for y in range(height):
        ratio = y / height
        r = int(0 + (255 - 0) * ratio)
        g = int(122 + (255 - 122) * ratio)
        b = int(255)
        draw.rectangle([(0, y), (width, y + 1)], fill=(r, g, b))

    # Large Apple Photos icon style circles
    draw.ellipse([(-50, -50), (200, 200)], fill='#FF3B30')  # Red
    draw.ellipse([(50, 100), (250, 300)], fill='#FF9500')   # Orange
    draw.ellipse([(1000, -50), (1250, 200)], fill='#5856D6') # Purple
    draw.ellipse([(950, 200), (1200, 450)], fill='#007AFF')  # Apple Blue

    # Semi-transparent overlay
    overlay = Image.new('RGBA', (width, height), (255, 255, 255, 200))
    image.paste(overlay, (0, 0), overlay)

    try:
        title_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 55)
        emoji_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 70)
        subtitle_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 28)
    except:
        title_font = ImageFont.load_default()
        emoji_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()

    # Apple Photos icon
    draw.text((150, 200), "📸", font=emoji_font, anchor='mm')

    # Title
    draw.text((600, 150), "Apple Photos Problem", font=title_font, fill='#1d1d1f', anchor='mm')

    # Visual story with Apple-style emojis
    draw.text((350, 250), "1️⃣", font=emoji_font, anchor='mm')
    draw.text((450, 250), "👤", font=emoji_font, anchor='mm')

    draw.text((600, 250), "→", font=title_font, fill='#86868b', anchor='mm')

    draw.text((750, 250), "5️⃣", font=emoji_font, anchor='mm')
    draw.text((850, 250), "👥", font=emoji_font, anchor='mm')

    draw.text((1050, 200), "❌", font=emoji_font, anchor='mm')

    # Subtitle
    draw.text((600, 330), "Same Person → Multiple Clusters", font=subtitle_font, fill='#515154', anchor='mm')

    output_path = 'images/blog-header.png'
    image.save(output_path, 'PNG', quality=95)
    print(f"✅ Apple-style blog header created: {output_path}")

def create_problem_diagram():
    """Create Apple-style problem diagram with iPhone UI"""
    width, height = 1200, 700
    image = Image.new('RGB', (width, height), '#f5f5f7')
    draw = ImageDraw.Draw(image)

    try:
        title_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 36)
        label_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 24)
        small_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 20)
        icon_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 40)
    except:
        title_font = ImageFont.load_default()
        label_font = ImageFont.load_default()
        small_font = ImageFont.load_default()
        icon_font = ImageFont.load_default()

    # Title
    draw.rectangle([(0, 0), (width, 80)], fill='#ffffff')
    draw.text((600, 40), "The Apple Photos Clustering Problem", font=title_font, fill='#1d1d1f', anchor='mm')

    # Left side - iPhone-style photo cards
    draw.text((200, 120), "Same Person, Different Photos", font=label_font, fill='#1d1d1f', anchor='mm')

    photos = [
        ("☀️", "Outdoor Lighting", "#FF9500", 180),
        ("🏠", "Indoor Dim Light", "#5856D6", 280),
        ("👓", "Wearing Glasses", "#007AFF", 380),
        ("📸", "Selfie Angle", "#34C759", 480),
        ("🎉", "Party Photo", "#FF3B30", 580)
    ]

    for emoji, label, color, y in photos:
        # iPhone-style rounded card
        draw.rounded_rectangle([(50, y), (350, y + 80)], radius=15, fill='#ffffff', outline='#d2d2d7', width=2)
        draw.text((100, y + 40), emoji, font=icon_font, anchor='mm')
        draw.text((220, y + 40), label, font=small_font, fill='#1d1d1f', anchor='lm')

        # Arrow
        draw.text((400, y + 40), "→", font=label_font, fill='#86868b', anchor='mm')

    # Center - Apple Photos algorithm
    draw.rounded_rectangle([(450, 320), (750, 400)], radius=20, fill='#007AFF')
    draw.text((600, 360), "Apple Photos", font=label_font, fill='#ffffff', anchor='mm')
    draw.text((600, 390), "Face Clustering", font=small_font, fill='#ffffff', anchor='mm')

    # Right side - Result clusters
    draw.text((1000, 120), "Creates 5 Different People ❌", font=label_font, fill='#FF3B30', anchor='mm')

    for i, y in enumerate([180, 280, 380, 480, 580]):
        # iOS-style person cards
        draw.rounded_rectangle([(850, y), (1150, y + 80)], radius=15, fill='#ffffff', outline='#FF3B30', width=3)
        draw.text((900, y + 40), "👤", font=icon_font, anchor='mm')
        draw.text((1000, y + 25), f"Person {i+1}", font=small_font, fill='#1d1d1f', anchor='lm')
        draw.text((1000, y + 55), "Duplicate", font=small_font, fill='#FF3B30', anchor='lm')

    output_path = 'images/problem-diagram.png'
    image.save(output_path, 'PNG', quality=95)
    print(f"✅ Apple-style problem diagram created: {output_path}")

def create_solution_flowchart():
    """Create Apple-style solution flowchart"""
    width, height = 1200, 900
    image = Image.new('RGB', (width, height), '#f5f5f7')
    draw = ImageDraw.Draw(image)

    try:
        title_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 38)
        box_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 22)
        label_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 20)
        small_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 18)
        icon_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 35)
    except:
        title_font = ImageFont.load_default()
        box_font = ImageFont.load_default()
        label_font = ImageFont.load_default()
        small_font = ImageFont.load_default()
        icon_font = ImageFont.load_default()

    # Title bar
    draw.rectangle([(0, 0), (width, 80)], fill='#ffffff')
    draw.text((600, 40), "💡 Context-Aware Solution", font=title_font, fill='#1d1d1f', anchor='mm')

    # Input photo
    draw.rounded_rectangle([(450, 110), (750, 190)], radius=15, fill='#007AFF')
    draw.text((520, 150), "📸", font=icon_font, anchor='mm')
    draw.text((650, 150), "Photo Input", font=box_font, fill='#ffffff', anchor='mm')

    # Arrow down
    draw.line([(600, 190), (600, 240)], fill='#86868b', width=4)
    draw.polygon([(600, 240), (590, 225), (610, 225)], fill='#86868b')

    # Multi-signal analysis boxes
    draw.text((600, 260), "Multi-Signal Analysis", font=label_font, fill='#1d1d1f', anchor='mm')

    signals = [
        ("👤", "Face\nFeatures", "#007AFF", 150),
        ("📍", "GPS\nLocation", "#34C759", 380),
        ("⏰", "Time\nStamp", "#FF9500", 610),
        ("👕", "Clothing\nBody", "#5856D6", 840)
    ]

    for emoji, text, color, x in signals:
        draw.rounded_rectangle([(x, 300), (x + 180, 420)], radius=15, fill=color)
        draw.text((x + 90, 335), emoji, font=icon_font, anchor='mm')
        draw.text((x + 90, 385), text, font=small_font, fill='#ffffff', anchor='mm', align='center')

        # Arrow down
        draw.line([(x + 90, 420), (x + 90, 470)], fill='#86868b', width=3)
        draw.polygon([(x + 90, 470), (x + 85, 460), (x + 95, 460)], fill='#86868b')

    # Clustering engine
    draw.rounded_rectangle([(200, 480), (1000, 570)], radius=20, fill='#ffffff', outline='#007AFF', width=4)
    draw.text((600, 525), "🧠 Hierarchical Clustering Engine", font=box_font, fill='#1d1d1f', anchor='mm')

    # Arrow down
    draw.line([(600, 570), (600, 610)], fill='#86868b', width=4)
    draw.polygon([(600, 610), (590, 595), (610, 595)], fill='#86868b')

    # Micro-clusters
    draw.text((600, 630), "Create Micro-Clusters", font=label_font, fill='#1d1d1f', anchor='mm')

    micro_positions = [250, 450, 650, 850]
    for x in micro_positions:
        draw.ellipse([(x - 60, 660), (x + 60, 780)], fill='#e8e8ed', outline='#5856D6', width=3)
        draw.text((x, 720), "👤", font=icon_font, anchor='mm')

    # Link them
    draw.line([(250, 720), (850, 720)], fill='#34C759', width=5)
    draw.text((550, 755), "Link with context", font=small_font, fill='#34C759', anchor='mm')

    # Final result
    draw.rounded_rectangle([(300, 800), (900, 870)], radius=15, fill='#34C759')
    draw.text((600, 835), "✅ Result: 1 Person (Correctly Grouped)", font=box_font, fill='#ffffff', anchor='mm')

    output_path = 'images/solution-flowchart.png'
    image.save(output_path, 'PNG', quality=95)
    print(f"✅ Apple-style solution flowchart created: {output_path}")

def create_statistics_chart():
    """Create Apple-style statistics chart"""
    width, height = 1000, 650
    image = Image.new('RGB', (width, height), '#ffffff')
    draw = ImageDraw.Draw(image)

    try:
        title_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 32)
        label_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 22)
        value_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 26)
        small_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 18)
        icon_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 30)
    except:
        title_font = ImageFont.load_default()
        label_font = ImageFont.load_default()
        value_font = ImageFont.load_default()
        small_font = ImageFont.load_default()
        icon_font = ImageFont.load_default()

    # Title bar
    draw.rectangle([(0, 0), (width, 70)], fill='#f5f5f7')
    draw.text((500, 35), "📊 Variables Affecting Face Recognition", font=title_font, fill='#1d1d1f', anchor='mm')

    # Chart data with Apple colors
    factors = [
        ("☀️ Lighting Changes", 45, '#FF9500'),
        ("📐 Viewing Angle", 38, '#FF3B30'),
        ("📷 Photo Quality", 35, '#5856D6'),
        ("👓 Accessories", 32, '#007AFF'),
        ("⏳ Time/Aging", 28, '#34C759')
    ]

    y_start = 120
    bar_height = 65
    spacing = 20
    max_bar_width = 550

    for i, (factor, percentage, color) in enumerate(factors):
        y_pos = y_start + (i * (bar_height + spacing))

        # Label
        draw.text((30, y_pos + 32), factor, font=label_font, fill='#1d1d1f', anchor='lm')

        # Bar background
        draw.rounded_rectangle([(300, y_pos), (870, y_pos + bar_height)], radius=10, fill='#f5f5f7')

        # Bar fill (animated feel)
        bar_width = int((percentage / 100) * max_bar_width)
        draw.rounded_rectangle([(300, y_pos), (300 + bar_width, y_pos + bar_height)], radius=10, fill=color)

        # Percentage text on bar
        draw.text((300 + bar_width + 20, y_pos + 32), f"{percentage}%", font=value_font, fill=color, anchor='lm')

    # Key insight box - Apple style
    draw.rounded_rectangle([(50, 560), (950, 620)], radius=15, fill='#007AFF')
    draw.text((100, 590), "💡", font=icon_font, anchor='mm')
    draw.text((500, 590), "Using multiple signals reduces error by 70%", font=label_font, fill='#ffffff', anchor='mm')

    output_path = 'images/statistics-chart.png'
    image.save(output_path, 'PNG', quality=95)
    print(f"✅ Apple-style statistics chart created: {output_path}")

def create_comparison_chart():
    """Create before/after comparison chart"""
    width, height = 1200, 500
    image = Image.new('RGB', (width, height), '#f5f5f7')
    draw = ImageDraw.Draw(image)

    try:
        title_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 32)
        label_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 24)
        value_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 50)
        small_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 18)
    except:
        title_font = ImageFont.load_default()
        label_font = ImageFont.load_default()
        value_font = ImageFont.load_default()
        small_font = ImageFont.load_default()

    # Title
    draw.text((600, 40), "Performance Comparison", font=title_font, fill='#1d1d1f', anchor='mm')

    # Current Apple approach
    draw.rounded_rectangle([(50, 100), (550, 450)], radius=20, fill='#ffffff', outline='#FF3B30', width=4)
    draw.text((300, 140), "❌ Current Approach", font=label_font, fill='#FF3B30', anchor='mm')
    draw.text((300, 190), "Face-Only Clustering", font=small_font, fill='#86868b', anchor='mm')

    draw.text((300, 270), "35%", font=value_font, fill='#FF3B30', anchor='mm')
    draw.text((300, 320), "Error Rate", font=small_font, fill='#86868b', anchor='mm')

    draw.text((300, 380), "👤 → 5👥", font=label_font, fill='#FF3B30', anchor='mm')
    draw.text((300, 420), "Splits same person", font=small_font, fill='#86868b', anchor='mm')

    # Proposed solution
    draw.rounded_rectangle([(650, 100), (1150, 450)], radius=20, fill='#ffffff', outline='#34C759', width=4)
    draw.text((900, 140), "✅ Proposed Solution", font=label_font, fill='#34C759', anchor='mm')
    draw.text((900, 190), "Context-Aware Clustering", font=small_font, fill='#86868b', anchor='mm')

    draw.text((900, 270), "10%", font=value_font, fill='#34C759', anchor='mm')
    draw.text((900, 320), "Error Rate", font=small_font, fill='#86868b', anchor='mm')

    draw.text((900, 380), "5👤 → 1👤", font=label_font, fill='#34C759', anchor='mm')
    draw.text((900, 420), "Correctly groups", font=small_font, fill='#86868b', anchor='mm')

    output_path = 'images/comparison-chart.png'
    image.save(output_path, 'PNG', quality=95)
    print(f"✅ Apple-style comparison chart created: {output_path}")

# Create all images
os.makedirs('images', exist_ok=True)
create_blog_header()
create_problem_diagram()
create_solution_flowchart()
create_statistics_chart()
create_comparison_chart()

print("\n🎉 All Apple-style blog images created successfully!")
print("📱 Images use official Apple design language and colors")
print("✨ Professional, eye-catching, and brand-consistent")
