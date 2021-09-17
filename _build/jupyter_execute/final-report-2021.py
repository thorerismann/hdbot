#!/usr/bin/env python
# coding: utf-8

# # The Flowers Around the City - A report on the flora of Biel/Bienne
# 
# The second year of surveying is coming to a close in mid-October and construction of the second year report will begin shortly. Check back for updates!

# In[1]:


# math and data packages
import pandas as pd
import numpy as np
import math

# charting and graphics
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.image as mpimg
from matplotlib import colors
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.dates as mdates
from matplotlib.gridspec import GridSpec

# os and file types
import os
import sys
import datetime as dt
import json
import csv

# images and display
import base64, io, IPython
from PIL import Image as PILImage
from IPython.display import Markdown as md
from IPython.display import display, Math, Latex


# In[2]:


this_picture = PILImage.open("resources/pictures/2021/DSC05650.JPG")
output = io.BytesIO()
this_picture.thumbnail((800, 1200))
this_picture.save(output, format='PNG')
encoded_string = base64.b64encode(output.getvalue()).decode()

html = '<img src="data:image/png;base64,{}"/>'.format(encoded_string)
md(html)


# ## Abstract
# 
# A number of plant surveys were conducted between March - October 2021 resulting in more than 4000 observations of herbeaceous plants, concentrated on public spaces in urban and suburban areas of Biel / Bienne. The results are TBD

# ## Background
# 
# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed dui imperdiet, eleifend enim ut, convallis velit. Praesent ornare lorem sit amet lobortis mollis. Morbi vitae commodo sapien. Nulla fermentum dui facilisis ex cursus, vel facilisis lacus venenatis. Cras luctus ante sit amet leo pulvinar, a accumsan velit elementum. Suspendisse ligula augue, sagittis in laoreet eu, molestie vitae nunc. Nam ornare tempus laoreet. Suspendisse aliquet, ligula dignissim vestibulum porta, ipsum ligula consectetur libero, ac condimentum orci erat id mauris. Phasellus id elit eget risus vestibulum egestas non sed mauris. In hac habitasse platea dictumst. Ut eget cursus metus, sit amet eleifend elit. Donec massa enim, rutrum in diam vel, tempor volutpat sapien. 

# ## Locations
# 
# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed dui imperdiet, eleifend enim ut, convallis velit. Praesent ornare lorem sit amet lobortis mollis. Morbi vitae commodo sapien. Nulla fermentum dui facilisis ex cursus, vel facilisis lacus venenatis. Cras luctus ante sit amet leo pulvinar, a accumsan velit elementum. Suspendisse ligula augue, sagittis in laoreet eu, molestie vitae nunc. Nam ornare tempus laoreet. Suspendisse aliquet, ligula dignissim vestibulum porta, ipsum ligula consectetur libero, ac condimentum orci erat id mauris. Phasellus id elit eget risus vestibulum egestas non sed mauris. In hac habitasse platea dictumst. Ut eget cursus metus, sit amet eleifend elit. Donec massa enim, rutrum in diam vel, tempor volutpat sapien. 

# ## Methodology
# 
# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed dui imperdiet, eleifend enim ut, convallis velit. Praesent ornare lorem sit amet lobortis mollis. Morbi vitae commodo sapien. Nulla fermentum dui facilisis ex cursus, vel facilisis lacus venenatis. Cras luctus ante sit amet leo pulvinar, a accumsan velit elementum. Suspendisse ligula augue, sagittis in laoreet eu, molestie vitae nunc. Nam ornare tempus laoreet. Suspendisse aliquet, ligula dignissim vestibulum porta, ipsum ligula consectetur libero, ac condimentum orci erat id mauris. Phasellus id elit eget risus vestibulum egestas non sed mauris. In hac habitasse platea dictumst. Ut eget cursus metus, sit amet eleifend elit. Donec massa enim, rutrum in diam vel, tempor volutpat sapien. surveys were conducted between March - October 2021 resulting in more than 4000 observations of herbeaceous plants, concentrated on public spaces in urban and suburban areas of Biel / Bienne. The results are TBD

# ## Results
# 
# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed dui imperdiet, eleifend enim ut, convallis velit. Praesent ornare lorem sit amet lobortis mollis. Morbi vitae commodo sapien. Nulla fermentum dui facilisis ex cursus, vel facilisis lacus venenatis. Cras luctus ante sit amet leo pulvinar, a accumsan velit elementum. Suspendisse ligula augue, sagittis in laoreet eu, molestie vitae nunc. Nam ornare tempus laoreet. Suspendisse aliquet, ligula dignissim vestibulum porta, ipsum ligula consectetur libero, ac condimentum orci erat id mauris. Phasellus id elit eget risus vestibulum egestas non sed mauris. In hac habitasse platea dictumst. Ut eget cursus metus, sit amet eleifend elit. Donec massa enim, rutrum in diam vel, tempor volutpat sapien. surveys were conducted between March - October 2021 resulting in more than 4000 observations of herbeaceous plants, concentrated on public spaces in urban and suburban areas of Biel / Bienne. The results are TBD

# ## Discussion
# 
# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed dui imperdiet, eleifend enim ut, convallis velit. Praesent ornare lorem sit amet lobortis mollis. Morbi vitae commodo sapien. Nulla fermentum dui facilisis ex cursus, vel facilisis lacus venenatis. Cras luctus ante sit amet leo pulvinar, a accumsan velit elementum. Suspendisse ligula augue, sagittis in laoreet eu, molestie vitae nunc. Nam ornare tempus laoreet. Suspendisse aliquet, ligula dignissim vestibulum porta, ipsum ligula consectetur libero, ac condimentum orci erat id mauris. Phasellus id elit eget risus vestibulum egestas non sed mauris. In hac habitasse platea dictumst. Ut eget cursus metus, sit amet eleifend elit. Donec massa enim, rutrum in diam vel, tempor volutpat sapien. surveys were conducted between March - October 2021 resulting in more than 4000 observations of herbeaceous plants, concentrated on public spaces in urban and suburban areas of Biel / Bienne. The results are TBD

# ## Conclusion
# 
# Survey again in 2022, but even better.

# In[ ]:




