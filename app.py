import streamlit as st

st.title('Leo Messi')

col1,col2=st.columns(2)

with col1:
    st.image('messi2.jpg')

with col2:
    st.write('''
    Messi relocated to Spain from Argentina aged 13 to join Barcelona, for whom he made his competitive debut aged 17 in October 2004. He established himself as an integral player for the club within the next three years, and in his first uninterrupted season in 2008–09 he helped Barcelona achieve the first treble in Spanish football; that year, aged 22, Messi won his first Ballon d'Or. Three successful seasons followed, with Messi winning four consecutive Ballons d'Or, making him the first player to win the award four times. During the 2011–12 season, he set the La Liga and European records for most goals scored in a single season, while establishing himself as Barcelona's all-time top scorer. The following two seasons, Messi finished second for the Ballon d'Or behind Cristiano Ronaldo (his perceived career rival), before regaining his best form during the 2014–15 campaign, becoming the all-time top scorer in La Liga and leading Barcelona to a historic second treble, after which he was awarded a fifth Ballon d'Or in 2015. Messi assumed captaincy of Barcelona in 2018, and won a record sixth Ballon d'Or in 2019. Out of contract, he signed for Paris Saint-Germain in August 2021.
    ''')

st.header('Courses Offered')
st.subheader('Data Science and Machine Learning')
st.subheader('Data Analysis')
st.subheader('Python')
st.subheader('SQL')
st.subheader('DSA')

st.sidebar.title('Menu')
st.sidebar.markdown('''
- Home
- About 
- Contact
''')