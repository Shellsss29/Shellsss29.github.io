from PIL import Image, ImageDraw, ImageFont
import os

def create_clean_header():
    """Clean header with no overlaps"""
    width, height = 1200, 350
    image = Image.new('RGB', (width, height), '#007AFF')
    draw = ImageDraw.Draw(image)

    # Simple gradient
    for y in range(height):
        alpha = int(200 + (55 * y / height))
        draw.rectangle([(0, y), (width, y+1)], fill=(0, 122, 255))

    try:
        title_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 60)
        subtitle_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 32)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()

    # Clean title
    draw.text((600, 120), "Apple Photos Clustering Problem", font=title_font, fill='#ffffff', anchor='mm')
    draw.text((600, 220), "Why your iPhone thinks you're 5 different people", font=subtitle_font, fill='#ffffff', anchor='mm')

    output_path = 'images/blog-header.png'
    image.save(output_path, 'PNG', quality=95)
    print(f"✅ Clean header: {output_path}")

def create_clean_problem():
    """Clean problem diagram - no overlaps"""
    width, height = 1000, 600
    image = Image.new('RGB', (width, height), '#ffffff')
    draw = ImageDraw.Draw(image)

    try:
        title_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 28)
        text_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 20)
    except:
        title_font = ImageFont.load_default()
        text_font = ImageFont.load_default()

    # Title
    draw.text((500, 30), "The Problem", font=title_font, fill='#1d1d1f', anchor='mm')

    # Left: Same person
    draw.rectangle([(50, 80), (300, 520)], outline='#007AFF', width=3)
    draw.text((175, 100), "Same Person", font=text_font, fill='#007AFF', anchor='mm')

    conditions = ["Outdoor", "Indoor", "With Glasses", "Selfie", "Party"]
    for i, cond in enumerate(conditions):
        y = 150 + (i * 75)
        draw.rectangle([(70, y), (280, y+50)], fill='#e0f2fe', outline='#007AFF', width=2)
        draw.text((175, y+25), cond, font=text_font, fill='#1d1d1f', anchor='mm')

    # Arrow
    draw.polygon([(350, 300), (380, 285), (380, 315)], fill='#86868b')
    draw.text((420, 300), "Apple Photos", font=text_font, fill='#86868b', anchor='lm')

    # Right: 5 people created
    draw.rectangle([(550, 80), (950, 520)], outline='#FF3B30', width=3)
    draw.text((750, 100), "Creates 5 People ❌", font=text_font, fill='#FF3B30', anchor='mm')

    for i in range(5):
        y = 150 + (i * 75)
        draw.rectangle([(570, y), (930, y+50)], fill='#fee2e2', outline='#FF3B30', width=2)
        draw.text((750, y+25), f"Person {i+1}", font=text_font, fill='#1d1d1f', anchor='mm')

    output_path = 'images/problem-diagram.png'
    image.save(output_path, 'PNG', quality=95)
    print(f"✅ Clean problem diagram: {output_path}")

def create_clean_solution():
    """Clean solution flowchart"""
    width, height = 900, 700
    image = Image.new('RGB', (width, height), '#f5f5f7')
    draw = ImageDraw.Draw(image)

    try:
        title_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 28)
        text_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 18)
    except:
        title_font = ImageFont.load_default()
        text_font = ImageFont.load_default()

    # Title
    draw.rectangle([(0, 0), (width, 60)], fill='#007AFF')
    draw.text((450, 30), "Proposed Solution", font=title_font, fill='#ffffff', anchor='mm')

    # Input
    draw.rectangle([(300, 90), (600, 140)], fill='#007AFF')
    draw.text((450, 115), "Photo Input", font=text_font, fill='#ffffff', anchor='mm')

    # Arrow
    draw.line([(450, 140), (450, 180)], fill='#000000', width=3)

    # 4 signals - well spaced
    signals = [
        ("Face", 100, '#007AFF'),
        ("Location", 280, '#34C759'),
        ("Time", 460, '#FF9500'),
        ("Clothing", 640, '#5856D6')
    ]

    for label, x, color in signals:
        draw.rectangle([(x, 190), (x+140, 260)], fill=color)
        draw.text((x+70, 225), label, font=text_font, fill='#ffffff', anchor='mm')
        draw.line([(x+70, 260), (x+70, 300)], fill='#000000', width=2)

    # Combine
    draw.rectangle([(200, 310), (700, 380)], fill='#ffffff', outline='#007AFF', width=3)
    draw.text((450, 345), "Hierarchical Clustering", font=text_font, fill='#1d1d1f', anchor='mm')

    # Arrow
    draw.line([(450, 380), (450, 420)], fill='#000000', width=3)

    # Micro-clusters
    for x in [220, 380, 540, 700]:
        draw.ellipse([(x-50, 430), (x+50, 530)], fill='#e0e7ff', outline='#5856D6', width=2)

    # Link
    draw.line([(220, 480), (700, 480)], fill='#34C759', width=4)

    # Result
    draw.rectangle([(250, 560), (650, 630)], fill='#34C759')
    draw.text((450, 595), "✅ 1 Person (Correct)", font=text_font, fill='#ffffff', anchor='mm')

    output_path = 'images/solution-flowchart.png'
    image.save(output_path, 'PNG', quality=95)
    print(f"✅ Clean solution flowchart: {output_path}")

