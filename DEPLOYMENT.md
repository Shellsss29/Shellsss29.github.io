# 🚀 Quick Deployment Guide

## Deploy to GitHub Pages in 5 Minutes

### Step 1: Create GitHub Repository

1. Go to [GitHub](https://github.com) and log in
2. Click the "+" icon (top right) → "New repository"
3. Repository name: `Shellsss29.github.io` (use YOUR GitHub username)
4. Make it **Public**
5. **DO NOT** initialize with README
6. Click "Create repository"

### Step 2: Deploy Your Code

Open Terminal and run these commands:

```bash
# Navigate to your portfolio folder
cd ~/Desktop/portfolio-website

# Initialize git repository
git init

# Add all files
git add .

# Commit files
git commit -m "Initial portfolio website"

# Add GitHub remote (replace with YOUR repository URL)
git remote add origin https://github.com/Shellsss29/Shellsss29.github.io.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Access Your Live Website

Wait 2-3 minutes, then visit:
- **Your URL**: `https://shellsss29.github.io`

That's it! Your portfolio is live! 🎉

---

## Alternative: Deploy to Netlify (Even Easier!)

### Option 1: Drag & Drop (Fastest)

1. Go to [Netlify](https://app.netlify.com)
2. Sign up (free)
3. Drag the `portfolio-website` folder onto the dashboard
4. Done! Your site is live at: `https://your-site-name.netlify.app`

### Option 2: Connect GitHub

1. Push your code to GitHub first (see above)
2. Go to Netlify
3. Click "Add new site" → "Import from Git"
4. Connect GitHub and select your repository
5. Click "Deploy"
6. Your site is live!

**Custom Domain:**
- Click "Domain settings" in Netlify
- Add your domain
- Update DNS settings (instructions provided)

---

## Update Your Website

After making changes to your code:

```bash
cd ~/Desktop/portfolio-website
git add .
git commit -m "Updated portfolio content"
git push
```

Your site will automatically update in 1-2 minutes!

---

## Add to LinkedIn

1. **In Featured Section:**
   - Go to your LinkedIn profile
   - Click "Add profile section"
   - Select "Featured" → "Link"
   - Paste your URL: `https://shellsss29.github.io`
   - Title: "My Portfolio"
   - Click "Save"

2. **In Contact Info:**
   - Click "Contact Info" on your profile
   - Under "Websites", click "+"
   - Type: "Portfolio"
   - URL: `https://shellsss29.github.io`
   - Click "Apply"

3. **In Headline/About:**
   - Add: "Portfolio: shellsss29.github.io"

---

## Troubleshooting

### "Git command not found"
Install Git:
```bash
brew install git
```

### "Permission denied"
Set up GitHub authentication:
1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Select "repo" scope
4. Use token as password when pushing

### "Repository already exists"
```bash
cd ~/Desktop/portfolio-website
git remote remove origin
git remote add origin https://github.com/Shellsss29/Shellsss29.github.io.git
git push -u origin main
```

---

## Next Steps

✅ Deploy website
✅ Add to LinkedIn
✅ Share on resume
✅ Test on mobile
✅ Check all links work
✅ Add Google Analytics (optional)
✅ Get custom domain (optional)

**Need help?** Email: shaillybhati72@gmail.com
