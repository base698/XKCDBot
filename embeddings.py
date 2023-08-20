import os
import openai
import sys
import json
import time

from openai.embeddings_utils import cosine_similarity


openai.api_key = os.environ.get('OPENAI_KEY')

EMBEDDING_MODEL = "text-embedding-ada-002"

def get_embeddings(transcript_str):
    embeddings = openai.Embedding.create(
            model=EMBEDDING_MODEL,
            input=transcript_str
    )
    return embeddings


def main():
    for item in os.listdir('transcription'):
      if item.endswith('.txt'):
         with open(os.path.join('transcription',item)) as f:
             transcript = f.read()

             retry_count = 4
             next_count = 4
            
             while True:
                 try:
                     embed = get_embeddings(transcript)
                     embed_path = os.path.join('embeddings',f"{item.replace('.txt','')}.json")
                     with open(embed_path,'w') as f:
                        f.write(json.dumps(embed))
                 except Exception as e:
                     print(f'sleeping for {retry_count} err: {str(e)}')
                     time.sleep(retry_count)
                     retry_count += next_count
                     next_count = next_count * 2 
                     continue
                 break

if __name__ == '__main__':
   main()


