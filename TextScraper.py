from bs4 import BeautifulSoup
import requests
import pdfkit

# Configuration
WKHTMLTOPDF_PATH = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
OUTPUT_DIR = "C:/Users/banka/Desktop/CSCI/GitHub/Worm Book PDFs/"

def fetch_page_content(url):
    """Fetch the HTML content of the given URL."""
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def parse_content(html):
    """Extract relevant content and title from HTML."""
    soup = BeautifulSoup(html, 'html.parser')
    title_tag = soup.find('h1', class_='entry-title')
    title = title_tag.text.strip() if title_tag else "Untitled"

    content = soup.find('div', class_='entry-content')
    paragraphs = content.find_all('p') if content else []
    selected_paragraphs = paragraphs[1:-1]  # Exclude first and last paragraphs
    paragraphs_html = ''.join(str(p) for p in selected_paragraphs)

    return title, paragraphs_html

def generate_pdf(html_content, output_filename):
    """Generate a PDF from the given HTML content."""
    options = {
        'page-width': '6in',
        'page-height': '9in',
        'margin-top': '0.8in',
        'margin-right': '0.75in',
        'margin-bottom': '0.8in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
    }
    config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)
    pdfkit.from_string(html_content, output_filename, configuration=config, options=options)

def process_url(url, chapter_name):
    """Process a single URL: fetch content, extract metadata, and generate a PDF."""
    try:
        print(f"Processing: {url}")
        html = fetch_page_content(url)
        title, paragraphs_html = parse_content(html)

        output_filename = f"{OUTPUT_DIR}{chapter_name}.pdf"

        html_for_pdf = f"""
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {{
                    font-family: 'Palatino Linotype', 'Book Antiqua', Palatino, serif;
                    font-size: 10pt;
                    line-height: 1.5;
                    color: #000000;
                    margin: 0;
                }}
                h1 {{
                    font-family: 'Palatino Linotype', 'Book Antiqua', Palatino, serif;
                    font-size: 20pt;
                    font-weight: bold;
                    text-align: center;
                }}
            </style>
        </head>
        <body>
            <h1>{title}</h1>
            {paragraphs_html}
        </body>
        </html>
        """

        generate_pdf(html_for_pdf, output_filename)
        print(f"PDF saved: {output_filename}")

    except Exception as e:
        print(f"Error processing {url}: {e}")

def fetch_table_of_contents():
    """Fetch the table of contents page and extract the URLs and chapter info."""
    toc_url = "https://parahumans.wordpress.com/table-of-contents/"
    toc_html = fetch_page_content(toc_url)

    soup = BeautifulSoup(toc_html, 'html.parser')

    # Find all links in the table of contents
    table = soup.find('div', class_='entry-content')
    chapters = table.find_all('a')
    selected_chapters = chapters[:-12]
    
    # Extract the URLs and chapter information
    urls = []
    for chapter in selected_chapters:
        chapter_url = chapter['href']
        chapter_name = chapter.text.strip()

        urls.append((chapter_url, chapter_name))
    
    return urls

def main():
    # Fetch the URLs from the table of contents page
    urls = fetch_table_of_contents()

    # Process each URL
    for url, chapter_name in urls:
        process_url(url, chapter_name)

if __name__ == "__main__":
    main()
