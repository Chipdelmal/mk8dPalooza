
import votes as vos
from scipy.spatial.distance import euclidean, cosine
import functions as fun


(PRINT_STATS, ANONYMIZE, WF_LEGEND) = (False, False, True)
###############################################################################
# Paths and Filenames
###############################################################################
(PT_DTA, PT_PLT) = ('./dta/', './plt/')
(FN_DTA, FN_RSP, FN_DST, FN_SCA) = (
    'votesDataframe.csv', 'votesReshape.csv',
    'distMatrix.csv', 'scaledMatrix.csv'
)
###############################################################################
# Distance matrix
###############################################################################
DIST_FUN = cosine
RANGE = (100, 10)

###############################################################################
# List of Valid Tracks
###############################################################################
TRACKS = [
    'Mario Kart Stadium', 'Water Park', 'Sweet Sweet Canyon', 'Thwomp Ruins',
    'Mario Circuit', 'Toad Harbor', 'Twisted Mansion', 'Shy Guy Falls',
    'Sunshine Airport', 'Dolphin Shoals', 'Electrodrome', 'Mount Wario',
    'Cloudtop Cruise', 'Bone-Dry Dunes', "Bowser's Castle", 'Rainbow Road',
    'Wii Moo Moo Meadows', 'GBA Mario Circuit', 'DS Cheep Cheep Beach', "N64 Toad's Turnpike",
    'GCN Dry Dry Desert', 'SNES Donut Plains 3', 'N64 Royal Raceway', '3DS DK Jungle',
    'DS Wario Stadium', 'GCN Sherbet Land', '3DS Music Park', 'N64 Yoshi Valley',
    'DS Tick-Tock Clock', '3DS Piranha Plant Slide', 'Wii Grumble Volcano', 'N64 Rainbow Road',
    'GCN Yoshi Circuit', 'Excitebike Arena', 'Dragon Driftway', 'Mute City',
    "Wii Wario's Gold Mine", 'SNES Rainbow Road', 'Ice Ice Outpost', 'Hyrule Circuit',
    'GCN Baby Park', 'GBA Cheese Land', 'Wild Woods', 'Animal Crossing',
    '3DS Neo Bowser City', 'GBA Ribbon Road', 'Super Bell Subway', 'Big Blue'
]

###############################################################################
# Players Colors
###############################################################################
ALPHA_HEX = '95'
PLYRS = {
    'Alele':    {'color': '#ADE300', 'votes': vos.ALELE },
    'Amaya':    {'color': '#92a0ab', 'votes': vos.AMAYA }, 
    'April':    {'color': '#2EB2FF', 'votes': vos.APRIL },
    'Chip':     {'color': '#2837af', 'votes': vos.CHIP  },
    'Chris':    {'color': '#45d40c', 'votes': vos.CHRIS },
    'Leo':      {'color': '#FF91D0', 'votes': vos.LEO   },
    'Mario':    {'color': '#FF8019', 'votes': vos.MARIO },
    'Mary':     {'color': '#757aff', 'votes': vos.MARY  },
    'Memo':     {'color': '#e30018', 'votes': vos.MEMO  },
    'Riché':    {'color': '#f00fbf', 'votes': vos.RICHIE},
    'Tomás':    {'color': '#FCE900', 'votes': vos.TOMAS },
    'Yami':     {'color': '#F15070', 'votes': vos.YAMI  }  
}
VOID = ('', '#F7F7F8')


###############################################################################
# Cmaps
###############################################################################
AL_MAP = ['#FF006E', '#0C4887', '#e30018', '#f00fbf', '#45d40c']
CMAPS = fun.generateAlphaColorMapFromColorArray(AL_MAP)



REVEAL_ORDER = [
    'Mary', 'Chris', 'Riché', 'Leo', 'Alele', 'Tomás', 
    'Mario', 'Yami', 'April', 'Chip', 'Memo', 'Amaya'
]