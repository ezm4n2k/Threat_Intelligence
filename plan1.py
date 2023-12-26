from googletrans import Translator
from bs4 import BeautifulSoup

def merge_adjacent_paragraphs(html):
    soup = BeautifulSoup(html, 'html.parser')
    paragraphs = soup.find_all('p')
    
    # Merge adjacent paragraphs
    for i in range(len(paragraphs)-1, 0, -1):
        if paragraphs[i].previous_sibling == paragraphs[i - 1]:
            paragraphs[i - 1].string += paragraphs[i].string
            paragraphs[i].decompose()

    return str(soup)

def translate_text(text, target_language='vi'):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

def translate_html(html, target_language='vi'):
    soup = BeautifulSoup(html, 'html.parser')
    for paragraph in soup.find_all('p'):
        original_text = paragraph.get_text(strip=True)
        
        # Dịch đoạn văn bản
        translated_text = translate_text(original_text, target_language)
        
        # Gán lại văn bản đã dịch cho thẻ <p>
        paragraph.string = translated_text

    # Ghép các thẻ <p> liền kề
    result_html = merge_adjacent_paragraphs(str(soup))
    return result_html

# In ra đoạn văn bản đã dịch
# translated_html = translate_html(html_content)
# print(translated_html)
