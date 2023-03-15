#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
from PIL import Image


st.title('Tableau Graphs')
st.write("""Here it would be found all the graphs related with the analysis done, which includes averages of subjetivity and polarity, also the max and min value of them,
the amount of articles published by agency, and also by topic, to finish analysing the top 50 words overall and by blocs( western and eastern)""")

def main():
    html_temp = """<div class='tableauPlaceholder' id='viz1678892045277' style='position: relative'>
                    <noscript>
                    <a href='#'><img alt='The geopolitical influence on the press ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ge&#47;geopoliticalpress&#47;Journalism&#47;1_rss.png' style='border: none' />
                    </a>
                    </noscript>
                    <object class='tableauViz'  style='display:none;'>
                    <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
                    <param name='embed_code_version' value='3' /> 
                    <param name='site_root' value='' />
                    <param name='name' value='geopoliticalpress&#47;Journalism' />
                    <param name='tabs' value='no' />
                    <param name='toolbar' value='yes' />
                    <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ge&#47;geopoliticalpress&#47;Journalism&#47;1.png' /> 
                    <param name='animate_transition' value='yes' />
                    <param name='display_static_image' value='yes' />
                    <param name='display_spinner' value='yes' />
                    <param name='display_overlay' value='yes' />
                    <param name='display_count' value='yes' />
                    <param name='language' value='en-GB' />
                    <param name='filter' value='publish=yes' />
                    </object>
                    </div>
                    <script type='text/javascript'>
                    var divElement = document.getElementById('viz1678892045277'); var vizElement = divElement.getElementsByTagName('object')[0]; vizElement.style.width='1016px';vizElement.style.height='991px'; var scriptElement = document.createElement('script'); scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js'; vizElement.parentNode.insertBefore(scriptElement, vizElement);
                    </script>"""
    st.components.v1.html(html_temp, width=2800, height=2400, scrolling=True)
if __name__ == "__main__":    
    main()