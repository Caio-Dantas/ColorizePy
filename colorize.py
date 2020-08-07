from dotenv import load_dotenv
load_dotenv()

import os
ALGORITHMIA_KEY = os.getenv('ALGORITHMIA_KEY')

import Algorithmia

from PIL import Image
import io

client = Algorithmia.client(ALGORITHMIA_KEY)

#imageLink =  "https://s3.amazonaws.com/algorithmia-assets/algo_desc_images/deeplearning_ColorfulImageColorization/lincoln.jpg"
imageLink = raw_input("Coloque o link da imagem: ")

input = {
  "image": imageLink
}
client = Algorithmia.client('sim9c4JI+TAoneoABRzubCdNAIN1')
algo = client.algo('deeplearning/ColorfulImageColorization/1.1.14')
print("Loading...")
algo.set_options(timeout=300) # optional
foto =algo.pipe(input).result 

# Download file and get the file handle
exampleFile = client.file(foto.get("output")).getBytes()

#Opens the result file.
image_data = exampleFile
image = Image.open(io.BytesIO(image_data))
image.show()