# TaskFlow - Professional Todo Management App

A beautifully designed, fully responsive todo management application built with Django, featuring smooth animations, professional design patterns, and an intuitive user interface.

## ✨ Features

### Design & UX
- **Modern Dark Theme** - Sleek dark mode with gradient backgrounds
- **Smooth Animations** - Fade-in, scale, and slide animations throughout
- **Responsive Design** - Works perfectly on desktop, tablet, and mobile
- **Professional Typography** - Clean, readable fonts with proper hierarchy
- **Hover Transitions** - Interactive elements with smooth hover effects
- **Scroll Animations** - Elements animate in as you scroll down the page

### Technical Features
- ⚡ **Lightning Fast** - Optimized performance
- 🎯 **Smart Prioritization** - Organize tasks by importance
- 📱 **Fully Responsive** - Mobile-first design approach
- 🔒 **Secure** - Enterprise-grade security
- 🌙 **Dark Mode** - Eye-friendly interface
- 🎨 **Beautiful UI** - Pixel-perfect design

## 📁 Project Structure

```
MyTodo/
├── manage.py              # Django management script
├── db.sqlite3             # Database file
├── MyTodo/                # Project settings
│   ├── settings.py        # Django settings
│   ├── urls.py            # URL routing
│   └── wsgi.py            # WSGI configuration
├── todo/                  # Main app
│   ├── views.py           # View logic
│   ├── models.py          # Data models
│   ├── urls.py            # App URLs
│   ├── templates/         # HTML templates
│   │   ├── base.html      # Base template (professional design system)
│   │   ├── todowork.html  # Home page (hero + features)
│   │   ├── about.html     # About page (profile + skills)
│   │   └── features.html  # Features page (feature list)
│   └── static/            # Static files
│       └── images/        # Image assets
└── tools/                 # Utility scripts
    └── test_all_templates.py  # Template testing
```

## 🎨 Design System

### Color Palette
- **Primary**: `#6366f1` (Indigo)
- **Secondary**: `#8b5cf6` (Purple)
- **Accent**: `#ec4899` (Pink)
- **Dark**: `#1f2937`
- **Light**: `#f9fafb`

### Typography
- **Font Family**: System fonts (-apple-system, BlinkMacSystemFont, Segoe UI, etc.)
- **Font Weights**: 400 (regular), 500 (medium), 600 (semibold), 700 (bold)
- **Sizes**: H1: 3.5rem, H2: 2.5rem, H3: 1.5rem, Body: 1rem

### Animations
- **Fade In Up**: Elements fade and slide up from below
- **Fade In Down**: Elements fade and slide down from above
- **Fade In Left/Right**: Elements fade and slide from left/right
- **Scale In**: Elements scale from 95% to 100%
- **Float**: Subtle floating animation (20s cycle)
- **Duration**: 300ms (all transitions)
- **Easing**: cubic-bezier(0.4, 0, 0.2, 1)

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Django 5.2.4

### Installation

1. **Clone or navigate to the project:**
   ```bash
   cd MyTodo
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install django
   ```

4. **Migrate the database:**
   ```bash
   python manage.py migrate
   ```

5. **Collect static files:**
   ```bash
   python manage.py collectstatic --noinput
   ```

### Running the Development Server

```bash
python manage.py runserver
```

The app will be available at `http://127.0.0.1:8000/`

## 📄 Pages

### Home (/)
- **Hero Section** - Eye-catching headline with gradient background
- **Features Grid** - 6 feature cards with hover animations
- **Stats Section** - Key metrics display
- **CTA Banner** - Call-to-action for engagement

### About (/about/)
- **Profile Section** - Professional profile card with social links
- **Journey Timeline** - About, professional journey, what I do
- **Skills Grid** - Technical skills and expertise areas
- **Contact Section** - Contact links and social media

### Features (/features/)
- **Feature List** - Displays all features with smooth animations
- **Add Feature CTA** - Link to suggest new features

## 🎯 Component Library

### Buttons
- `.btn-primary` - Primary gradient button
- `.btn-secondary` - Secondary outline button
- `.btn-outline` - Outlined button variant

### Cards
- `.card` - Base card styling
- `.card-featured` - Featured card with gradient background

### Layouts
- `.grid-2` - 2-column responsive grid
- `.grid-3` - 3-column responsive grid
- `.grid-4` - 4-column responsive grid

### Utilities
- `.text-center`, `.text-white`, `.text-muted`
- `.mt-1` to `.mt-4` - Margin top
- `.mb-1` to `.mb-4` - Margin bottom
- `.gap-1` to `.gap-4` - Gap (for flex/grid)

## 📱 Responsive Breakpoints

- **Desktop**: 1200px+
- **Tablet**: 768px - 1199px
- **Mobile**: < 768px

All components and layouts are mobile-first and fully responsive.

## 🧪 Testing Templates

Run the template test script to verify all pages render correctly:

```bash
python tools/test_all_templates.py
```

Expected output:
```
✓ todowork.html rendered successfully
✓ about.html rendered successfully
✓ features.html rendered successfully
ALL TEMPLATES RENDERED SUCCESSFULLY! ✓
```

## 📸 Adding Your Profile Image

1. Place your profile image at: `todo/static/images/pawan.jpg`
2. Supported formats: JPG, PNG, WebP
3. Recommended size: 400x400px or larger
4. A placeholder SVG will display if the image is missing

Then collect static files:
```bash
python manage.py collectstatic --noinput
```

## 🔧 Customization

### Changing Colors
Edit `:root` CSS variables in `base.html`:
```css
:root {
    --primary: #6366f1;        /* Change this */
    --secondary: #8b5cf6;      /* And this */
    --accent: #ec4899;         /* And this */
}
```

### Adjusting Animation Duration
Find `--duration: 300ms;` in base.html and change to desired value (e.g., `500ms` for slower animations).

### Modifying Page Content
Edit the respective template files:
- Home: `todo/templates/todowork.html`
- About: `todo/templates/about.html`
- Features: `todo/templates/features.html`

## 📝 Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Mobile, etc.)

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Pawan Poojary** - Full Stack Developer

- GitHub: [@Pawanpoojary5](https://github.com/Pawanpoojary5)
- LinkedIn: [/in/Pawanpoojary](https://linkedin.com/in/Pawanpoojary)
- Email: [pawanpoojari026@gmail.com](mailto:pawanpoojari026@gmail.com)
- Instagram: [@pawan.__.poojary](https://instagram.com/pawan.__.poojary)

## 🙏 Credits

Built with ❤️ using:
- Django 5.2.4
- CSS3 & HTML5
- Modern Web Standards

---

**TaskFlow** - Master Your Tasks, Amplify Productivity ✨
