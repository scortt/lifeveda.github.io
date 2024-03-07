import os
import argparse
from datetime import datetime

def generate_sitemap(markdown_dir, base_url, output_file='sitemap.xml'):
    sitemap_header = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""
    sitemap_footer = "</urlset>"
    sitemap_entries = ""

    lastmod = datetime.now().strftime("%Y-%m-%d")

    for root, dirs, files in os.walk(markdown_dir):
        for file in files:
            if file.endswith(".md"):
                rel_path = os.path.relpath(os.path.join(root, file), markdown_dir)
                url_path = os.path.splitext(rel_path)[0].replace(os.sep, '/')
                full_url = f"{base_url}/{url_path}/"
                
                sitemap_entries += f"""  <url>
    <loc>{full_url}</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
"""

    sitemap = sitemap_header + sitemap_entries + sitemap_footer

    with open(output_file, 'w') as file:
        file.write(sitemap)

    print(f"Sitemap generated: {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Generate a sitemap for a GitHub Pages site from Markdown files.")
    parser.add_argument("markdown_dir", help="Directory containing the Markdown files.")
    parser.add_argument("base_url", help="Base URL of the GitHub Pages site.")
    parser.add_argument("-o", "--output", default="sitemap.xml", help="Output sitemap file name (default: sitemap.xml).")

    args = parser.parse_args()

    generate_sitemap(args.markdown_dir, args.base_url, args.output)

if __name__ == "__main__":
    main()

