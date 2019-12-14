# Cantonese NLP webapp

**Description**: Webapp taking an input in Chinese Cantonese and returning a sentiment with polarity. This application was built for a MBA project aiming at defining an innovative financial product.

**High level principle**: The web app takes an input in Cantonese, calls Azure Cogninitive Services to translate the input in English, then locally computes a polarity levering the textblob library and return the output to the frontend. 

**Author**: Romain Barraud

**Notes**:

 - run pip install -r requirements.txt to reproduce a similar environment.

 - Action needed adter installing textblob: run 
"python -m textblob.download_corpora"

  - Translation Key: Subscribe to Azure to get a free API key to make Cantonese translations

 - Endpoint for translations: https://westus.api.cognitive.microsoft.com/sts/v1.0

 - The webpage displays a QRcode for phone users to scan and access the page. The image needs to be regenerated in order to redirect to the web address of your webpage.
