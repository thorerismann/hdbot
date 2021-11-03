#!/usr/bin/env python
# coding: utf-8

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


# # Floral Buckets - summary

# In[2]:


this_picture = PILImage.open("resources/pictures/2021/DSC09846.JPG")
output = io.BytesIO()
this_picture.thumbnail((800, 1200))
this_picture.save(output, format='PNG')
encoded_string = base64.b64encode(output.getvalue()).decode()

html = '<img src="data:image/png;base64,{}"/>'.format(encoded_string)
md(html)


# ## Market for Regional Seeds
# 
# If regional biodiversity is to be preserved effectively, then the market for local ecotype wildflowers is only going to expand. In terms of provision of seeds and seedlings, there is significant interest among private individuals in using local wildflowers to create natural gardens that provide habitat and food resources to the larger ecosystem. Public authorities are continuously engaged in renaturalization projects that need local seeds and seedlings to be maximaly effective at preserving regional biodiversity. Even municipal authorities engaged in providing wildflower strips alongside roadways and as part of public greenspaces should be using regional type seeds.
# 
# Indeed, there are a number of companies offering to cut flowering meadows, dry the seed and offer sacks of wildflower mixes. In general, they do not offer individual spieces either as seedlings or as seed packets - they offer slightly different prairie mixes with more or less the same standard composition. This means that, for example, early blooming forest flowers like anemone nemorosa and A. hepatica are simply not offered by anyone. In general, there are about 50-60 species that can be more or less regionally sourced from different actors.
# 
# In comparison to the number of flowering plants found regionally, the selection on offer is relatively restricted. 
# sa
# ### Biodiversity boxes
# 
# Traditional horticultural settings do not provide the floral resources 
# 
# ### Seeds and Seedlings
# 
# 
# ### Local competition
# 
# There are numerous horticulturalists, florists, and landscapers offering horticultural products similar to the naive consumer. Key points to be detailed
# 
# * Big box stores are just starting to move into the wildflower market
# * No other local source for actual wild flowers
# * Number of landscapers, florists, horticulturalists. 

# ## Revenue Streams
# 
# The primary revenue stream is projected to originate from monthly subscriptions for wildflowers grown from local seeds. Secondary revenue streams that build off of the knowledge and the production process are also important to consider and may end up being larger than the wildflower buckets, especially at the beginning.
# 
# 1. Flower bucket subscription
# 2. Biotope subscription
# 3. Flower bucket / biotope rental for events
# 4. Guided tours to unique biotopes for seed collection for regional ecotourism (via VHS?)
# 5. Sale of seeds / "seed bombs"
# 6. Sale of individual plants as well as flower bucket subscriptions at city markets
# 7. Sale of cut flowers
# 8. Contracts with municipal and regional authorities
# 9. Subsidies
# 

# ### Flower bucket subscription
# 
# The core of the value proposition is the following:
# > Buckets of wildflowers grown from locally collected seed that look great year round while protecting the unique flora and fauna of the region. Grown in a certified organic horticultural center with seeds collected sustainably, and managed to provide resources and habitat for native insects.
# 
# A back of the envelope calculation yields the following:
# 

# ### Biotope subscription
# 
# Production of larger, custom creations based on unique and threatened local biotopes.

# ### Guided tours
# 
# Offer guided tours of where seeds are collected. A "balade botanique" costs 40 CHF from the VHS Biel-Lyss

# ### Sale of seeds
# Wildflower seed mixes could be sold as well. There are no other seed mixes originating from wild-type flowers available.
# * Past equipe volo experience
# * number of wild branded seed mixes available from the chains stores.

# ### Sale of individual plants
# The sale of invididual plants currently occurs only at Equipe Volo essentially through an existing network with little effort made to find additional customers. 
# * The most effective way to increase the sale of plant stock is to participate in the sale of individual plants at markets. This would also be a chance to sell bucket subscriptions.

# ### Sale of cut flowers.
# A certain amount of cut flowers will be generated through the maintenance and production process, as well as by undelivered inventory. Could these be sold at markets etc as well ?

# ### Contracts with municipal and regional authorities
# There is a growing awareness within local, regional and national governments of the importance of using wild flowers, and even more so using wild-type seeds. A main constraint they face is the lack of wild-type plants available for renaturalization projects, city beautification projects, and the rest.
# 
# Education and engagement with these authorities could yield significant revenu streams.
# 
# As discussed with the M. from the city, and demonstrated by Uni Zurich contract.

# ### Subsidies
# Due to the high environmental and scientific contributions that can be made, there is a strong possibility for government subsidies to pay for some of the diffuse benefits that are generated by the project but not captured sufficiently in the revenu stream.

# ### Event rentals
# 
# Rent out beautiful natural wildflower displays for weddings and other events.

# In[ ]:





# ## IT system
# 
# In order to operate and scale effectively a strong IT system will be needed for the following:
# * Manage inventory
# * Manage plant data
# * Use and the present the data
# * Electronic delivery of all things.

# ### Inventory management
# 
# Both wildflower buckets and biotopes will need to be swapped and/or maintained throughout the year, thus it is critical to have a strong system of information management. As it takes time to produce the flowers in a way that respects the environment, information management is key to not exceed inventory capacity nor end up purchasing flowers to maintain contractual obligations. . Maintaining an electronic database will be a critical part of managing fixed and variable costs.
# * The expected state of the different buckets and biotopes needs to be tracked in order for the to be maintained and swapped 
# * Construct and optimize a city level maintenance schedule for the buckets and biotopes.
# * Digitize information regarding inventory management from seedling to sale of flower bucket.

# ### Data management
# 
# The data produced during the production process should be effectively captured, stored and put to use. Further, the trips out to the field to collect seeds can double as data collection opportunities.
# * Plant surveys of the areas where seeds are being collected should be conducted and stored using the infoflora app, a supremely useful and useable tool for keeping track of plant surveys in Switzerland. Survey data is easily exportable for other uses while being immediately registered for the national database.
# * Data should be kept on the successes and failures of growing wild-type wildflowers commercially as there is relatively little information on effective propoagation of many of these species. TBD
# * Database to register data for other scientific work (genetic work)

# ### Use and presentation of data
# For data to have value it must be both useable and be put to use. In order for this to happen, it must be maintained, stored and updated, as well as have a human available to collaborate with researchers and others interested in the topic. In addition, prioritization of taking plant data and promoting species 
# * Integration with other local and regional databases to provide the context of where the flora products fit into the flora of the built environment (e.g. cadastre des arbres de bienne, info flora observations, 2020, 2021 survey data) 
# * Basic analytics should be automatically generated for funding, management, communication and reporting
# * Use of industry standard coding platforms to facilitate integration with emerging knowledge and nature-based solutions econmy

# ## Scientific integration
# In order for the next generation of sustainable businesses oriented firmly in a nature based solutions economy to succeed, it must be embedded on the frontier of relevant scientific developments. 
# * Genetic analysis becomes more accessible  just as the importance of preserving genetic diversity is being recognized a serious topic.
# * Strong connection to (sub)urban plant surveys and local biogeographic knowledge
# * Development of a "living seedbank"
# 

# ### Genetic analysis
# Genetic analysis becomes more accessible just as the importance of preserving genetic diversity is being recognized as a serious topic.
# * Possibility for environmental DNA analysis (50 - 100 CHF per sample for edna analysis?) on flower heads
# * Possibility to contribute to DNA barcoding of plant species
# * Comparison to commcercial "wildflower" seed mixes
# 

# ### Local biogeography
# The 
