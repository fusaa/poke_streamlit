import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import requests

st.set_page_config( layout='wide')



def get_details(poke_number):
    try:
        url = f'https://pokeapi.co/api/v2/pokemon/{poke_number}'
        response = requests.get(url)
        pokemon = response.json()
        return pokemon['name'], pokemon['height'], pokemon['weight'], len(pokemon['moves']), pokemon['sprites'], pokemon['cries']['latest']
    except:
        return 'Error', np.NAN, np.NAN, np.NAN, np.NAN, np.NAN


st.title("Poke Stats")
pokemon_number = st.slider("Use the Slider to pick a Pokemon", 
                           min_value = 1, 
                           max_value=150)



name, height, weight, moves, sprites, cry = get_details(pokemon_number)

height = height * 10

height_data = pd.DataFrame({'Pokemon': ['Weedle', name, 'victreebel'],
                            'Heights': [30, height, 170]})

colors = ['gray', 'red', 'gray']

graph = sns.barplot(data = height_data,
                    x= 'Pokemon',
                    y='Heights',
                    palette = colors)







col1, col2, col3 = st.columns([7,5,4])

if 'latest_seen' not in st.session_state:
    st.session_state['latest_seen'] = [name]
    st.session_state['height'] = [height]
    
else:
    st.session_state['latest_seen'].append(name)
    st.session_state['height'].append(height)
    
    





with col1:
   st.header("Recent Checked Pokes")
   col100, col200 = st.columns([1,1])
   with col100:
       st.write("Name")
       for i in st.session_state['latest_seen']:
           st.markdown("- " + i.title())
   with col200:
       st.write("Tallest so far")
       
       sorted_latest_and_height = sorted(zip(st.session_state['latest_seen'], st.session_state['height']), key=lambda x: x[1], reverse=True)

       for i,j in sorted_latest_and_height:
           st.markdown("- " + i.title() + " - " + str(j))
   

with col2:
    st.pyplot(graph.figure)

with col3:
   st.header(name.title())
   col10, col20 = st.columns([1,1])
   with col10:
       st.image(sprites['other']['home']['front_default'], use_column_width = 'always')
   with col20:
       st.write(f'Height:{height}')
       st.write(f'Weight:{weight}')
       st.write(f'Moves:{moves}')

   st.audio(cry, format='audio/ogg')

st.header("Poke Variations:")

colA, colB, colC, colD, colE, colF, colG, colH = st.columns([1,1,1,1,1,1,1,1])
with colA:
    st.image(sprites['versions']['generation-i']['red-blue']['front_default'], use_column_width = 'always')
with colB:
    st.image(sprites['versions']['generation-ii']['gold']['front_default'], use_column_width = 'always')
with colC:
    st.image(sprites['versions']['generation-iii']['emerald']['front_default'], use_column_width = 'always')
with colD:
    st.image(sprites['versions']['generation-iv']['heartgold-soulsilver']['front_default'], use_column_width = 'always')
with colE:
    st.image(sprites['versions']['generation-v']['black-white']['front_default'], use_column_width = 'always')
with colF:
    st.image(sprites['versions']['generation-vi']['omegaruby-alphasapphire']['front_default'], use_column_width = 'always')
with colG:
    st.image(sprites['versions']['generation-vii']['ultra-sun-ultra-moon']['front_default'], use_column_width = 'always')
with colH:
    st.image(sprites['versions']['generation-viii']['icons']['front_default'], use_column_width = 'always')
