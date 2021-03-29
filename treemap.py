
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
    color='Name', color_discrete_map=colDict,
    title='MK8D Palooza'
)
# fig.show()
fig.write_html(path.join(PT_PLT, 'treemap.html'))
###############################################################################
# Plot barchart
###############################################################################
print('(9) Plotting BarChart')
colDict = {i: PLYRS[i]['color'] for i in PLYRS}
fig = px.bar(VOTES_RS, 
    x="Track", y="Votes", color="Name", title="MK8D Palooza",
    color_discrete_map=colDict
)
# fig.update_layout(barmode='stack', xaxis={'categoryorder':'total ascending'})
# fig.show()
fig.write_html(path.join(PT_PLT, 'barchart.html'))