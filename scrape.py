import requests
import time
import random
from tqdm import tqdm


def main():
   xkcd_ids = range(100,2001)

   for n in tqdm(xkcd_ids):
      response = requests.get(f'https://xkcd.com/{n}')
      with open(f'data/{n}.html','w') as f:
         f.write(response.text)
      time.sleep(random.randrange(0,5))

if __name__ == '__main__':
   main()
