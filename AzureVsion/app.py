from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import sys
import time
import streamlit as st

#cognitiveVisionとの接続
os.environ["AZURE_COGNITIVE_SERVICES_SUBSCRIPTION_KEY"] = "6edf6aa63e3046c7a727a8d1267223cc"
os.environ["AZURE_COGNITIVE_SERVICES_ENDPOINT"] = "https://udemy20240506.cognitiveservices.azure.com/"

subscription_key = os.environ["AZURE_COGNITIVE_SERVICES_SUBSCRIPTION_KEY"]
endpoint = os.environ["AZURE_COGNITIVE_SERVICES_ENDPOINT"]

#認証
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

#画像認識メソッド
def get_tags(filepath):
    local_image = open(filepath, "rb")
    
    tags_result = computervision_client.tag_image_in_stream(local_image)
    
    tags=tags_result.tags
    
    tags_name = []
    for tag in tags:
        tags_name.append(tag.name)
    return tags_name

def detect_objects(filepath):
    
    local_image = open(filepath, "rb")
    
    detect_objects_results=computervision_client.detect_objects_in_stream(local_image)
    objects =detect_objects_results.objects
    return objects

#streamlit
st.title('物体検出アプリ')

uploaded_file =st.file_uploader('Chooose an image',type=['jpg','png'])#パスを直接取得できないことに注意
if uploaded_file is not None:
     img = Image.open(uploaded_file)
     img_path = f'img_{uploaded_file.name}'#アップロードしたファイルの名前を取得している
     img.save(img_path)#一旦保存したファイルパスを別途読み込んでいる
     objects = detect_objects(img_path)
     
     #描画
     draw = ImageDraw.Draw(img)
     for object in objects:
            x = object.rectangle.x
            y = object.rectangle.y
            w = object.rectangle.w
            h = object.rectangle.h
            caption =object.object_property
            
            font =ImageFont.truetype(font = './Helvetica 400.ttf', size=50)
            # テキストのバウンディングボックスを取得
            bbox = draw.textbbox((0, 0), caption, font=font)

            # テキストサイズの計算
            text_w = bbox[2] - bbox[0]
            text_h = bbox[3] - bbox[1]

            draw.rectangle([(x,y),(x+w,y+h)],fill =None,outline='green',width=5)
            draw.rectangle([(x,y),(x+text_w,y+text_h)],fill ='green',outline='green',width=5)
            draw.text((x,y),caption,fill ='white',font=font)

     st.image(img)
     
     tags_name =get_tags(img_path)
     print(', '.join(tags_name))
     
     st.markdown('**認識されたコンテンツタグ**')
     st.markdown(f'> {tags_name}')

