#!/usr/bin/env python
# coding: utf-8

# # The biodiversity crisis

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


# 
# ## A general decline
# 
# There is a global consensus that global biodiversity and ecosystem health are under serious threat. Rapid declines have been registered across nearly all major indices of ecoysystem health and biodiversity, with around 25% of species threatened with extinction across the Animal, Plant and Fungi Kingdoms {cite}`ipbes_2019`. Data overwhelming points to long term and irreversible declines in biodiversity with the term sixth mass extinction being commonly evoked to describe the ongoing phenomenon {cite}`sixth_extinction`. The following quotation from a special issue of the Proceedings of the Academy of Natural Sciences dedicated to the decline in insects sums up the situation in stark terms`decline_anthroposcene`:
# 
# >Even without much-needed monitoring and demographic data, enough is already known, based on first principles and records for amphibians, birds, flowering plants, mammals, reptiles, insects, and other taxa, to understand that a biodiversity crisis is accelerating as the planet’s human population grows, increasingly exacerbated by unprecedented recent climate changes and other anthropogenic stressors. Time is not on our side, and urgent action is needed on behalf of nature.
# 
# Insect populations in particular are undergoing a significant decline. The data available for Europe points strongly in a negative direction, exemplified by a 2017 study that identified a 75% decline between 1989 and 2017 in flying insect mass in nature reserves in Southern Germany {cite}`insect_loss_DE`. Data from the UK and the Netherlands showed a decline of the same magnitude: both registered a drop of 50% since 1976 and and 1990 respectively, which itself comes after a drop in population on the order of 80% in the Netherlands in the period 1880 - 1940 {cite}`butterflies_europe`. Switzerland has not escaped the pan European decline in insect populations and diversity; researchers are clear that significant steps need to be taken immediately to reverse these trends. Of the 226 butterfly and moth species monitored nationally (out of some 3700 lepidoptera species confirmed in Switzerland), just over 50% are considered to be under threat or potentially under threat.  Most of this loss is occurring due to insecticides, ever increasing intensification of agriculture, and continued artificialisation of land for residential, agricultural or commercial purposes {cite}`insect_loss_ch`.
# 
# ## Switzerland and the Central Plateau
# 
# More than a quarter of Swiss vascular plants are under threat with "thousands of local extinctions" of sensitive and endangered species. As the researchers who identified these local extinctions put it {cite}`ch_localextinct`:
# 
# > Our study presents clear evidence that current efforts to conserve threatened plant species are insufficient to achieve national and international targets (Convention on Biological Diversity (CBD), 2011; Swiss Biodiversity Strategy 2012) for maintaining biodiversity. The current paradigm of protecting and restoring threatened habitats is failing to avert extinctions. Going forward, we need to develop a comprehensive landscape approach, involving the creation of ecological infrastructure and translocation and assisted migration of threatened species into suitable habitats.
# 
# These localized extinctions are most prominent in Switzerland's Central Plateau region, where 60% of the vascular plant species evaluated for the International Union of the Conservation of Nature's Red List are classified as potentially or actually regionally threatened. The Jura region follows with 50% of evaluated species for the Jura classified as potentially or actually regionally threatened {cite}`red_list`. As Biel lies on the border between two regions, the city and its inhabitants have both a special oportunity and obligation to act to preserve the local flora surrounding the city.
# 
# ## Smart conservation
# 
# A judicious use of public spaces, such as road verges, railroad berms and parks, that balances their potential as habitats with the needs and requirements of the city's inhabitants, is one step cities can take to mitigate some of the anthropologic pressure. Allowing spaces to go un-mowed, sowing native wild-flower beds, and creating micro-habitats strategically throughout urban and suburban areas can provide measurable benefits to both herbaceous and predatory insects {cite}`urban_arthropod_ch`. In fact, (sub)urban green spaces and road verges can provide plants, insects and birds with suitable conditions to pursue their life cycles and even become a "last refuge" for certain species (ibid). 
# 
# At the same time, it is important to consider the effectiveness of the actions being taken by local authorities. It is well known that severely worked plantations of annual wildflower meadows provide only a fraction of the habitat and food resources of perennial meadows, which themselves do not provide resources as continuously throughout the year as the remnant weed populations. (CITE). In fact, the widespread use of commercially grown "wildflowers" has the potential to have severely negative impacts on the already fragile genetic diversity of fragmented and shrinking wild populations. As one study of 3 relatively common wildflowers in Switzerland put it, "The results suggest that only plants of relatively local origin should be used in wildflower mixtures, although it is not possible to specify precisely over what distance seed can safely be transferred. The same recommendation is also valid for schemes to reinvigorate endangered plant populations {cite}`Keller et al. 2000`." The specific obligations of producers of regional seed types are the following`Czarnecki et al. 2008`:
# 
# > Growers of regional seed types must ensure that populations are adequately sampled so as to accurately represent the genetic diversity of the original population(s). Growers must then produce seeds that are of high quality and preserve the level and composition of genetic diversity of the original, naturally occurring population (Rogers, 2004). Inadequate sampling (narrowly based genetic collection), production practices, or inappropriate distribution or use of seeds could cause loss of genetic diversity, disruption of the natural distribution of genetic diversity, and inbreeding or outbreeding depression. 
# 
# ## The market gap
# 
# An undeniable conclusion is that urgent action needs to be taken to preserve the biodiversity of the Central Plateau and the Jura regions and that regionally sourced seeds must be used in the repopulation of our urban, suburban and rural spaces with native plants. As conversations and sectoral research has made clear, it is difficult, if not impossible, to find most varieties of native wildlfowers in sufficient quantitie and of reliable enough quality for use in personal gardens, let alone for even small to medium scale renaturalization projects. The germination and propogation of wildflower seeds is notoriously difficult and as a result only a few well known species that lend themselves to typical greenhouse propogation become represented in the wildflower gardens of well intentioned citizens or in the renaturalization projects of governmental authorities. This is the problem that this report will focus on solving.

# In[ ]:




