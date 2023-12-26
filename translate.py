import pyperclip
import undetected_chromedriver as uc
import urllib3
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from selenium.webdriver.common.keys import Keys

from scrapt_library import *

urllib3.disable_warnings()


def wait_for_answer(driver):
    print("Waiting")
    while True:
        try:
            # btn = getElements(driver, "btn relative btn-neutral whitespace-nowrap border-0 md:border")
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            button_element = soup.select('.rounded-full.border-2')
            if button_element:
                print('wait for 5 second')
                wait(5)
            else:
            # Nếu không có button_element, kiểm tra và click vào button "Continue generating"
                continue_btn = getElement(driver,'button.btn.relative.btn-neutral')
                
                if continue_btn.text.lower() == "continue generating":
                    continue_btn.click()
                    print("Clicked on 'Continue generating' button.")
                    time.sleep(0.5)
        except Exception as e:
            
            print('eer', e)
            
        # print(getElmText(btn[0]).lower())
        # try:
        #     if len(btn) > 0 and getElmText(btn[0]).lower() == "stop generating":
        #         wait(0.5)
        #         continue
        #     elif getElmText(btn[0]).lower() == "continue generating":
        #         continueBtn = getElement(driver, "button.btn.relative.btn-neutral")
        #         clickToElm(driver, continueBtn)
        #         wait(0.5)
        #         continue
        # except Exception as e:
        #     print("ERR", e)
        # wait(3)
        


def send_prompt(driver, prompt):
    print("SENDING PROMPT")
    wait(1)
    textarea = getElement(driver, "textarea")
    pyperclip.copy(prompt)
    textarea.send_keys(Keys.CONTROL + "v")
    # textarea.send_keys(prompt)
    wait(1)
    sendBtn = getElement(driver, "form button.absolute")
    clickToElement(driver, sendBtn)
    wait_for_answer(driver=driver)
    answers = getElements(driver, ".w-full .text-base .markdown")
    answer = answers[len(answers) - 1]
    value = getElmHtml(answer)
    print(value)
    return value


def newBrowser(profileName):
    options = uc.ChromeOptions()
    options.add_argument("--no-sandbox")
    # options.add_argument('--headless')
    options.add_argument("--enable-javascript")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-sync")
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"

    options.add_argument("User-Agent={0}".format(user_agent))
    options.user_data_dir = profileName
    options.add_argument("--profile-directory=" + profileName)
    driver = uc.Chrome(options=options)
    return driver


class ChatModelAdapter:
    profiles = [
        "chatgpt1",
    ]
    drivers = {}

    def __init__(self):
        for i in self.profiles:
            self.drivers[i] = newBrowser(i)

    def translate(self, article, profile):
        """
        Need to get all the article before any summary task.
        """
        driver: uc.Chrome = self.drivers.get(profile)
        driver.get("https://chat.openai.com/?")
        time.sleep(3)
        translate_prompt = f"""As a cyber security specialist, translate this paragraph into Vietnamese. No need to explain or introduce, just translate: 

{(article)}. 
"""
        ans = {}
        value = send_prompt(driver=driver, prompt=translate_prompt)

        ans["translate"] = value

        self.drivers.append(driver)
        return ans
model  = ChatModelAdapter()
article="""  Unfortunately for Lisa, Emilia’s team has long been monitoring newly registered domains (NRDs),
        and they have applied extra scrutiny to these domains. Emilia’s team scraped the sites’ content, analyzed
        registration behavior and discovered the underlying infrastructure. (This is just as we at Palo Alto Networkspay
        special attention to NRDs, finding manymalicious ones). As a result, Lisa’s scam websites were swiftly found and
        taken down.Lisa was determined to succeed. So, before launching the puppy scam campaigns, she started
        aging domain names used for the websites. As Emilia monitored various scam campaigns, she quickly caught on to
        the tactic of strategically aging domains (seeour research on aged domains) and set her team to watch for when
        dormant domains get activated.To evade having her sites scraped by Chief Emilia’s team, Lisa employed a
        variety of tactics. These included cloaking (showing benign content to suspected crawling bots) and user
        targeting (showing malicious content only to specific users).Researchers have shownthat cybercriminals
        use various cloaking and user-targeting techniques, which pose a significant challenge to detect malicious
        domains. Palo Alto Networksinspects web traffic inline, ensuring we block malicious websites even if they
        leverage cloaking or user-targeting practices.Inline detection has its limitations, so Emilia’s team
        set out to combine a variety of large datasets (including certificate logs and pDNS) to train a machine learning
        model. This model can find malicious domains leveraging similar automation or infrastructure, or that the same
        criminal group owns.Ultimately, it became tough for Lisa to maintain her scam campaigns without getting
        caught.One day, while looking at a real web shop that sold puppies, she saw one that looked exactly
        like the one she wanted as a little girl. She suddenly realized all the evil she had done and decided to give up
        her life of crime. She adopted the puppy as an adult and joined Emilia’s team to fight cybercrime to undo some
        of her wrongdoing.Unfortunately, not all cybercriminals have turned their life around, so we have
        plenty of similar examples to examine in the real world. Figure 1 shows a real-life puppy scam website
        (baronessabernesemountaindogpuppies[.]com) and how our detection model gives an advantage in detecting this
        scam.Threat actors registered this site on April 21, 2023. Our stockpiled detector first flagged it on
        April 24, 2023. Two days later, one vendor on VirusTotal marked it as malicious. Then on Aug. 22, 2023,
        volunteers on a scam-hunting websiteArtists Against 419marked it as a scam site.Fighting the domain
        wars is a global community effort where we lean on previous work by academic researchers, law enforcement,
        cybersecurity professionals, policymakers and volunteers. Researchers in the past have shown
        thatWHOISandpDNSdata are useful for finding malicious domain names registered in bulk.More
        recently,researchers looking into certificate datasetsdiscovered they can use these datasets to find stockpiled
        domains (potentially independent of registration time) where certificates were set up similarly because the
        criminals likely used automated scripts. Closest to our work is research byAlSabah et al., where the authors
        looked at both certificate transparency logs and pDNS to identify phishing domains.Recognizing that
        automation can leave us crumbs of information in different datasets, we extracted features from certificate
        transparency logs, pDNS data and domain name strings that our detector can use to find malicious domain names.
        Browsers enforce certificate transparency to monitor and audit certificates to make it harder for cybercriminals
        to use malicious certificates (e.g., when a certificate authority is compromised).We collect millions
        of certificates and domains every day from multipletransparency log serversthat maintain immutable records of
        certificates. Similarly,pDNSis a database of DNS request-response pairs passively collected from all over the
        world (e.g., when users access various web resources or send emails). Our pDNS database consists of billions of
        DNS records daily.From these datasets, we collect the following six categories of features as shown in
        Figure 2."""
model.translate(article,'chatgpt1')
    