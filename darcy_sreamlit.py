# -*- coding: utf-8 -*-

import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
sns.set_style('whitegrid', {'grid.linestyle': u'--'})

from pathlib import Path

'''This is a streamlit webapp to demonstrate the properties, capabilities and limits of the Darcy flow model.
'''

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

def sat_hydraulic_flow(K, L, dH):
    '''Darcy saturated hydraulic flow
    q = K · i/L
    Inputs
    K :: hydraulic conductivity (saturated) (m/s)
    L :: length of porous medium (m)
    dH :: hydraulic pressure gradient (m_H2O)

    Output
    q :: flux in system (m/s)
    '''
    q = K * dH / L
    return q

def d_simple():
    Ke = st.sidebar.slider('Sat. hydraulic conductivity exponent (m/s):', min_value=-10., max_value=-2., value=-4.3, key='Ks')
    st.sidebar.markdown('K = '+str(1.2*10**Ke),unsafe_allow_html=True)
    Ks = 1.2*10**Ke
    dH = st.sidebar.slider('Hydraulic pressure gradient (m):', min_value=0., max_value=15., value=2.,key='dH')
    L  = st.sidebar.slider('Length of system (m):', min_value=0., max_value=15., value=2., key='L')

    q = sat_hydraulic_flow(Ks, L, dH)
    st.write('q = '+str(np.round(q,8))+'m/s')
    return


st.title('Darcy Flow')

darcysketch = './schwartzendruber.png'
st.sidebar.image(darcysketch, caption='', use_column_width=True)

st.sidebar.header('Control Panel')

topics = ['simple', 'non-static', 'non-homogeneous']
navi_sec = st.sidebar.selectbox('Select Topic:', topics)

if navi_sec=='simple':
    st.header('Original simple Darcy')
    st.markdown(read_markdown_file('./sdarcy_md.md'), unsafe_allow_html=True)
    d_simple()
elif navi_sec=='non-static':
    st.header('Non-static conditions Darcy')
    st.markdown('''This is simply a dummy.''',unsafe_allow_html=True)
elif navi_sec=='non-homogeneous':
    st.header('Non-homogeneous conditions Darcy')
    st.markdown('''This is simply a dummy.''',unsafe_allow_html=True)



