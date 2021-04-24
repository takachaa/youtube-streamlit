import streamlit as st
# import numpy as np 
# import pandas as pd 
# from PIL import Image
import time


st.title('Sterwamlit 超入門')

st.write('pregress bar show')
'start'


    
latest_iteratino = st.empty()
bar = st.progress(0)

for i in range(100):
    time.sleep(0.1)
    bar.progress(i + 1)


left_column, right_column = st.beta_columns(2)
te =  left_column.button('ボタンを押してくｄさくあ')
if te:
    right_column.write('ボタンを押されました')


expander1 = st.beta_expander('quesion')
expander1.write('ansewr')
expander1.write('ansewr')
expander1.write('ansewr')
expander1.write('ansewr')




# df = pd.DataFrame(
#     np.random.rand(100,2) / [50,50] + [35.69, 139.70],
#     columns=['lat','lon']
# )


# st.dataframe(df)

# st.write(df)
# st.table(df.style.highlight_max())
# st.dataframe(df.style.highlight_max(), width=300,height=300)


# """
# # 章
# ## 節
# ### 項

# ```python
# import pandas as pd 
# ```

# """
# st.line_chart(df)

# st.area_chart(df)

# st.bar_chart(df)

# st.map(df)

# if st.checkbox('saaa'):
#     img = Image.open('image.jpg')
#     st.image(img,caption='testsdsata', use_column_width=True)

#     st.video('sample.mp4', format='video/mp4', start_time=0)


# option = st.selectbox('色',list(range(1,11)))

# 'あなたの趣味は' , option


# text = st.text_input('あなたの趣味を教えてくさし')


# 'あなたの趣味は' , text

# slider = st.slider('あなたの調子は', 0, 100, 40)

# 'あなたの調子は' , slider



