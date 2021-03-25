
import votes as vos
from scipy.spatial.distance import euclidean, cosine


PRINT_STATS = False
###############################################################################
# Paths and Filenames
###############################################################################
(PT_DTA, PT_PLT) = ('./dta/', './plt/')
(FN_DTA, FN_DST, FN_SCA) = (
    'votesDataframe.csv', 'distMatrix.csv', 'scaledMatrix.csv'
)
###############################################################################
# Distance matrix
###############################################################################
DIST_FUN = cosine
RANGE = (10, 100)

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
    'Leo':      {'color': '#FF9175', 'votes': vos.LEO   }, 
    'Mary':     {'color': '#757aff', 'votes': vos.MARY  },
    'Memo':     {'color': '#e30018', 'votes': vos.MEMO  },
    'Riché':    {'color': '#f00fbf', 'votes': vos.RICHIE},
    'Tomás':    {'color': '#FCE900', 'votes': vos.TOMAS },
    'Yami':     {'color': '#F15062', 'votes': vos.YAMI  }  
}
VOID = ('', '#ffffff')
