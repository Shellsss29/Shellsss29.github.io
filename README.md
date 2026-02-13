# Shailly Bhati - Portfolio Website

A modern, responsive portfolio website showcasing software engineering experience, projects, and skills.

## 🌟 Features

- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Modern UI**: Dark theme with gradient accents and smooth animations
- **Interactive Elements**: Typing effect, parallax scrolling, hover animations
- **SEO Optimized**: Meta tags and semantic HTML structure
- **Fast Loading**: Optimized performance with minimal dependencies
- **Accessible**: ARIA labels and keyboard navigation support

## 📁 Project Structure

```
portfolio-website/
├── index.html          # Main HTML file
├── css/
│   └── style.css      # Styling
├── js/
│   └── script.js      # JavaScript functionality
├── images/            # Images folder (add your photos here)
└── README.md          # This file
```

## 🚀 Quick Start

### Option 1: View Locally

1. Open `index.html` in your web browser
2. That's it! No build process required.

### Option 2: Use Live Server (Recommended for Development)

1. Install the VS Code extension: "Live Server"
2. Right-click on `index.html` and select "Open with Live Server"
3. The site will open in your browser with auto-reload on changes

## 🌐 Deployment Options

### 1. GitHub Pages (Free & Easy)

**Step-by-step:**

1. Create a new repository on GitHub named `<your-username>.github.io`
   - Example: `Shellsss29.github.io`

2. Push your code to GitHub:
```bash
cd portfolio-website
git init
git add .
git commit -m "Initial portfolio website"
git remote add origin https://github.com/Shellsss29/<your-username>.github.io.git
git branch -M main
git push -u origin main
```

3. Enable GitHub Pages:
   - Go to your repository on GitHub
   - Click "Settings" > "Pages"
   - Under "Source", select "main" branch
   - Click "Save"

4. Your site will be live at: `https://<your-username>.github.io`
   - Example: `https://Shellsss29.github.io`

**Custom Domain (Optional):**
- Add a `CNAME` file with your domain name
- Configure DNS settings with your domain provider

### 2. Netlify (Recommended for Custom Domain)

**Step-by-step:**

1. Sign up at [netlify.com](https://www.netlify.com)

2. **Option A - Drag & Drop:**
   - Drag the entire `portfolio-website` folder onto Netlify's dashboard
   - Your site is live instantly!

3. **Option B - Connect GitHub:**
   - Click "New site from Git"
   - Connect your GitHub account
   - Select your portfolio repository
   - Click "Deploy site"

4. Get your URL: `https://your-site-name.netlify.app`

5. **Custom Domain:**
   - Go to "Domain settings"
   - Click "Add custom domain"
   - Follow instructions to configure DNS

### 3. Vercel (Alternative)

1. Sign up at [vercel.com](https://vercel.com)
2. Click "Import Project"
3. Connect your GitHub repository
4. Click "Deploy"
5. Your site is live at: `https://your-project.vercel.app`

## 🎨 Customization

### Update Personal Information

Edit `index.html` and replace:
- Name, title, and description in the hero section
- Experience details in the timeline
- Project information and GitHub links
- Contact information and social media links

### Change Colors

Edit `css/style.css` and modify the CSS variables in `:root`:

```css
:root {
    --primary-color: #3b82f6;    /* Main blue color */
    --secondary-color: #8b5cf6;  /* Purple accent */
    --accent: #06b6d4;           /* Cyan highlight */
    --success: #10b981;          /* Green for metrics */
}
```

### Add Your Photo

1. Add your photo to the `images/` folder
2. Update the hero section in `index.html` with an img tag:
```html
<img src="images/your-photo.jpg" alt="Shailly Bhati" class="hero-image">
```
3. Add styling in `style.css`

### Add More Projects

Copy the project card structure in `index.html` and modify:

```html
<div class="project-card">
    <div class="project-header">
        <i class="fas fa-icon-name project-icon"></i>
        <h3>Project Name</h3>
    </div>
    <p class="project-subtitle">Project Type</p>
    <p class="project-description">Description here...</p>
    <!-- metrics, tags, and links -->
</div>
```

## 📱 Add to LinkedIn

1. Deploy your site (see deployment options above)
2. Copy your live URL (e.g., `https://shellsss29.github.io`)
3. On LinkedIn:
   - Go to your profile
   - Click "Add profile section" > "Recommended" > "Add featured"
   - Select "Link"
   - Paste your portfolio URL
   - Add a title: "My Portfolio"
   - Click "Save"

**Or add in Contact Info:**
- Edit your profile
- Click "Contact info"
- Under "Websites", add your portfolio URL
- Select "Portfolio" as the type

## 🔧 Advanced Customization

### Add Google Analytics

Add this before `</head>` in `index.html`:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=YOUR-GA-ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'YOUR-GA-ID');
</script>
```

### Add Favicon

1. Create a favicon (use [favicon.io](https://favicon.io))
2. Place `favicon.ico` in the root folder
3. Add to `<head>` in `index.html`:
```html
<link rel="icon" type="image/x-icon" href="favicon.ico">
```

### Connect Contact Form

To receive messages from the contact section:

**Option 1: Formspree (Easy)**
1. Sign up at [formspree.io](https://formspree.io)
2. Create a form and get your endpoint
3. Add a form to your contact section in `index.html`

**Option 2: Netlify Forms**
1. Add `netlify` attribute to your form
2. Forms will appear in Netlify dashboard

## 📊 Performance Tips

- Optimize images: Use WebP format and compress them
- Minimize CSS/JS: Use tools like [CSS Minifier](https://cssminifier.com)
- Enable caching: Configure in your hosting platform
- Use a CDN: Automatically enabled on Netlify/Vercel

## 🐛 Troubleshooting

**Site not loading on GitHub Pages?**
- Check that the repository name is `<username>.github.io`
- Verify that Pages is enabled in Settings
- Wait 2-3 minutes for deployment

**Mobile menu not working?**
- Clear browser cache
- Check browser console for JavaScript errors

**Links not working?**
- Update all `href` attributes with your actual URLs
- Replace GitHub and LinkedIn links with yours

## 📝 TODO (Future Enhancements)

- [ ] Add a blog section
- [ ] Include downloadable resume
- [ ] Add project screenshots/demos
- [ ] Implement dark/light mode toggle
- [ ] Add testimonials section
- [ ] Include certifications
- [ ] Add language switcher (if needed)

## 📄 License

This portfolio template is free to use for personal and commercial projects.

## 📧 Support

If you have questions or need help:
- Email: shaillybhati72@gmail.com
- LinkedIn: [linkedin.com/in/shailly-bhati](https://www.linkedin.com/in/shailly-bhati)

---

**Built with ❤️ and code**

Made by Shailly Bhati
