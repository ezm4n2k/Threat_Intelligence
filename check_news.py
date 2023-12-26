import json
import concurrent.futures
from forum import *

def get_articles_by_titles(json_file, target_titles, json_result):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    old_articles = [article['title'] for article_list in data for article in article_list]
    
    new_titles = [new_title for new_title in target_titles if new_title not in old_articles]
    
    with open(json_file, 'w', encoding='utf-8') as file:
        file.write(json_result)
    return list(set(new_titles))


def get_state():
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        results = list(executor.map(lambda func: func(), [Done.shadowstackre, Done.securityaffairs, Done.paloalto, Done.volexity, Done.netlab, Done.trailofbits, Done.jpcert, Done.censys, Done.troyhunt, Done.lab52, Done.bitdefender, Done.kaspersky, Done.malwarebyte, Done.mandiant, Done.resecur, Done.zimper]))
        titles = []
        json_result = json.dumps(results, indent=2, ensure_ascii=False)
        for result in results:
            for article_list in result:
                title = article_list.get('title', '')
                if title:
                    titles.append(title)

    return titles, results, json_result

def check_news():
    json_file_path = 'state.json'
    new_tit, results, json_result = get_state()
    missing_titles = get_articles_by_titles(json_file_path, new_tit, json_result )
    matching_articles = []
    for result in results:
        for article_list in result:
            title = article_list.get('title', '')
            if title and title in missing_titles:
                matching_articles.append(article_list)

    return matching_articles
