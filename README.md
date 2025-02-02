# Web Scraping PDF Generator

This project is a Python script that scrapes web pages from a given table of contents and generates PDF files from the extracted content. The script uses BeautifulSoup for web scraping, requests for fetching the web pages, and pdfkit for generating PDFs. It's a useful tool for automating the conversion of web content into formatted PDF documents.

## Features

- Scrapes web pages for content from a table of contents.
- Generates PDFs from the extracted content.
- Allows customization of output formats, including page sizes and margins.
- Supports automatic exclusion of unwanted paragraphs (first and last).
- Easy to set up and use.

## Requirements

- Python 3.x
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- [requests](https://pypi.org/project/requests/)
- [pdfkit](https://pypi.org/project/pdfkit/)
- [wkhtmltopdf](https://wkhtmltopdf.org/) (installed locally)

## Setup Instructions

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/JAQLx/WormWebScraper.git
    ```

2. Install the required Python packages:

    ```bash
    pip install beautifulsoup4 requests pdfkit
    ```

3. Install [wkhtmltopdf](https://wkhtmltopdf.org/), a command-line tool required by pdfkit for generating PDFs. Ensure it's correctly installed on your system, and update the `WKHTMLTOPDF_PATH` in the script to point to the location of the executable.

4. Run the script:

    ```bash
    python TextScraper.py
    ```

5. The script will fetch the table of contents from the specified URL, scrape the content, and generate a PDF for each chapter.

## How It Works

1. **Scraping Content**: The script fetches the content from a table of contents page (e.g., a blog or website) using the `requests` library. It then uses `BeautifulSoup` to parse the HTML and extract the relevant chapter links and text.

2. **Generating PDFs**: After parsing the content, the script generates PDFs using `pdfkit` and the `wkhtmltopdf` tool. The PDF files are saved in the specified output directory with filenames based on chapter names.

3. **Customization**: You can modify the script to adjust the page layout, margins, fonts, and other options for the PDFs generated.


## Acknowledgments

- The project uses [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for HTML parsing.
- [pdfkit](https://pypi.org/project/pdfkit/) is used to generate PDFs using the `wkhtmltopdf` tool.
- [wkhtmltopdf](https://wkhtmltopdf.org/) is a command-line tool that renders HTML into PDFs.
