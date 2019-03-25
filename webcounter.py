"""
Created on Sat Feb 23 23:41:51 2019
@author: annawu
"""

import re #import Regular Expression library
from nltk.corpus import stopwords #import tool stopwords 
import requests

"""
Function:
    function run() with 3 parameters: a link to webpage and two words w1 and w2.

Args: 
    return a set of all the words in the webpage that have a higher frequency than w1 but a lower frequency than w2. 
"""
def run(url,w1,w2):
    
    freq={}     
    
    stopLex=set(stopwords.words('english')) #build a set of english stopwords
    
    success=False
    
    for i in range(5): #try 5 times
        try:
            response=requests.get(url,headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'})
            success=True
            break
        except: 
            print ('failed attempt', i)
    
    if not success: return None
    
    text=response.text# read in the text from the file
 
    sentences=text.split('.') # split the text into sentences 
	
    for sentence in sentences: # for each sentence 

        sentence=sentence.lower().strip() # loewr case and strip	
        sentence=re.sub('[^a-z]',' ',sentence) # replace all non-letter characters  with a space
		
        words=sentence.split(' ') # split to get the words in the sentence 

        for word in words: # for each word in the sentence 
            if word=='' or word in stopLex:continue # ignore empty words and stopwords 
            else: freq[word]=freq.get(word,0)+1 # update the frequency of the word 
    
    # get the frequency count for each input word 
    freqw1=freq.get(w1)
    freqw2=freq.get(w2)
    
    # create a set for the words that have a frequency count beween input words
    wordsbetween=set()
    for a, b in freq.items():
        if b > freqw1 and  b < freqw2:
            wordsbetween.add(a)
   
    return wordsbetween
    
if __name__=='__main__':
    print(run('https://www.familysearch.org/service/records/storage/das-mem/patron/v2/TH-301-46453-209-10/dist.txt','years','home'))