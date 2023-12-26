import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings()

def scrape_page(url):
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        headers = soup.find_all(['header', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'footer'])
        for header in headers:
            header.decompose()
        paragraphs_and_images = soup.find_all(['p', 'img'])
        result = []
        for element in paragraphs_and_images:
            if element.name == 'p':
                text = element.get_text(strip=True)
                if text.strip():
                    result.append({'type': 'text', 'content': text})
            elif element.name == 'img':
                image_url = element.get('src') or element.get('data-src')
                if image_url:
                    result.append({'type': 'image', 'url': image_url})
        return result
    except requests.RequestException as e:
        print(f"Error scraping content: {e}")
        return None

def generate_html(content_list):
    html_content = "<html><body>\n"
    for item in content_list:
        if item['type'] == 'text':
            html_content += f"<p>{item['content']}</p>"
        elif item['type'] == 'image':
            html_content += f"<img src='{item['url']}' alt='Image'>\n"
    html_content += "</body></html>"
    return html_content

def get_all_content(url):
    content_list = scrape_page(url)
    if content_list:
        html_content = generate_html(content_list)
        return html_content


