# hackNY Partners Visualization

A standalone visualization showcasing all the companies and startups that have hosted hackNY fellows from 2010 to 2024.

## Features

- Interactive grid display of all partner companies
- Real-time search functionality
- Multiple sorting options (by fellow count, alphabetically, most recent)
- Responsive design for mobile and desktop
- Shows total fellows hosted by each partner
- Displays active years for each partnership

## Data

The visualization displays **172 partner companies** that have hosted **368+ fellows** over **15 years** (2010-2024).

## Development

### Updating Data

To update the partners data from the latest Alumni.csv:

```bash
python3 generate_data.py
```

This script reads from `../../AlumNY/data/AlumNY/data/Alumni.csv` and generates `partners.json`.

### Local Development

Simply open `index.html` in a browser, or use a local server:

```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000`

## Deployment

This site is deployed via GitHub Pages at: [URL will be added after deployment]

## Tech Stack

- Pure HTML/CSS/JavaScript (no frameworks)
- JSON for data storage
- Responsive CSS Grid layout
- Modern ES6+ JavaScript

## Credits

Built for [hackNY](https://hackny.org) - the fellowship connecting NYC's tech ecosystem with students.
