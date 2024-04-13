import streamlit as st
from PIL import Image
import time

st.set_page_config()


st.title('streamlit超入門')
st.write('プログレスバーの表示')
'Start!!'
latest_iteration =st.empty()#わかりやすさでこの変数名にするというだけ
bar =st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!'


left_column,right_column=st.columns(2)
button =left_column.button('右からむに文字を表示')
if button:
    right_column.write('ここは右カラム')


expander1 =st.expander('問い合わせ')#textinputと組み合わせつつ、ここの回答を作れれるはず
expander1.text_input('問い合わせ内容を書く')


# expander.write('問い合わせ内容を書く')
# expander.write('問い合わせ内容を書く')
# expander.write('問い合わせ内容を書く')


# text =option=st.text_input('あなたの趣味を教えてください')
# 'あなたの趣味：',text

# conditon=st.slider('あなたの今の調子は？',0,100,50)

# 'コンディション',conditon,'です'


# if st.checkbox('ShowImage'):#チェックがあるかどうかでtrue,falseの判定となる
#     img =Image.open('/Users/taikikida/Desktop/画像/IMG_7668.JPG')
#     st.write(img, caption='sample', use_column_width=True)



