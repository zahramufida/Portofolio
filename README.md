# Zahra Mufida - Portfolio

Static website (HTML, CSS, a little JavaScript). No install or build step.

## Run locally
Double-click `index.html`, or run `python3 -m http.server` in this folder and open http://localhost:8000.

## Deploy (free)
- **Netlify**: drag this whole folder to https://app.netlify.com/drop
- **GitHub Pages**: push the folder to a repo, then Settings > Pages > Deploy from branch.
- **Vercel**: `vercel` inside this folder.

## Edit content
- Change the text in `build.py` (projects, experience, skills, links), then run `python3 build.py` to regenerate the 4 pages.
- Or edit the `.html` files directly.
- Colors and fonts: top of `css/style.css` (`:root`).
- Photo: replace `assets/zahra.jpg`. CV: replace `assets/Zahra-Mufida-CV.pdf`.
- Add a GitHub link to a project: set `link=` in `build.py`.
