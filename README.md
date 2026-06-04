# Resume & Portfolio Generator

Generate a responsive web portfolio and a traditional, single-page resume from a single JSON data source. This ensures both documents stay perfectly in sync without manual duplicate updates.

## Features
- **Single Source of Truth**: Update one `data.json` file to update both outputs simultaneously.
- **Web Portfolio**: Responsive design including social links, images, and hobbies/interests.
- **Traditional Resume**: Stripped-down, single-page layout optimized for PDF export and printing (excludes images, social links, and hobbies).
- **Static Output**: Generates pure HTML/CSS files. No backend required; easy to deploy to any static host (e.g., GitHub Pages).
- **Highly Customizable**: Easily modify the CSS to match your personal brand.

## Prerequisites
- Python 3.x

## Project Structure
```text
├── data.json            # Your personal data (single source of truth)
├── generate.py          # Python script to generate HTML files
├── portfolio.html       # Generated web portfolio
├── resume.html          # Generated traditional resume
├── asdfghj.css  # Custom CSS for the portfolio
└── cvbnmdf.css     # Custom CSS for the resume
```

## Usage
1. **Clone** this repository.
2. **Edit** `data.json` with your personal information, experience, and links.
3. **Run** the generator script:
   ```bash
   python generate.py
   ```
4. **View** the generated `portfolio.html` and `resume.html` in your browser.
5. **Export** `resume.html` to PDF via your browser's print dialog (select "Save as PDF" and adjust margins if needed to ensure a perfect single-page fit).

## Customization
- **Content**: Modify the structure of `data.json` and update `generate.py` accordingly to add or remove fields.
- **Styling**: Edit `asdfghj.css` and `scvbnm.css` to change colors, fonts, spacing, and layouts.