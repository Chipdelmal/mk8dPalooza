
from os import path
import pandas as pd
import plotly.express as px
import constant as cst
import functions as fun

(PT_DTA, PT_PLT, FN_RSP) = (cst.PT_DTA, cst.PT_PLT, cst.FN_RSP)
(PLYRS, TRK_SET) = (cst.PLYRS, set(cst.TRACKS))
###############################################################################
# Read data and get constants
###############################################################################
VOTES_RS = pd.read_csv(path.join(PT_DTA, FN_RSP), index_col=False)
###############################################################################
# Plot treemap
###############################################################################
print('(8) Plotting TreeMap')
colDict = {i: PLYRS[i]['color']+cst.ALPHA_HEX for i in PLYRS}
colDict['(?)']='EAEAEA'
fig = px.treemap(
    VOTES_RS, path=['Track', 'Name'], values='Votes',
    color='Name', color_discrete_map=colDict
)
# fig.show()
fig.write_html(path.join(PT_PLT, 'treemap.html'))