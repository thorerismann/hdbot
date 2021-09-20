#!/usr/bin/env python
# coding: utf-8

# # the threat to our plants and insects

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


this_picture = PILImage.open("resources/pictures/2021/DSC06816.JPG")
output = io.BytesIO()
this_picture.thumbnail((800, 1200))
this_picture.save(output, format='PNG')
encoded_string = base64.b64encode(output.getvalue()).decode()

html = '<img src="data:image/png;base64,{}"/>'.format(encoded_string)
md(html)


# ## Abstract

# ## Global Context
# Globally, the health of the natural world is at serious risk due to human activities, or as put by the Intergovernmental Science-Policy Platform on Biodiversity and Ecosystem Services (IPBES), "Nature across most of the globe has now been significantly altered by multiple human drivers, with the great majority of indicators of ecosystems and biodiversity showing rapid decline." {cite}`ipbes_2019` Extinction rates are high and on the rise, especially among species dependent on ecological niches that have experienced significant decline, such as wetland habitats and wildflower meadows. The current rate of extinction globally is estimated to be around 10X - 100X higher than the background extinction rate, and is often characterized by extinction without replacement, which further leads to the loss of integrity of ecological systems. In addition to extinctions, we see the rarefaction of formerly common species and a general decline in the total mass of wild mammals, birds and insects. An example of this which prompted serious reflection among scientists, civil society and governments is a 2017 paper which identified a 75% decline between 1989 and 2017 in flying insect mass in nature reserves in Southern Germany. Where long term data on insect populations is available, all evidence points to a long term decline across Europe with an estimated 10% of pollinator species being considered threatened with extinction. Europe's flora faces similar challenges: half of the continents endemic tree species are threatened.
# <p>&nbsp;</p>
# While national actors work to set standards and engage in international negotiations to protect biodiversity and ecosystem health on a global scale, local public and private actors have significant room to maneuver. It is well known that one way to mitigate some of the anthropologic pressure is a judicious use of public spaces, such as road verges, railroad berms and parks, that balances their potential as habitats with the needs and requirements of the city's inhabitants. Allowing spaces to go un-mowed, sowing flower beds, and creating micro-habitats strategically throughout urban and suburban areas are small, relatively cost-neutral steps that can have marginal but important impacts. In fact, studies have shown that (sub)urban green spaces and road verges can provide plants, insects and birds with suitable conditions to pursue their life cycles and even become a "last refuge" for certain species.
# <p>&nbsp;</p>
# At the same time, it is important to consider the effectiveness of the actions being taken by local authorities. Annual flower meadows for pollinators are an increasingly common sight in different countries, yet provide only a fraction of the resources of perennial meadows, which themselves do not provide resources as continuously throughout the year as remnant weed populations. There are many factors to consider, and unraveling the complex web of ecosystem interdependence remains on the frontier of science. Beyond the ecological questions, there is also the question of genetic diversity. A significant part of biodiversity that had been overlooked until relatively recently, genetic diversity is required for the long term health and success of populations. This project will not address these questions directly, but will build the knowledge to begin addressing them during the second iteration. 

# ## Swiss Context Plants
# 
# In Switzerland, more than a quarter of Swiss vascular plants are under threat with "thousands of local extinctions" of sensitive and endangered species. These localized extinctions are most prominent in Switzerland's Central Plateau region. This is partially due to the unique bio-geography of this region and partially due to the intense human pressures on the Central Plateau, home to most of Switzerland's agricultural output and where 70% of the population lives and works. 60% of the vascular plant species evaluated for the International Union of the Conservation of Nature's Redlist are classified as potentially or actually regionally threatened in the Central Plateau, followed by 50% of evaluated species for the Jura. As Biel lies on the border between two regions, the city has an opportunity and a responsibility to act.
# <p>&nbsp;</p>
# As the researchers who identified these local extinctions put it :
# > Our study presents clear evidence that current efforts
# to conserve threatened plant species are insufficient to
# achieve national and international targets (Convention
# on Biological Diversity (CBD), 2011; Swiss Biodiversity
# Strategy 2012) for maintaining biodiversity. The current
# paradigm of protecting and restoring threatened habitats
# is failing to avert extinctions. Going forward, we need to
# develop a comprehensive landscape approach, involving
# the creation of ecological infrastructure and translocation
# and assisted migration of threatened species into suitable
# habitats.
# 
# Similarly, the situation for insects and especially pollinators, often taken as key biological indicators, is extremely worrying. Of the 226 butterfly and moth species monitored nationally (out of some 3700 lepidotpera species confirmed in Switzerland), just over 50% are considered to be under threat or potentially under threat.  Switzerland has not escaped the pan European decline in insect populations and diversity and researchers are clear that significant steps need to be taken immediately to reverse these trends. Most of this loss is occurring due to insecticides, ever increasing intensification of agriculture, and continued artificialisation of land for residential, agricultural or commercial purposes.

# In[ ]:





# ## Swiss Context Insects

# ## Biel Context Plants

# ## Biel Context Insects
