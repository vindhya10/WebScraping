import requests
from bs4 import BeautifulSoup
import csv
import re

# Function to filter out non-Telugu characters
def filter_telugu_text(text):
    telugu_pattern = re.compile('[\u0C00-\u0C7F]+')  # Telugu Unicode block
    telugu_text = ''.join(telugu_pattern.findall(text))
    return telugu_text

def scrape_blogspot(blog_url, output_csv):
    try:
        # Make a GET request to fetch the raw HTML content
        response = requests.get(blog_url)

        # Skip invalid links (e.g., 404 or 403 errors)
        if response.status_code != 200:
            print(f"Skipping {blog_url}: Invalid link (Status code: {response.status_code})")
            return

        response.encoding = 'utf-8'  # Ensure proper encoding to handle Telugu

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the title and the main content (adjust according to actual structure)
        title = soup.title.string if soup.title else 'No Title'
        content = ''

        # Adjust the tag for your blog content, here we're assuming it's within <div class="post-body">
        post_body = soup.find('div', class_='post-body')
        if post_body:
            # Get text and filter for Telugu characters only
            content = filter_telugu_text(post_body.get_text(separator=' ', strip=True))

        # If the content is not empty, write it to the CSV file
        if content.strip():  # Avoid writing empty content
            with open(output_csv, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([title, content])  # Writing the title and content

            print(f"Successfully scraped {blog_url}")
        else:
            print(f"Skipping {blog_url}: No Telugu content found")

    except Exception as e:
        print(f"Error while scraping {blog_url}: {e}")

# List of blog URLs
blog_urls = [
    "http://telugupadyam.blogspot.com/", "http://kotthachiguru.blogspot.com/", "http://dprathap.blogspot.com/",
    "http://amritaveena.wordpress.com/", "http://vadaami.blogspot.com/", "http://ramakasharma.blogspot.com/",
    "http://prasadgummadi.blogspot.com/", "http://cckrao2000.blogspot.com/", "http://battibandh.wordpress.com/",
    "http://padma-theinvincible.blogspot.com/", "http://joruga-husharuga.blogspot.com/", "http://nsaicharan.blogspot.com/",
    "http://drrams.wordpress.com/", "http://ubusu.blogspot.com/", "http://janamnaadi.blogspot.com/",
    "http://paraani.blogspot.com/", "http://ravindranadhg.blogspot.com/", "http://oosulu.blogspot.com/",
    "http://ourspiro.blogspot.com/", "http://rajivputtagunta.blogspot.com/", "http://ramasanthi.blogspot.com/",
    "http://gopalkoduri.wordpress.com/", "http://indianteluguassociation.blogspot.com/", "http://teluguerrors.blogspot.com/",
    "http://telugu-bhaktiganga.blogspot.com/", "http://oohalanni-oosulai.blogspot.com/", "http://yogihistory.blogspot.com/",
    "http://shankharavam.blogspot.com/", "http://poddu.net/", "http://farmeristheking.blogspot.com/",
    "http://aksharaarchana.blogspot.com/", "http://kalpanarentala.wordpress.com/", "http://chaduvu.wordpress.com/",
    "http://psravikiran.blogspot.com/", "http://sameekshaclub.wordpress.com/", "http://navatarangam.com/",
    "http://kesland.blogspot.com/", "http://tiyyanitenugu.wordpress.com/", "http://jeevanasutraalu.blogspot.com/",
    "http://nishigandha-poetry.blogspot.com/", "http://funcounterbyphani.blogspot.com/", "http://telugulomeemunduku.blogspot.com/",
    "http://puranalu.blogspot.com/", "http://drpvsnp.blogspot.com/", "http://raj-wanderingthoughts.blogspot.com/",
    "http://satya-writes.blogspot.com/", "http://www.janani.net.in/news/", "http://saiabhay2000.blogspot.com/",
    "http://spoorti7.blogspot.com/", "http://sathyagraahi.blogspot.com/", "http://dinnipati.wordpress.com/",
    "http://manimanasa.blogspot.com/", "http://teepigurutulu.blogspot.com/", "http://nava-vasantham.blogspot.com/",
    "http://ram-kv.blogspot.com/", "http://ushamuraliyam.blogspot.com/", "http://puretelugu.blogspot.com/",
    "http://ap2us.blogspot.com/", "http://happyday4every1.blogspot.com/", "http://telugubudugu.blogspot.com/",
    "http://chaitanyapaturu.blogspot.com/", "http://teluguvadini.blogspot.com/", "http://teluguwebchannel.blogspot.com/",
    "http://madhuvu.blogspot.com/", "http://naakathalu.blogspot.com/", "http://sridharchandupatla.blogspot.com/",
    "http://palaka-balapam.blogspot.com/", "http://telugutetalu.blogspot.com/", "http://for-what-iam-here.blogspot.com/",
    "http://veeresham.blogspot.com/", "http://nikosam.blogspot.com/", "http://ekantham.blogspot.com/",
    "http://telugu-cartoons.blogspot.com/", "http://iditelusa.blogspot.com/", "http://www.pranahita.org/",
    "http://suridu.blogspot.com/", "http://blaagu.com/chitralekha", "http://teluguman.blog.com/",
    "http://theuntoldhistory.blogspot.com/", "http://mavuduruvenugopal.blogspot.com/", "http://shashitarangam.blogspot.com/",
    "http://jarasodhichepparadhe.blogspot.com/", "http://scienceintelugu.blogspot.com/",
    "http://antulenialochanalu.wordpress.com/", "http://daadu91204.blogspot.com/", "http://punnami.blogspot.com/",
    "http://yamajala.blogspot.com/", "http://ulipikatte.blogspot.com/", "http://rangulakala.blogspot.com/",
    "http://gsashok.wordpress.com/", "http://indianshiva.blogspot.com/", "http://loguttu.blogspot.com/",
    "http://teluguwritings.blogspot.com/", "http://kondaveetisatyavati.wordpress.com/", "http://viraamam.blogspot.com/",
    "http://ashala-harivillu.blogspot.com/"
]

# Output file where data will be saved
output_csv = 'scraped_blogs_telugu.csv'

# Write headers to CSV file
with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Content'])

# Scrape each blog and save the results
for blog_url in blog_urls:
    scrape_blogspot(blog_url, output_csv)
