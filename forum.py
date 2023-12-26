import requests
from bs4 import BeautifulSoup
import json
from format_date import *

class Done:
    def shadowstackre():
        burp0_url = "https://www.shadowstackre.com:443/"
        burp0_headers = {"Sec-Ch-Ua": "\"-Not.A/Brand\";v=\"8\", \"Chromium\";v=\"102\"", 
                         "Sec-Ch-Ua-Mobile": "?0", 
                         "Sec-Ch-Ua-Platform": "\"Windows\"", 
                         "Upgrade-Insecure-Requests": "1", 
                         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36", 
                         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
                         "Sec-Fetch-Site": "none", "Sec-Fetch-Mode": "navigate", 
                         "Sec-Fetch-User": "?1", 
                         "Sec-Fetch-Dest": "document", 
                         "Accept-Encoding": "gzip, deflate", 
                         "Accept-Language": "en-US,en;q=0.9", 
                         "Connection": "close"}
        shadow=requests.get(burp0_url, headers=burp0_headers)
        soup= BeautifulSoup(shadow.content, 'html.parser')
        articles = soup.find_all('article', class_='blog-basic-grid--container')
        result= []
        post_limit = 5
        post_count = 0
        for article in articles:
            time_tag = article.find('time', class_='blog-date')
            title_tag = article.find('h1', class_='blog-title')
            excerpt_tag = article.find('div', class_='blog-excerpt')
            href_tag = article.find('a', class_='blog-more-link')['href']
            image_url = article.select_one('a.image-wrapper img')['data-src']

            article_info = {
                'time': time_tag.text.strip() if time_tag else None,
                'title': title_tag.text.strip() if title_tag else None,
                'excerpt': excerpt_tag.text.strip() if excerpt_tag else None,
                'href': f'https://www.shadowstackre.com:443{href_tag}' if href_tag else None,
                'author':None,
                'img_url': image_url if image_url else None
            }
            result.append(article_info)
            post_count += 1
        
            if post_count == post_limit: 
                break
        # results = json.dumps(result, indent=2)
        return result
             
    def securityaffairs():
        burp0_url = "https://securityaffairs.com:443/"
        burp0_headers = {"Sec-Ch-Ua": "\"-Not.A/Brand\";v=\"8\", \"Chromium\";v=\"102\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Windows\"", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "none", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
        securityaffairs=requests.get(burp0_url, headers=burp0_headers)
        soup = BeautifulSoup(securityaffairs.content, 'html.parser')
        latest_news_section = soup.find('div', class_='latest-news-section')
        news_list = []
        post_limit = 5
        post_count = 0
        news_cards = latest_news_section.find_all('div', class_='news-card')
        for news_card in news_cards:
            news_pic = news_card.find('div', class_='news-card-pic')
            news_cont = news_card.find('div', class_='news-card-cont')
            author_and_post_time = news_cont.find('div', class_='post-time').text.strip().split('\n')
            author = author_and_post_time[0].strip()
            post_time = author_and_post_time[1].strip()
            title = news_cont.find('h5').text.strip()
            href = news_cont.find('a')['href'] if news_cont.find('a') else None
            image_url = news_pic.find('img')['src'] if news_pic.find('img') else None


            news_info = {
                'title': title,
                'excerpt': news_cont.find('p').text.strip(),
                'authors': author,
                'time': post_time,
                'href': href,
                'img_url': image_url
            }
            news_list.append(news_info)
            post_count += 1
        
            if post_count == post_limit: 
                break
        # results = json.dumps(news_list, indent=2)
        return news_list

    def paloalto():
        burp0_url = "https://unit42.paloaltonetworks.com:443/"
        burp0_headers = {"Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Accept-Language": "en-US;q=0.9,en;q=0.8", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36", "Connection": "close", "Cache-Control": "max-age=0"}
        paloalto=requests.get(burp0_url, headers=burp0_headers)
        soup=BeautifulSoup(paloalto.content, 'html.parser')
        news_divs = soup.find_all('article', class_='news mx-auto bg-gray-700')
        post_limit = 5
        post_count = 0
        result= []
        for news_div in news_divs:
            title = news_div.find('h3', class_='h5 news__title mb-15').text.strip()
            article_url = news_div.find('h3', class_='h5 news__title mb-15').a['href']
            authors = [author.text.strip() for author in news_div.select('ul.entry-meta li')[0].find_all('a', class_='author')]
            publish_date = news_div.select('ul.entry-meta li')[1].time['datetime']
            img_url = news_div.find('figure', class_='thumbnail').img['src']

            article_info = {
                'time': publish_date if publish_date else None,
                'title': title if title else None,
                'excerpt': None,
                'href': article_url if article_url else None,
                'authors': authors if authors else None,
                'img_url':img_url if img_url else None
            }
            result.append(article_info)
            post_count += 1
        
            if post_count == post_limit: 
                break
        # results = json.dumps(result, indent=2)
        return result
    
    def volexity():
        burp0_url = "https://www.volexity.com:443/blog/"
        burp0_headers = {"Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Accept-Language": "en-US;q=0.9,en;q=0.8", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36", "Cache-Control": "max-age=0"}
        volexity=requests.get(burp0_url, headers=burp0_headers)
        soup=BeautifulSoup(volexity.content, 'html.parser')
        recent_posts_widget = soup.find('li', class_='widget_recent_entries')
        recent_posts_list = []
        post_limit = 5
        post_count = 0
        recent_post_items = recent_posts_widget.find_all('li')
        for recent_post_item in recent_post_items:
            post_link = recent_post_item.find('a')
            post_info = {
                'title': post_link.text.strip(),
                'url': post_link['href'],
                'time': format(post_link['href'],2,5),
                'excerpt': None,
                'authors': None,
                'img_url':None
                
            }
            recent_posts_list.append(post_info)
            post_count += 1
        
            if post_count == post_limit: 
                break
        # results =json.dumps(recent_posts_list, indent=2)
        return recent_posts_list
    
    def netlab():
        burp0_url = "https://blog.netlab.360.com:443/"
        burp0_headers = {"Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Accept-Language": "en-US;q=0.9,en;q=0.8", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36", "Connection": "close", "Cache-Control": "max-age=0"}
        netlab=requests.get(burp0_url, headers=burp0_headers)
        soup= BeautifulSoup(netlab.content, 'html.parser')
        article_contents = soup.find_all('div', class_='post-card-content')
        post_limit = 5
        post_count = 0
        result = []
        for content in article_contents:
            title = content.find('h2', class_='post-card-title').text.strip()
            excerpt = content.find('div', class_='post-card-excerpt').text.strip()
            authors = content.select('.author-list-item .author-name-tooltip')
            author_names = [author.text.strip() for author in authors]
            date = content.find('time', class_='post-card-meta-date').text.strip()
            link = content.find('a', class_='post-card-content-link')['href']

        
            article_info = {
                'time': date if date else None,
                'title': title if title else None,
                'excerpt': excerpt if excerpt else None,
                'href': f'https://blog.netlab.360.com{link}' if link else None,
                'authors': author_names if author_names else None,
                'img_url':None                
            }
            result.append(article_info)
            post_count += 1
        
            if post_count == post_limit: 
                break
        # results = json.dumps(result, indent=2, ensure_ascii=False)
        return result
    
    def trailofbits():
        burp0_url = "https://blog.trailofbits.com:443/"
        burp0_headers = {"Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Accept-Language": "en-US;q=0.9,en;q=0.8", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36", "Connection": "close", "Cache-Control": "max-age=0"}
        trail=requests.get(burp0_url, headers=burp0_headers)
        soup = BeautifulSoup(trail.content, 'html.parser')
        recent_posts = soup.find('aside', class_='widget widget_recent_entries')
        post_items = recent_posts.find_all('li')
        post_limit = 5
        post_count = 0
        result=[]
        for post_item in post_items:
            title = post_item.a.text.strip()
            href = post_item.a['href'].strip()
            time = format(href,1,4)
            
            article_info = {
                'time': time if time else None,
                'title': title if title else None,
                'excerpt': None,
                'href': href if href else None,
                'authors':None,
                'img_url':None
            }
            result.append(article_info)
            post_count += 1
        
            if post_count == post_limit: 
                break
        # results = json.dumps(result, indent=2, ensure_ascii=False)                  
        return result
    
    def jpcert():
        burp0_url = "https://blogs.jpcert.or.jp:443/en/"
        burp0_headers = {"Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Accept-Language": "en-US;q=0.9,en;q=0.8", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36", "Connection": "close", "Cache-Control": "max-age=0"}
        jpcert=requests.get(burp0_url, headers=burp0_headers)
        soup = BeautifulSoup(jpcert.content, 'html.parser')
        articles = soup.find_all('article')
        post_limit = 5
        post_count = 0
        result=[]
        for article in articles:
            title_div = article.find('div', class_='entry-title')
            title = title_div.find('a').text.strip()
            link = title_div.find('a')['href']
            author_div = soup.find('div', class_='entry-meta__cell-author')
            author_name = author_div.find('p').text.strip()
            date = article.find('time').text.strip()
            summary = article.find('div', class_='entry-lead').text.strip()
            img= article.find('figure', class_='entry-image')
            img_url=img.find('img')['src']
            article_info = {
                'time': date if date else None,
                'title': title if title else None,
                'excerpt': summary if summary else None,
                'href': link if link else None,
                'authors':author_name,
                'img_url':img_url
            }
            result.append(article_info)
            post_count += 1
        
            if post_count == post_limit: 
                break
        # results = json.dumps(result, indent=2, ensure_ascii=False)                  
        return result
        
    def censys():
        burp0_url = "https://censys.com:443/resources/"
        burp0_headers = {"Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Accept-Language": "en-US;q=0.9,en;q=0.8", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36", "Connection": "close", "Cache-Control": "max-age=0"}
        censys=requests.get(burp0_url, headers=burp0_headers)
        soup = BeautifulSoup(censys.content, 'html.parser')
        postcards = soup.find_all('li', class_='pc')
        post_limit = 5
        post_count = 0
        result=[]
        for postcard in postcards:
            title = postcard.find('a', class_='pc-title').text.strip()
            link = postcard.find('a', class_='pc-title')['href']
            
            article_info = {
                            'time': None,
                            'title': title if title else None,
                            'excerpt': None,
                            'href': link if link else None,
                            'authors': None,
                            'img_url':None
                        }
            result.append(article_info)
            post_count += 1
        
            if post_count == post_limit: 
                break
        # results = json.dumps(result, indent=2, ensure_ascii=False)                  
        return result
    
    def troyhunt():
        burp0_url = "https://www.troyhunt.com:443/"
        burp0_headers = {"Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Accept-Language": "en-US;q=0.9,en;q=0.8", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36", "Connection": "close", "Cache-Control": "max-age=0"}
        troyhunt=requests.get(burp0_url, headers=burp0_headers)
        soup= BeautifulSoup(troyhunt.content, 'html.parser')
        posts = soup.find_all('article', class_='article_content')
        result=[]
        post_limit = 5
        post_count = 0
        for post in posts:
            title = post.find('h2', class_='post_title').text
            date = post.find('time')['datetime']
            description = post.find('p', itemprop='description').text
            href = post.find('a', class_='article_link-more')['href']
            article_info = {
                            'time': date if date else None,
                            'title': title if title else None,
                            'excerpt': description if description else None,
                            'href': f'https://troyhunt{href}' if href else None,
                            'authors': None,
                            'img_url':None
                        }
            result.append(article_info)
            post_count += 1
        
            if post_count == post_limit: 
                break
        # results = json.dumps(result, indent=2, ensure_ascii=False)                  
        return result
    
    def intezer():
        burp0_url = "https://intezer.com:443/blog/"
        burp0_headers = {"Accept-Encoding": "gzip, deflate", 
                         "Accept": "*/*", 
                         "Accept-Language": "en-US;q=0.9,en;q=0.8", 
                         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36", 
                         "Connection": "close", 
                         "Cache-Control": "max-age=0"}
        intezer=requests.get(burp0_url, headers=burp0_headers)
        soup = BeautifulSoup(intezer.content, 'html.parser')
        start_tag = soup.find('hr', class_='blog-hr').find_all_next('div', class_='single-post-page')
        post_limit = 5
        post_count = 0
        result=[]
        for post in start_tag:
            href = post.find('a', class_='featured-image-link')['href']
            title = post.find('h2', class_='entry-title').text.strip()
            description = post.find('p', class_='excerpt-text').text.strip()
            date = post.find('div', class_='post-date').text.strip()
            author = post.find('a',class_='author url fn').text.strip()
            img=post.find('div', class_='featured-image-cont rocket-lazyload')['data-bg']
            article_info = {
                            'time': date if date else None,
                            'title': title if title else None,
                            'excerpt': description if description else None,
                            'href': f'{href}' if href else None,
                            'authors': author if author else None,
                            'img_url': img if img else None
                        }
            result.append(article_info)
            post_count += 1
        
            if post_count == post_limit: 
                break
        # results = json.dumps(result, indent=2, ensure_ascii=False)
        return result
    
    def lab52():
        burp0_url = "https://lab52.io:443/blog/"
        burp0_headers = {"Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Accept-Language": "en-US;q=0.9,en;q=0.8", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36", "Connection": "close", "Cache-Control": "max-age=0"}
        lab52=requests.get(burp0_url, headers=burp0_headers)
        soup=BeautifulSoup(lab52.content,'html.parser')
        result=[]
        post_limit = 5
        post_count = 0
        articles = soup.find_all('article')
        for article in articles:
            title = article.find('h2', class_='entry-title').text.strip()
            date = article.find('time', class_='entry-time')['datetime']
            content = article.find('div', class_='entry-content').text.strip()
            author = article.find('span', class_='entry-author-name').text.strip()
            url = article.find('a', class_='entry-title-link')['href']
            img= article.find('a', class_='entry-image-link')
            imgurl=img.find('img')['src']
            article_info = {
                                'time': date if date else None,
                                'title': title if title else None,
                                'excerpt': content if content else None,
                                'href': f'{url}' if url else None,
                                'authors': author if author else None,
                                'img_url':imgurl if imgurl else None
                            }
            result.append(article_info)
            post_count += 1
        
            if post_count == post_limit: 
                break
        # results = json.dumps(result, indent=2, ensure_ascii=False)
        return result
    
    def bitdefender():
        burp0_url = "https://www.bitdefender.com:443/blog/"
        burp0_headers = {"Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Accept-Language": "en-US;q=0.9,en;q=0.8", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36", "Connection": "close", "Cache-Control": "max-age=0"}
        bit=requests.get(burp0_url, headers=burp0_headers)
        soup=BeautifulSoup(bit.content, 'html.parser')
        articles = soup.find_all('div', class_='tw-mb-12 tw-flex-wrap tw-items-center sm:tw-flex')
        result=[]
        post_limit = 5
        post_count = 0
        for article in articles:
            title = article.find('h2', class_='tw-mb-2.5 tw-h-auto tw-overflow-hidden tw-text-lg tw-font-bold tw-no-underline tw-line-clamp-2 lg:tw-text-2xl').text.strip()
            url = article.find('a', class_='tw-block')['href']
            description = article.find('p', class_='tw-h-18 tw-overflow-hidden tw-text-base tw-text-[#7c7c7c] tw-line-clamp-3').text.strip()
            imgurl= article.find('img')['data-src']
            article_info = {
                                'time': None,
                                'title': title if title else None,
                                'excerpt': description if description else None,
                                'href': f'https://www.bitdefender.com/{url}' if url else None,
                                'authors': None,
                                'img_url':imgurl
                            }
            result.append(article_info)
            post_count += 1
        
            if post_count == post_limit: 
                break
        # results = json.dumps(result, indent=2, ensure_ascii=False)
        return result
    
    def kaspersky():
        burp0_url = "https://www.kaspersky.com:443/blog/"
        burp0_headers = {"Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Accept-Language": "en-US;q=0.9,en;q=0.8", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36", "Connection": "close", "Cache-Control": "max-age=0"}
        kas=requests.get(burp0_url, headers=burp0_headers)
        soup=BeautifulSoup(kas.content,'html.parser')
        articles = soup.find_all('div', class_='o-col-6@sm o-col-4@lg')
        result=[]
        post_limit = 5
        post_count = 0
        for article in articles:
            title = article.find('h3', class_='c-card__title').find('a').text.strip()
            url = article.find('h3', class_='c-card__title').find('a')['href']
            description = article.find('div', class_='c-card__desc').text.strip()
            author = article.find('li', class_='c-card__author').find('a').text.strip()
            date_published = article.find('li', class_='c-card__time').find('time')['datetime']
            imgurl=article.find('figure',class_='c-card__figure')
            img_url=imgurl.find('img')['src']
            article_info = {
                                'time': date_published if date_published else None,
                                'title': title if title else None,
                                'excerpt': description if description else None,
                                'href': url if url else None,
                                'authors': author if author else None,
                                'img_url':img_url if img_url else None
                            }
            result.append(article_info)
            post_count += 1
        
            if post_count == post_limit: 
                break
        # results = json.dumps(result, indent=2, ensure_ascii=False)
        return result
    
    def malwarebyte():
        burp0_url = "https://www.malwarebytes.com:443/blog"
        burp0_headers = {"Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Accept-Language": "en-US;q=0.9,en;q=0.8", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36", "Connection": "close", "Cache-Control": "max-age=0"}
        malbyte=requests.get(burp0_url, headers=burp0_headers)
        soup=BeautifulSoup(malbyte.content,'html.parser')
        articles = soup.find_all('div', class_='blog-list__content')
        result=[]
        post_limit = 5
        post_count = 0
        for article in articles:
            title = article.h4.a.text
            link = article.h4.a['href']
            author = article.find('div', class_='blog-author').a.text
            date = article.find('div', class_='blog-date').span.text
            description = article.find('div', class_='blog-list__content-wrap').p.text

            article_info = {
                                'time': date if date else None,
                                'title': title if title else None,
                                'excerpt': description if description else None,
                                'href': link if link else None,
                                'authors': author if author else None,
                                'img_url': None
                            }
            result.append(article_info)
            post_count += 1
        
            if post_count == post_limit: 
                break
        # results = json.dumps(result, indent=2, ensure_ascii=False)
        return result
    
    def mandiant():
        burp0_url = "https://www.mandiant.com:443/resources/blog"
        burp0_headers = {"Sec-Ch-Ua": "\"-Not.A/Brand\";v=\"8\", \"Chromium\";v=\"102\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Windows\"", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "none", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"}
        mandiant=requests.get(burp0_url, headers=burp0_headers)
        soup= BeautifulSoup(mandiant.content, 'html.parser')
        result=[]
        post_limit = 5
        post_count = 0
        for resource_card in soup.find('div', class_='cols cols-3').find_all_next('a', class_='resources-card'):
            link = resource_card['href']
            title = resource_card.find('h3', class_='title').text
            date = resource_card.find('span', class_='date').text
            description = resource_card['aria-label']
            article_info = {
                                'time': date if date else None,
                                'title': title if title else None,
                                'excerpt': description if description else None,
                                'href': link if link else None,
                                'authors': None,
                                'img_url':'https://www.mandiant.com/sites/default/files/2023-01/blog-thumb.jpg'
                            }
            result.append(article_info)
            post_count += 1
        
            if post_count == post_limit: 
                break
        # results = json.dumps(result, indent=2, ensure_ascii=False)
        return result
    
    def resecur():
        burp0_url = "https://www.resecurity.com:443/blog"
        burp0_headers = {"Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Accept-Language": "en-US;q=0.9,en;q=0.8", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36", "Connection": "close", "Cache-Control": "max-age=0"}
        resec=requests.get(burp0_url, headers=burp0_headers)
        soup=BeautifulSoup(resec.content, 'html.parser')
        result=[]
        post_limit = 5
        post_count = 0
        for card in soup.find_all('div', class_='col-lg-6 card full small-screen-align'):
            link = card.find('a')['href']
            title = card.find('div', class_='news-title').text
            date = card.find('time')['datetime']
            tags = card.find('p', class_='tags').text
            imgurl=card.find('div', class_='image-plug blog mb-6')
            img_url= imgurl.find('img')['src']
            article_info = {
                                'time': date if date else None,
                                'title': title if title else None,
                                'excerpt': None,
                                'href': f'https://www.resecurity.com{link}' if link else None,
                                'authors': None,
                                'img_url': img_url
                            }
            result.append(article_info)
            post_count += 1
        
            if post_count == post_limit: 
                break
        # results = json.dumps(result, indent=2, ensure_ascii=False)
        return result
    
    def zimper():
        burp0_url = "https://www.zimperium.com:443/blog/"
        burp0_headers = {"Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Accept-Language": "en-US;q=0.9,en;q=0.8", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36", "Connection": "close", "Cache-Control": "max-age=0"}
        zimper=requests.get(burp0_url, headers=burp0_headers)
        soup=BeautifulSoup(zimper.content, 'html.parser')
        articles = soup.find_all('article')
        result=[]
        post_limit = 5
        post_count = 0
        for article in articles:
            title_tag = article.find('h2')
            title = title_tag.text.strip()
            link = title_tag.find('a')['href']
            entry_meta = article.find('div', class_='entry-meta')
            date_published = entry_meta.find('span', class_='published').text.strip()
            author = entry_meta.find('span', class_='author').text.strip()
            content = article.find('div', class_='entry-content').text.strip()
            # img =article.find('img')
            # imgurl=img['src']
            article_info = {
                                'time': date_published if date_published else None,
                                'title': title if title else None,
                                'excerpt': content if content else None,
                                'href': link if link else None,
                                'authors': author if author else None,
                                'img_url':None
                            }
            result.append(article_info)
            post_count += 1
        
            if post_count == post_limit: 
                break
        # results = json.dumps(result, indent=2, ensure_ascii=False)
        return result

class Pending:
    def group_ib():
        burp0_url = "https://www.group-ib.com:443/blog/"
        burp0_cookies = {"cfidsgib-w-61354c22-16cc-40a8-a871-6901f1a76e24": "Lm9hc+W/syI/s8kiZ7pDDL8q0YpJ/IxnJ3Q7v/g+qpuzGM5L2CoP/A3kGmJ9u/rncka/KgA3MPOttpbiyVQsu/y3BCzqdymWIjwx09fRoWqIaMI+cZyPsp4vlWglJ8g/QFMr1WpGjRCCDgZxGINDBs/DRYghLJHT8m+U", "cfidsgib-w-61354c22-16cc-40a8-a871-6901f1a76e24": "Lm9hc+W/syI/s8kiZ7pDDL8q0YpJ/IxnJ3Q7v/g+qpuzGM5L2CoP/A3kGmJ9u/rncka/KgA3MPOttpbiyVQsu/y3BCzqdymWIjwx09fRoWqIaMI+cZyPsp4vlWglJ8g/QFMr1WpGjRCCDgZxGINDBs/DRYghLJHT8m+U", "gsscgib-w-61354c22-16cc-40a8-a871-6901f1a76e24": "MKEPfCSZLGGEcH2R7fctz0ft6As786vftGABu/beFddytkbdLpgnNS9U1DDv2cI1mRDz/ndfjoqnkKkEU2TPnYXAe7qMOz6dIjxxqIShqWerZE3M84WMsGi6bar3EDDbWsYFzToMSDijxAEUGR9m8fRbV+NULuxhUwPNEsFM17a89ZLSBEAeXhAP0zgAIeL02/ysy0GEde1MkQSKPBjpzevdh5I4yWcdSr0SiuaK+NDDe6VgWCI/SM1fPdya9XLJ", "gsscgib-w-61354c22-16cc-40a8-a871-6901f1a76e24": "MKEPfCSZLGGEcH2R7fctz0ft6As786vftGABu/beFddytkbdLpgnNS9U1DDv2cI1mRDz/ndfjoqnkKkEU2TPnYXAe7qMOz6dIjxxqIShqWerZE3M84WMsGi6bar3EDDbWsYFzToMSDijxAEUGR9m8fRbV+NULuxhUwPNEsFM17a89ZLSBEAeXhAP0zgAIeL02/ysy0GEde1MkQSKPBjpzevdh5I4yWcdSr0SiuaK+NDDe6VgWCI/SM1fPdya9XLJ", "fgsscgib-w-61354c22-16cc-40a8-a871-6901f1a76e24": "vAw88efa59f0ae40d6fae5c587c130765d03887f", "fgsscgib-w-61354c22-16cc-40a8-a871-6901f1a76e24": "vAw88efa59f0ae40d6fae5c587c130765d03887f", "__zzatgib-w-61354c22-16cc-40a8-a871-6901f1a76e24": "MDA0dBA=Fz2+aQ==", "__zzatgib-w-61354c22-16cc-40a8-a871-6901f1a76e24": "MDA0dBA=Fz2+aQ=="}
        burp0_headers = {"Sec-Ch-Ua": "\"-Not.A/Brand\";v=\"8\", \"Chromium\";v=\"102\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Windows\"", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Dest": "document", "Referer": "https://www.group-ib.com/blog/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"}
        group_ib=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
        soup = BeautifulSoup(group_ib.content, 'html.parser')
        blog_posts_wrapper = soup.find('div', class_='blog-posts__wrapper')
        blog_posts_list = []
        print(blog_posts_wrapper)
        blog_post_cards = blog_posts_wrapper.find_all('a', class_='blogpost-card')

        for blog_post_card in blog_post_cards:
            blogpost_card_image = blog_post_card.find('div', class_='blogpost-card__image')
            blogpost_card_info = blog_post_card.find('div', class_='blogpost-card__info')

            blog_post_info = {
                'title': blogpost_card_info.find('div', class_='blogpost-card__title').text.strip(),
                'category': blogpost_card_info.find('div', class_='blogpost-card__meta').text.strip(),
                'date': blogpost_card_info.find('div', class_='blogpost-card__meta').text.strip().split('·')[-1].strip(),
                'text': blogpost_card_info.find('div', class_='blogpost-card__text').text.strip(),
                'image_url': blogpost_card_image.find('img')['data-src'],
                'article_url': blog_post_card['href'],
                'author': blogpost_card_info.find('div', class_='blogpost-card__authors').find('div', class_='subtitle').text.strip(),
                'views': blogpost_card_info.find('div', class_='post-views-count').text.strip()
            }
            blog_posts_list.append(blog_post_info)
        for blog_post_info in blog_posts_list:
            print(blog_post_info)
            print('-' * 50)
    
    def trendmicro():
        
            return
