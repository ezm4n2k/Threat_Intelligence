from bs4 import BeautifulSoup

html_content = """
<html>

<body><p>ByJanos Szurdi,Shehroze FarooqiandNabeel Mohamed</p><p>December 15, 2023 at 3:00 PM</p><p>
        Category:Malware</p><p>Tags:Advanced URL Filtering,Cloud-Delivered Security Services,Cybercrime,DNS,DNS
        security,Malicious Domains,next-generation firewall,Phishing,Scams</p><img
        src='https://unit42.paloaltonetworks.com/wp-content/uploads/2023/12/Unit42-blog-2by1-characters-r4d1-2020_Cyber-squatting-v3.png'
        alt='Image'><p>This post is also available in:日本語(Japanese)</p><p>Malicious actors often acquire a large
        number of domain names (called stockpiled domains) at the same time or set up their infrastructure in an
        automated fashion. They do so, for example, by creating DNS settings and certificates for these domains using
        scripts.</p><p>Automation employed by attackers can leave traces of information about their campaigns in
        various data sources. Security defenders can find these traces in locations such as certificate transparency
        logs (e.g., certificate field reputation or timing information) and passive DNS (pDNS) data (e.g.,
        infrastructure reuse or characteristics).</p><p>Leveraging these crumbs of information, we built a detector to
        identify stockpiled domains. The two main advantages of detecting stockpiled domains are expanding coverage of
        malicious domains and providing patient-zero detections as attackers stock up on domains for future use.</p>
    <p>To detect stockpiled domains, we engineered over 300 features to process many terabytes of data and billions of
        pDNS and certificate records. We used a knowledge base of millions of malicious and benign domains to calculate
        certificate and pDNS reputation and to train and test a Random Forest machine learning algorithm.</p><p>As of
        July 2023, our detection pipeline has found 1,114,499 unique stockpiled root domain names and identifies tens of
        thousands of malicious domains weekly. Our model, on average, found stockpiled domains 34.4 days earlier
        compared to vendors on VirusTotal. The success of our approach emphasizes the need to combine multiple large
        datasets, such as passive DNS and certificate logs, to detect malicious campaigns.</p><p>The stockpiled
        detector continuously picks up a wide variety of scam, phishing, malware distribution, C2 and other campaigns.
        Some of these phishing campaigns target the largest software companies, online retail shops, banks, streaming
        services and more. In this article, we share both large campaigns leveraging thousands of domains and small
        campaigns involving just a few domains.</p><p>Palo Alto Networks customers receive protection against
        stockpiled domains by leveraging our automated classifier in multiplePalo Alto Networks Next-Generation
        Firewallcloud-delivered security services, includingAdvanced Wildfire,DNS SecurityandAdvanced URL Filtering.</p>
    <p>Overview of the Domain WarsThe Misadventures of Lisa and the Puppy Scam SiteScam Sites in the Real WorldEarly
        Detection of Malicious/Phishing DomainsDetecting Stockpiled Domain NamesCertificate-Specific
        FeaturesDomain-Specific Certificate FeaturesCertificate Reputation and Aggregation Features for Various
        Certificate FieldsLexical Features for DomainspDNS Reputation and Aggregation FeaturesAggregate Features for
        Certificates and pDNSA Malicious Redirection CampaignA European Postal Phishing CampaignA USPS Phishing
        CampaignA High-Yield Investment Scam CampaignConclusionAcknowledgmentsIndicators of CompromiseAdditional
        Resources</p><p>In our previous article onfast fluxing, we described how, over time, techniques used by
        cybercriminals evolved into the domain wars. This ongoing struggle involves criminals registering many domain
        names to make it harder for law enforcement to take down their botnets.</p><p>The domain wars have spread
        across all types of online crime, including:</p><p>In this article, we return to our fictional scenario of an
        interaction between cybercriminals and law enforcement, namely Chief Emilia and Lisa (who is the sister of Bart
        from our previousepisode).</p><p>We’ll also discuss multiple campaigns that we’ve detected with our model, as
        a way of illustrating how we can use various features to improve protection.</p><p>In our fictional scenario,
        Chief Emilia saw that even though stricter registration policy changes thatresearchers had proposedcould be
        useful, these changes would take a long time. These changes also wouldn’t be enough by themselves to solve the
        domain wars. Thus, she created a research team to collect data about malicious domain names and to develop
        detectors to identify them.</p><p>In the meantime, our budding cybercriminal Lisa had an evil plan. Lisa
        hasn’t always been evil. In fact, she was a very good-hearted person. But her parents never let her have a
        puppy, and slowly, she turned sour.</p><p>One day, Lisa decided that if she couldn’t have a puppy as a kid,
        then no other kids could. She began her descent into evil by launching puppy scam websites. Figure 1 shows a
        real-life example of a puppy scam site.</p><p>Figure 1. Screenshot of a puppy scam
        websitebaronessabernesemountaindogpuppies[.]com.She started this endeavor by stockpiling a bunch of domain names
        and cutting together content from real puppy web shops but with fraudulent email addresses, phone numbers and
        payment sites. (We call these domains registered by the same actor for use in malicious campaigns stockpiled
        domains.)</p><img src='https://unit42.paloaltonetworks.com/wp-content/uploads/2023/12/word-image-131595-1.png'
        alt='Image'><p>Unfortunately for Lisa, Emilia’s team has long been monitoring newly registered domains (NRDs),
        and they have applied extra scrutiny to these domains. Emilia’s team scraped the sites’ content, analyzed
        registration behavior and discovered the underlying infrastructure. (This is just as we at Palo Alto Networkspay
        special attention to NRDs, finding manymalicious ones). As a result, Lisa’s scam websites were swiftly found and
        taken down.</p><p>Lisa was determined to succeed. So, before launching the puppy scam campaigns, she started
        aging domain names used for the websites. As Emilia monitored various scam campaigns, she quickly caught on to
        the tactic of strategically aging domains (seeour research on aged domains) and set her team to watch for when
        dormant domains get activated.</p><p>To evade having her sites scraped by Chief Emilia’s team, Lisa employed a
        variety of tactics. These included cloaking (showing benign content to suspected crawling bots) and user
        targeting (showing malicious content only to specific users).</p><p>Researchers have shownthat cybercriminals
        use various cloaking and user-targeting techniques, which pose a significant challenge to detect malicious
        domains. Palo Alto Networksinspects web traffic inline, ensuring we block malicious websites even if they
        leverage cloaking or user-targeting practices.</p><p>Inline detection has its limitations, so Emilia’s team
        set out to combine a variety of large datasets (including certificate logs and pDNS) to train a machine learning
        model. This model can find malicious domains leveraging similar automation or infrastructure, or that the same
        criminal group owns.</p><p>Ultimately, it became tough for Lisa to maintain her scam campaigns without getting
        caught.</p><p>One day, while looking at a real web shop that sold puppies, she saw one that looked exactly
        like the one she wanted as a little girl. She suddenly realized all the evil she had done and decided to give up
        her life of crime. She adopted the puppy as an adult and joined Emilia’s team to fight cybercrime to undo some
        of her wrongdoing.</p><p>Unfortunately, not all cybercriminals have turned their life around, so we have
        plenty of similar examples to examine in the real world. Figure 1 shows a real-life puppy scam website
        (baronessabernesemountaindogpuppies[.]com) and how our detection model gives an advantage in detecting this
        scam.</p><p>Threat actors registered this site on April 21, 2023. Our stockpiled detector first flagged it on
        April 24, 2023. Two days later, one vendor on VirusTotal marked it as malicious. Then on Aug. 22, 2023,
        volunteers on a scam-hunting websiteArtists Against 419marked it as a scam site.</p><p>Fighting the domain
        wars is a global community effort where we lean on previous work by academic researchers, law enforcement,
        cybersecurity professionals, policymakers and volunteers. Researchers in the past have shown
        thatWHOISandpDNSdata are useful for finding malicious domain names registered in bulk.</p><p>More
        recently,researchers looking into certificate datasetsdiscovered they can use these datasets to find stockpiled
        domains (potentially independent of registration time) where certificates were set up similarly because the
        criminals likely used automated scripts. Closest to our work is research byAlSabah et al., where the authors
        looked at both certificate transparency logs and pDNS to identify phishing domains.</p><p>Recognizing that
        automation can leave us crumbs of information in different datasets, we extracted features from certificate
        transparency logs, pDNS data and domain name strings that our detector can use to find malicious domain names.
        Browsers enforce certificate transparency to monitor and audit certificates to make it harder for cybercriminals
        to use malicious certificates (e.g., when a certificate authority is compromised).</p><p>We collect millions
        of certificates and domains every day from multipletransparency log serversthat maintain immutable records of
        certificates. Similarly,pDNSis a database of DNS request-response pairs passively collected from all over the
        world (e.g., when users access various web resources or send emails). Our pDNS database consists of billions of
        DNS records daily.</p><p>From these datasets, we collect the following six categories of features as shown in
        Figure 2.</p><img
        src='https://unit42.paloaltonetworks.com/wp-content/uploads/2023/12/word-image-131595-2.jpeg' alt='Image'><p>
        Then we follow a series of steps to gather further information.</p><p>Certificate-Specific Features</p><p>
        These features include, for example, the validity length of the certificate or the number of root domain names
        in the certificate. When cybercrooks automate their processes, they might not think to change these details.</p>
    <p>Domain-Specific Certificate Features</p><p>These features include, for example, the number of certificates
        and issuers we see for a domain name, which would signal that their owners treat them similarly.</p><p>
        Certificate Reputation and Aggregation Features for Various Certificate Fields</p><p>For example, this
        category includes the proportion of malicious domain names or the distribution of words for specific fields of
        certificates. We compute reputation scores for certificate fields (e.g., validity length, seen time, not before
        field and fingerprint). Certificate reputation features help our classifier understand certain field values
        commonly set by malicious operations.</p><p>Lexical Features for Domains</p><p>From the domain name itself,
        we calculate features like the randomness of the name, the number of words, encoding of the top-level domain
        (TLD), and whether there is a brand name in the domain name. These features help us capture whether a malicious
        campaign is targeting a specific set of brands, or if the same algorithm generated the domain names.</p><p>
        pDNS Reputation and Aggregation Features</p><p>From pDNS we calculate features like the known malicious and
        benign proportions of domains and the average domain age or the number of certificates for an IP (or
        a/24subnet). PDNS reputation helps us understand more about the shared infrastructure of stockpiled domain
        names.</p><p>Aggregate Features for Certificates and pDNS</p><p>These features include, for example, the
        number of IPs of all the domains in a certificate. Aggregating across multiple data sources (e.g., certificates
        and pDNS) is essential to understanding the deeper connection between certificate setup and the infrastructure
        of stockpiled domain names.</p><p>After generating features from domain names, certificate logs and pDNS, we
        train aRandom Forestmachine learning classifier to predict stockpiled domain names. We leverage our extensive
        knowledge of millions of malicious and benign domain names as labeled data for training and fine-tuning the
        classifier for high precision.</p><p>Our classifier can achieve 99% precision with 48% recall, even though
        many of the malicious domains might not be stockpiled or cybercriminals might not leave traces of information in
        certificate logs and passive DNS data.</p><p>Our detection pipeline has found 1,114,499 unique stockpiled root
        domain names since July 2023, identifying tens of thousands of malicious domains weekly. Other content and
        behavior analysis-based detectors later identified 45,862 malware, 8,989 phishing and 844 C2 domains among the
        stockpiled domains.</p><p>Our model caught stockpiled domains on average 34.4 days earlier than vendors on
        VirusTotal. We expect the average delay to grow as other detectors find already identified stockpiled domains.
    </p><p>Our stockpiled detector picked up a variety of campaigns including scams, phishing, malware distribution
        and C2. Below, we share a few interesting campaigns that our stockpiled detector was able to detect early.</p>
    <p>Our detector captured more than 9,000 registered domains that were part of a malicious redirection campaign, for
        example:</p><p>VirusTotal vendors were only able to mark 31.7% of these domains as malicious. Even when they
        found a domain to be malicious, our detector was capable of finding them 32.3 days earlier on average.</p><p>
        Perpetrators rarely set up such a large campaign without leaving some valuable information for our machine
        learning model. Even though these domains use Cloudflare, which makes pDNS-based identification challenging, we
        can follow other trails.</p><p>In a recent example, perpetrators randomly generated domains using low-quality
        TLDs. Also, all the domains had the same validity length for their certificates. And while their activation
        dates are different, perpetrators activated them all fairly recently.</p><p>In this campaign, victims are
        redirected to different websites before reaching a landing page, which is usually an adware or a scam page. For
        example, Figure 3 shows a screenshot of the final payload received by our crawler after redirections.</p><p>In
        both cases, our crawler was redirected to a fake notification scam with clickbait. A fake warning message was
        displayed to trick people into allowing an attacker-controlled website to send browser notifications.
        Additionally, both pages have a clickbait advertisement at the bottom of the website.</p><p>Figure 3. Fake
        warning message after an example of malicious redirection frompbyiyyht[.]gq.Further analysis shows that all
        these hostnames redirected users to one of two hostnames (i.e.,thewinjackpot[.]lifeandwinjackpot[.]life). From
        the visual analysis of the content of a few detected hostnames, we found that a URL of these two hostnames was
        assigned towindows.location.hrefwith a timeout (shown in Figure 4). We surmise the campaign owner likely owns
        both these hostnames, and they later redirect victims to other websites.</p><img
        src='https://unit42.paloaltonetworks.com/wp-content/uploads/2023/12/word-image-131595-3.jpeg' alt='Image'><img
        src='https://unit42.paloaltonetworks.com/wp-content/uploads/2023/12/word-image-131595-4.png' alt='Image'><p>In
        a postal phishing campaign targeting Italian- and German-speaking users, the phishing page harvested victims’
        login credentials. Our detector found a group of related domains.</p><p>Vendors on VirusTotal marked only two
        out of our four example domains as malicious:</p><p>Abschlussschritte-info[.]comwas registered on June 2,
        2023, and our detector found it to be malicious ten days later, on June 12, 2023. We only saw VirusTotal vendors
        detecting it two months later, on Aug. 11, 2023.</p><p>Figure 5 shows what the original webpageposte[.]itlooks
        like.</p><p>Figure 5. The legitimate Italian postal service pageposte[.]it.Figure 6 is a screenshot of the
        phishing domain222camo[.]comthat is impersonating the original website.</p><img
        src='https://unit42.paloaltonetworks.com/wp-content/uploads/2023/12/word-image-131595-5.png' alt='Image'><p>
        Figure 6. A phishing domain222camo[.]comimpersonatingposte[.]it.These four domains clearly had the same content
        and were part of the same campaign. However, there were a few signals related to automation for our detector to
        use.</p><img src='https://unit42.paloaltonetworks.com/wp-content/uploads/2023/12/word-image-131595-6.png'
        alt='Image'><p>Although these domains had the same validity length, they were registered on vastly different
        dates and used different IP addresses. Thus, our model mainly relied on certificate field-based and pDNS-based
        reputation features to identify the domains in this campaign.</p><p>Our detector caught a campaign
        impersonating the United States Postal Service (USPS) where more than 30 domains (including the following
        examples) are used to host the same website shown in Figure 7:</p><p>These domains are registered under only
        four certificates. Our stockpiled domain detector caught all these domains before VirusTotal first detected
        them. We detected some of these domains days (e.g.,usps-redelivery[.]art– 3 days) or weeks
        (e.g.,usps-redelivery[.]live– 2 weeks) ahead of other vendors.</p><p>These domains were registered in the time
        span between June 17, 2023, and Aug. 28, 2023, and the domain certificates were obtained on the same day of
        registration. The aggregation of domains into a few certificates and the correlation to domain creation time
        suggests that threat actors created these domains with some level of automation. This automation allowed us to
        connect the dots and detect all of these malicious stockpiled domains.</p><img
        src='https://unit42.paloaltonetworks.com/wp-content/uploads/2023/12/word-image-131595-7.png' alt='Image'><p>
        One of these campaigns consisted of more than 17 domains focusing on high-yield investment scams. In these
        campaigns, scammers try to convince users that in return for a small initial investment, they would earn a lot
        of money.</p><p>The following are a few example domains in this campaign:</p><p>While VirusTotal vendors
        found 12 out of 17 of these domains, on average they found them 34.7 days later than our detector.</p><p>When
        criminals set these domains up for their malicious campaigns, they left crumbs of information. For example, all
        the domains had the same validity length for their certificates, and they used the same IP address. While their
        registration dates are different, and they had more than one registrar, they were all newly registered domains.
    </p><p>At first, customers will be presented with a page (shown in Figure 8) that asks for very little. Give us
        your name and email address in return for earning $500 deposits. What is there to lose, right?</p><p>After
        filling out the information, victims will be redirected to another page to double-check if they’re ready to be
        tricked.</p><p>Figure 8. Scam domainerinemailbiz[.]cominitial page screenshot.People who fill out the
        information and click the submission button will be redirected tocheckout.mytraffic[.]biz, as shown in Figure 9.
        On this page, victims are asked if they want a massive discount. But when they click “Yes,” they’re redirected
        to the final landing page.</p><img
        src='https://unit42.paloaltonetworks.com/wp-content/uploads/2023/12/Stockpile-F8.png' alt='Image'><p>Figure 9.
        Redirection page fromerinemailbiz[.]comtocheckout.mytraffic[.]biz.Finally, the victims are redirected to the
        landing page oncheckout.mytraffic[.]biz(shown in Figure 10). The page checks every checkbox for a phishing page:
    </p><img src='https://unit42.paloaltonetworks.com/wp-content/uploads/2023/12/word-image-131595-9.png'
        alt='Image'><p>We hope not many people filled in their credit card information at the bottom.</p><img
        src='https://unit42.paloaltonetworks.com/wp-content/uploads/2023/12/Stockpile-F10.png' alt='Image'><p>As the
        domain wars unfolded, cybercriminals started to automate their infrastructure setup. However, bulk domain
        registration and infrastructure automation can leave crumbs of information that allow us to detect stockpiled
        domains. The success of our approach emphasizes the need for security defenders looking to improve their
        detection to combine multiple large datasets, such as pDNS and certificate logs, to uncover malicious campaigns.
    </p><p>Our high-precision, machine learning-based detector processes terabytes of certificate and DNS logs to
        discover thousands of stockpiled domains weekly. Our detection pipeline has uncovered a wide variety of
        different types of campaigns earlier than VirusTotal vendors, and we also found domains that were not detected
        by others.</p><p>Palo Alto Networks customers receive protection against stockpiled domains by leveraging our
        automated classifier in multiplePalo Alto Networks Next-Generation Firewallcloud-delivered security services,
        includingDNS SecurityandAdvanced URL Filtering.</p><p>TheAdvanced WildFiremachine-learning models and analysis
        techniques have been reviewed and updated in light of the IoCs shared in this research.</p><p>We want to thank
        George Jones, Arun Kumar, Alex Starov, Lysa Myers, Bradley Duncan, Erica Naone and Jun Javier Wang for their
        invaluable input on this post.</p><p>Puppy Scam Example Domain</p><p>Malicious Redirection Campaign Domains
    </p><p>Postal Phishing Campaign Domains</p><p>A Sample of USPS Phishing Campaign Domains</p><p>USPS Phishing
        Campaign Certificate SHA-1 Fingerprints</p><p>High Yield Investment Scam Campaign Domains</p><p>Sign up to
        receive the latest news, cyber threat intelligence and research from us</p><p>Please enter your email address!
    </p><p>Please mark, I'm not a robot!</p><p>By submitting this form, you agree to ourTerms of Useand acknowledge
        ourPrivacy Statement.</p></body>

</html>
"""

def merge_adjacent_paragraphs(html):
    soup = BeautifulSoup(html, 'html.parser')
    paragraphs = soup.find_all('p')
    
    # Merge adjacent paragraphs
    for i in range(len(paragraphs)-1, 0, -1):
        if paragraphs[i].previous_sibling == paragraphs[i - 1]:
            paragraphs[i - 1].string += paragraphs[i].string
            paragraphs[i].decompose()

    return str(soup)

# Gọi hàm để ghép các thẻ <p> liền kề
result_html = merge_adjacent_paragraphs(html_content)

# In ra kết quả
print(result_html)
