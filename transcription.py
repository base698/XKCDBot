import os
from tqdm import tqdm
from bs4 import BeautifulSoup


def main():
   for item in tqdm(os.listdir('data')):
      if item.endswith('.html'):
         with open(os.path.join('data',item)) as f:
             html = f.read()
          
             soup = BeautifulSoup(html,"html.parser")
             el = soup.find("div",{"id":"transcript"})
             if el == None: continue
             transcript = el.get_text()
             transcript = transcript.strip()
             if len(transcript) == 0: continue

             transcript_path = os.path.join('transcription',f"{item.replace('.html','')}.txt")

             with open(transcript_path,'w') as tf:
                 tf.write(transcript)

if __name__ == '__main__':
    main()
