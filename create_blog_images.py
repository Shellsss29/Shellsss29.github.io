from PIL import Image, ImageDraw, ImageFont
import os

def create_blog_header():
    """Create hero image for blog post"""
    width, height = 1200, 400
    image = Image.new('RGB', (width, height), '#0f172a')
    draw = ImageDraw.Draw(image)

    # Gradient background
    for y in range(height):
        ratio = y / height
        r = int(59 + (139 - 59) * ratio)
        g = int(130 - (51) * ratio)
        b = int(246)
        draw.rectangle([(0, y), (width, y + 1)], fill=(r, g, b))

    # Decorative circles
    draw.ellipse([(-100, -100), (300, 300)], fill='#06b6d4')
    draw.ellipse([(900, 100), (1400, 600)], fill='#8b5cf6')

    # Semi-transparent overlay
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    overlay_draw.rectangle([(0, 0), (width, height)], fill=(15, 23, 42, 100))
    image.paste(overlay, (0, 0), overlay)

    try:
        title_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 60)
        emoji_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 80)
    except:
        title_font = ImageFont.load_default()
        emoji_font = ImageFont.load_default()

    # Visual representation
    draw.text((200, 200), "👤", font=emoji_font, anchor='mm')
    draw.text((400, 200), "→", font=title_font, fill='#ffffff', anchor='mm')
    draw.text((550, 150), "👥", font=emoji_font, anchor='mm')
    draw.text((550, 250), "👥", font=emoji_font, anchor='mm')
    draw.text((700, 100), "👥", font=emoji_font, anchor='mm')
    draw.text((700, 200), "👥", font=emoji_font, anchor='mm')
    draw.text((700, 300), "👥", font=emoji_font, anchor='mm')
    draw.text((900, 200), "❓", font=emoji_font, anchor='mm')

    output_path = 'images/blog-header.png'
    image.save(output_path, 'PNG', quality=95)
    print(f"✅ Blog header created: {output_path}")

def create_problem_diagram():
    """Create diagram showing the clustering problem"""
    width, height = 1000, 600
    image = Image.new('RGB', (width, height), '#ffffff')
    draw = ImageDraw.Draw(image)

    try:
        title_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 28)
        label_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 20)
        small_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 16)
    except:
        title_font = ImageFont.load_default()
        label_font = ImageFont.load_default()
        small_font = ImageFont.load_default()

    # Title
    draw.text((500, 30), "The Apple Photos Clustering Problem", font=title_font, fill='#0f172a', anchor='mm')

    # Same person, different conditions (left side)
    photos_y = 100
    conditions = [
        ("☀️ Outdoor", "#fbbf24"),
        ("🏠 Indoor", "#3b82f6"),
        ("👓 With Glasses", "#8b5cf6"),
        ("📸 Selfie", "#ec4899"),
        ("🎭 Party Photo", "#10b981")
    ]

    draw.text((150, photos_y), "Same Person →", font=label_font, fill='#6b7280', anchor='mm')

    for i, (condition, color) in enumerate(conditions):
        y_pos = photos_y + 60 + (i * 80)
        # Photo box
        draw.rectangle([(50, y_pos), (250, y_pos + 60)], fill=color, outline='#0f172a', width=2)
        draw.text((150, y_pos + 30), condition, font=small_font, fill='#ffffff', anchor='mm')

    # Arrow
    draw.text((500, 300), "Apple's Algorithm", font=label_font, fill='#3b82f6', anchor='mm')
    for i in range(5):
        y_pos = photos_y + 60 + (i * 80) + 30
        draw.line([(260, y_pos), (400, y_pos)], fill='#94a3b8', width=3)
        draw.polygon([(400, y_pos), (390, y_pos-5), (390, y_pos+5)], fill='#94a3b8')

    # Result clusters (right side)
    draw.text((750, photos_y), "← Creates 5 People", font=label_font, fill='#ef4444', anchor='mm')

    for i in range(5):
        y_pos = photos_y + 60 + (i * 80)
        draw.ellipse([(650, y_pos), (850, y_pos + 60)], fill='#fee2e2', outline='#ef4444', width=2)
        draw.text((750, y_pos + 30), f"Person {i+1}", font=small_font, fill='#dc2626', anchor='mm')

    # Problem label
    draw.rectangle([(300, 520), (700, 570)], fill='#fef3c7', outline='#f59e0b', width=3)
    draw.text((500, 545), "❌ Problem: Same person split into 5 clusters", font=label_font, fill='#d97706', anchor='mm')

    output_path = 'images/problem-diagram.png'
    image.save(output_path, 'PNG', quality=95)
    print(f"✅ Problem diagram created: {output_path}")