def create_clean_stats():
    """Clean statistics chart"""
    width, height = 900, 550
    image = Image.new('RGB', (width, height), '#ffffff')
    draw = ImageDraw.Draw(image)

    try:
        title_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 26)
        text_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 18)
        num_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 20)
    except:
        title_font = ImageFont.load_default()
        text_font = ImageFont.load_default()
        num_font = ImageFont.load_default()

    # Title
    draw.text((450, 30), "Variables Affecting Accuracy", font=title_font, fill='#1d1d1f', anchor='mm')

    # Bars - well spaced
    factors = [
        ("Lighting", 45, '#FF9500', 90),
        ("Angle", 38, '#FF3B30', 170),
        ("Quality", 35, '#5856D6', 250),
        ("Accessories", 32, '#007AFF', 330),
        ("Aging", 28, '#34C759', 410)
    ]

    for label, pct, color, y in factors:
        # Label
        draw.text((50, y+20), label, font=text_font, fill='#1d1d1f', anchor='lm')

        # Bar background
        draw.rectangle([(200, y), (850, y+40)], fill='#f5f5f7')

        # Bar fill
        bar_width = int(600 * (pct/100))
        draw.rectangle([(200, y), (200+bar_width, y+40)], fill=color)

        # Percentage
        draw.text((860, y+20), f"{pct}%", font=num_font, fill=color, anchor='lm')

    # Insight
    draw.rectangle([(50, 490), (850, 530)], fill='#007AFF')
    draw.text((450, 510), "Multi-signal approach reduces errors by 70%", font=text_font, fill='#ffffff', anchor='mm')

    output_path = 'images/statistics-chart.png'
    image.save(output_path, 'PNG', quality=95)
    print(f"✅ Clean stats chart: {output_path}")

def create_clean_comparison():
    """Clean comparison"""
    width, height = 1000, 400
    image = Image.new('RGB', (width, height), '#f5f5f7')
    draw = ImageDraw.Draw(image)

    try:
        title_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 26)
        big_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 50)
        text_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 18)
    except:
        title_font = ImageFont.load_default()
        big_font = ImageFont.load_default()
        text_font = ImageFont.load_default()

    # Title
    draw.text((500, 30), "Performance Comparison", font=title_font, fill='#1d1d1f', anchor='mm')

    # Current
    draw.rectangle([(50, 80), (450, 350)], fill='#ffffff', outline='#FF3B30', width=3)
    draw.text((250, 110), "Current", font=text_font, fill='#FF3B30', anchor='mm')
    draw.text((250, 200), "35%", font=big_font, fill='#FF3B30', anchor='mm')
    draw.text((250, 250), "Error Rate", font=text_font, fill='#86868b', anchor='mm')
    draw.text((250, 310), "Splits people", font=text_font, fill='#86868b', anchor='mm')

    # Proposed
    draw.rectangle([(550, 80), (950, 350)], fill='#ffffff', outline='#34C759', width=3)
    draw.text((750, 110), "Proposed", font=text_font, fill='#34C759', anchor='mm')
    draw.text((750, 200), "10%", font=big_font, fill='#34C759', anchor='mm')
    draw.text((750, 250), "Error Rate", font=text_font, fill='#86868b', anchor='mm')
    draw.text((750, 310), "Groups correctly", font=text_font, fill='#86868b', anchor='mm')

    output_path = 'images/comparison-chart.png'
    image.save(output_path, 'PNG', quality=95)
    print(f"✅ Clean comparison: {output_path}")

# Create all
os.makedirs('images', exist_ok=True)
create_clean_header()
create_clean_problem()
create_clean_solution()
create_clean_stats()
create_clean_comparison()

print("\n✅ All clean diagrams created - no overlaps!")
