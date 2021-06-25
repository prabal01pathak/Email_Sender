import os
import requests
from bs4 import BeautifulSoup
from email.message import EmailMessage
import smtplib
import lxml
url = 'http://www.coreyms.com'
def html_parser(url):
    r = requests.get(url)
    html = BeautifulSoup(r.text,'lxml')
    links = []
    for article in html.find_all('article'):
        vid_pl = article.find('iframe',class_ = 'youtube-player')
        if vid_pl != None:
            vid_pl = vid_pl['src']
            vid_id = vid_pl.split('/')
            vid_fid = vid_id[4].split('?')[0]
            yt_link = f'https://youtube.com/watch?v={vid_fid}'
            links.append(yt_link)
        else:
            continue
    return links

def send_mail():
    msg = EmailMessage()
    msg['Subject'] = 'These are links of coreyms programming videos.'
    msg['To'] = os.getenv('REC_EMAIL')
    msg['From'] = os.getenv('EMAIL_ADDRESS')
    video_links = f'{html_parser(url)}'
    msg.set_content(video_links)
    print(msg)

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as mail:
        mail.login(os.getenv('EMAIL_ADDRESS'),os.getenv('EMAIL_PASS'))
        mail.send_message(msg)
        print('done')

def photo_downloader(url):
    request = requests.get(url,allow_redirects = True)
    data = BeautifulSoup(request.text,'lxml')
    all_image=data.find_all('figure',itemprop="image")
    count =20 
    os.chdir('..\\pictures')
    for i in all_image:
        url=i.find('a',rel="nofollow")
        if url != None:
            i_url = url['href']
            photo_bytes = requests.get(i_url,allow_redirects=True)
            with open(f'{count}programming.jpg','wb') as photo:
                photo.write(photo_bytes.content)
                print(count)
                count +=1
                
    print("Done")
        
        

if __name__ == "__main__":
    photo_downloader("https://unsplash.com/s/photos/programming")