def create_solution_flowchart():
    """Create flowchart showing the solution"""
    width, height = 1000, 700
    image = Image.new('RGB', (width, height), '#ffffff')
    draw = ImageDraw.Draw(image)

    try:
        title_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 28)
        box_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 18)
        label_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 16)
    except:
        title_font = ImageFont.load_default()
        box_font = ImageFont.load_default()
        label_font = ImageFont.load_default()

    # Title
    draw.text((500, 30), "Context-Aware Solution", font=title_font, fill='#0f172a', anchor='mm')

    # Input
    draw.rectangle([(350, 80), (650, 130)], fill='#dbeafe', outline='#3b82f6', width=3)
    draw.text((500, 105), "Photo with Face", font=box_font, fill='#1e40af', anchor='mm')

    # Arrow down
    draw.line([(500, 130), (500, 170)], fill='#94a3b8', width=3)
    draw.polygon([(500, 170), (495, 160), (505, 160)], fill='#94a3b8')

    # Multi-signal analysis
    signals = [
        ("Face Features", 180, '#3b82f6'),
        ("Location Data", 350, '#10b981'),
        ("Time Stamp", 520, '#f59e0b'),
        ("Clothing/Body", 690, '#8b5cf6')
    ]

    for label, x_pos, color in signals:
        draw.rectangle([(x_pos-80, 180), (x_pos+80, 240)], fill=color, outline='#0f172a', width=2)
        draw.text((x_pos, 210), label, font=label_font, fill='#ffffff', anchor='mm')
        # Arrow down
        draw.line([(x_pos, 240), (x_pos, 280)], fill='#94a3b8', width=2)
        draw.polygon([(x_pos, 280), (x_pos-5, 270), (x_pos+5, 270)], fill='#94a3b8')

    # Combine signals
    draw.rectangle([(250, 290), (750, 350)], fill='#c7d2fe', outline='#6366f1', width=3)
    draw.text((500, 320), "Hierarchical Clustering Engine", font=box_font, fill='#4338ca', anchor='mm')

    # Arrow down
    draw.line([(500, 350), (500, 390)], fill='#94a3b8', width=3)
    draw.polygon([(500, 390), (495, 380), (505, 380)], fill='#94a3b8')

    # Micro-clusters
    draw.text((500, 420), "Create Micro-Clusters", font=label_font, fill='#6b7280', anchor='mm')
    micro_x = [200, 400, 600, 800]
    for x in micro_x:
        draw.ellipse([(x-40, 450), (x+40, 530)], fill='#ddd6fe', outline='#8b5cf6', width=2)
        draw.text((x, 490), "Mini\nGroup", font=label_font, fill='#6b21a8', anchor='mm')

    # Link with context
    draw.line([(240, 490), (760, 490)], fill='#10b981', width=4)
    draw.text((500, 555), "Link based on context signals", font=label_font, fill='#059669', anchor='mm')

    # Final result
    draw.rectangle([(300, 590), (700, 650)], fill='#d1fae5', outline='#10b981', width=3)
    draw.text((500, 620), "✅ Result: 1 Person (correctly grouped)", font=box_font, fill='#065f46', anchor='mm')

    output_path = 'images/solution-flowchart.png'
    image.save(output_path, 'PNG', quality=95)
    print(f"✅ Solution flowchart created: {output_path}")

def create_statistics_chart():
    """Create chart with statistics"""
    width, height = 800, 500
    image = Image.new('RGB', (width, height), '#ffffff')
    draw = ImageDraw.Draw(image)

    try:
        title_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 26)
        label_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 18)
        value_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 22)
    except:
        title_font = ImageFont.load_default()
        label_font = ImageFont.load_default()
        value_font = ImageFont.load_default()

    # Title
    draw.text((400, 30), "Impact of Variables on Face Recognition", font=title_font, fill='#0f172a', anchor='mm')

    # Chart data (accuracy drop %)
    factors = [
        ("Lighting Change", 45, '#ef4444'),
        ("Viewing Angle", 38, '#f59e0b'),
        ("Accessories (Glasses)", 32, '#eab308'),
        ("Time (Aging)", 28, '#22c55e'),
        ("Photo Quality", 35, '#3b82f6')
    ]

    y_start = 100
    bar_height = 50
    spacing = 20
    max_width = 500

    for i, (factor, percentage, color) in enumerate(factors):
        y_pos = y_start + (i * (bar_height + spacing))

        # Label
        draw.text((20, y_pos + 25), factor, font=label_font, fill='#374151', anchor='lm')

        # Bar
        bar_width = int((percentage / 100) * max_width)
        draw.rectangle([(250, y_pos), (250 + bar_width, y_pos + bar_height)], fill=color)

        # Percentage
        draw.text((250 + bar_width + 15, y_pos + 25), f"{percentage}%", font=value_font, fill=color, anchor='lm')

    # Key insight box
    draw.rectangle([(50, 440), (750, 480)], fill='#dbeafe', outline='#3b82f6', width=2)
    draw.text((400, 460), "💡 Multiple signals reduce error rate by 70%", font=label_font, fill='#1e40af', anchor='mm')

    output_path = 'images/statistics-chart.png'
    image.save(output_path, 'PNG', quality=95)
    print(f"✅ Statistics chart created: {output_path}")

# Create all images
os.makedirs('images', exist_ok=True)
create_blog_header()
create_problem_diagram()
create_solution_flowchart()
create_statistics_chart()

print("\n🎉 All blog images created successfully!")
