import requests
from bs4 import BeautifulSoup
import cssutils

def scrape_website(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        css_links = [link['href'] for link in soup.find_all('link', rel='stylesheet') if 'href' in link.attrs]
        return {"html": response.text, "css_links": css_links}
    except Exception as e:
        return {"error": str(e)}

def analyze_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    report = []

    # Semantic tags
    semantic_tags = ['header', 'nav', 'main', 'article', 'section', 'footer']
    used = [tag for tag in semantic_tags if soup.find(tag)]
    report.append(f"Semantic tags used: {', '.join(used)}")

    # Accessibility: missing alt
    images = soup.find_all('img')
    missing_alt = sum(1 for img in images if not img.get('alt'))
    report.append(f"Images missing alt attribute: {missing_alt}")

    # Heading structure
    headings = [f"{tag.name}: {tag.text.strip()}" for tag in soup.find_all(['h1', 'h2', 'h3'])]
    report.append("Headings structure:\n" + "\n".join(headings))

    return "\n".join(report)

def analyze_css(html, css_links):
    report = []
    report.append(f"CSS Files Found: {len(css_links)}")
    for link in css_links:
        report.append(f"- {link}")
    report.append("Note: Remote CSS parsing can be extended further.")
    return "\n".join(report)

def generate_report(html_result, css_result, html_url="https://example.com"):
    return f'''
# Website Audit Report

## URL
{html_url}

## HTML Insights
{html_result}

## CSS Insights
{css_result}

## Recommendations
- Add alt attributes to all images.
- Review semantic tags usage and heading structure.
- Combine and optimize CSS files for performance.
- Improve mobile responsiveness if needed.
'''

# Tool definitions for CrewAI
scrape_tool = {
    "name": "scrape_tool",
    "description": "Scrape HTML and CSS links from a website",
    "function": scrape_website
}

html_analysis_tool = {
    "name": "html_analysis_tool",
    "description": "Analyze HTML structure for accessibility, semantics, SEO",
    "function": analyze_html
}

css_analysis_tool = {
    "name": "css_analysis_tool",
    "description": "Analyze CSS for maintainability, performance, responsiveness",
    "function": analyze_css
}

report_tool = {
    "name": "report_tool",
    "description": "Generate final report from HTML and CSS analysis",
    "function": generate_report
}
