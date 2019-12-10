#!/usr/bin/env python
# coding: utf-8

# In[1]:


oplsaa_sigmas = {
    "ALA": {
        "C": 0.21046163,
        "CA": 0.19643086,
        "CB": 0.19643086,
        "HA": 0.14030776,
        "HB1": 0.14030776,
        "HB2": 0.14030776,
        "HB3": 0.14030776,
        "HN": 0.0,
        "N": 0.18240008000000002,
        "O": 0.16612438000000002
    },
    "ARG": {
        "C": 0.21046163,
        "CA": 0.19643086,
        "CB": 0.19643086,
        "CD": 0.19643086,
        "CG": 0.19643086,
        "CZ": 0.12627698,
        "HA": 0.14030776,
        "HB1": 0.14030776,
        "HB2": 0.14030776,
        "HD1": 0.14030776,
        "HD2": 0.14030776,
        "HE": 0.0,
        "HG1": 0.14030776,
        "HG2": 0.14030776,
        "HH11": 0.0,
        "HH12": 0.0,
        "HH21": 0.0,
        "HH22": 0.0,
        "HN": 0.0,
        "N": 0.18240008000000002,
        "NE": 0.18240008000000002,
        "NH1": 0.18240008000000002,
        "NH2": 0.18240008000000002,
        "O": 0.16612438000000002
    },
    "ASN": {
        "C": 0.21046163,
        "CA": 0.19643086,
        "CB": 0.19643086,
        "CG": 0.21046163,
        "HA": 0.14030776,
        "HB1": 0.14030776,
        "HB2": 0.14030776,
        "HD21": 0.0,
        "HD22": 0.0,
        "HN": 0.0,
        "N": 0.18240008000000002,
        "ND2": 0.18240008000000002,
        "O": 0.16612438000000002,
        "OD1": 0.16612438000000002
    },
    "ASP": {
        "C": 0.21046163,
        "CA": 0.19643086,
        "CB": 0.19643086,
        "CG": 0.21046163,
        "HA": 0.14030776,
        "HB1": 0.14030776,
        "HB2": 0.14030776,
        "HN": 0.0,
        "N": 0.18240008000000002,
        "O": 0.16612438000000002,
        "OD1": 0.16612438000000002,
        "OD2": 0.16612438000000002
    },
    "CYS": {
        "C": 0.21046163,
        "CA": 0.19643086,
        "CB": 0.19643086,
        "HA": 0.14030776,
        "HB1": 0.14030776,
        "HB2": 0.14030776,
        "HG1": 0.0,
        "HN": 0.0,
        "N": 0.18240008000000002,
        "O": 0.16612438000000002,
        "SG": 0.20204317
    },
    "GLN": {
        "C": 0.21046163,
        "CA": 0.19643086,
        "CB": 0.19643086,
        "CD": 0.21046163,
        "CG": 0.19643086,
        "HA": 0.14030776,
        "HB1": 0.14030776,
        "HB2": 0.14030776,
        "HE21": 0.0,
        "HE22": 0.0,
        "HG1": 0.14030776,
        "HG2": 0.14030776,
        "HN": 0.0,
        "N": 0.18240008000000002,
        "NE2": 0.18240008000000002,
        "O": 0.16612438000000002,
        "OE1": 0.16612438000000002
    },
    "GLU": {
        "C": 0.21046163,
        "CA": 0.19643086,
        "CB": 0.19643086,
        "CD": 0.21046163,
        "CG": 0.19643086,
        "HA": 0.14030776,
        "HB1": 0.14030776,
        "HB2": 0.14030776,
        "HG1": 0.14030776,
        "HG2": 0.14030776,
        "HN": 0.0,
        "N": 0.18240008000000002,
        "O": 0.16612438000000002,
        "OE1": 0.16612438000000002,
        "OE2": 0.16612438000000002
    },
    "GLY": {
        "C": 0.21046163,
        "CA": 0.19643086,
        "HA1": 0.14030776,
        "HA2": 0.14030776,
        "HN": 0.0,
        "N": 0.18240008000000002,
        "O": 0.16612438000000002
    },
    "HIS": {
        "C": 0.21046163,
        "CA": 0.19643086,
        "CB": 0.19643086,
        "CD2": 0.19923701,
        "CE1": 0.19923701,
        "CG": 0.19923701,
        "HA": 0.14030776,
        "HB1": 0.14030776,
        "HB2": 0.14030776,
        "HD1": 0.0,
        "HD2": 0.13581791000000001,
        "HE1": 0.13581791000000001,
        "HN": 0.0,
        "N": 0.18240008000000002,
        "ND1": 0.18240008000000002,
        "NE2": 0.18240008000000002,
        "O": 0.16612438000000002
    },
    "ILE": {
        "C": 0.21046163,
        "CA": 0.19643086,
        "CB": 0.19643086,
        "CD1": 0.19643086,
        "CG1": 0.19643086,
        "CG2": 0.19643086,
        "HA": 0.14030776,
        "HB": 0.14030776,
        "HD1": 0.14030776,
        "HD2": 0.14030776,
        "HD3": 0.14030776,
        "HG11": 0.14030776,
        "HG12": 0.14030776,
        "HG21": 0.14030776,
        "HG22": 0.14030776,
        "HG23": 0.14030776,
        "HN": 0.0,
        "N": 0.18240008000000002,
        "O": 0.16612438000000002
    },
    "LEU": {
        "C": 0.21046163,
        "CA": 0.19643086,
        "CB": 0.19643086,
        "CD1": 0.19643086,
        "CD2": 0.19643086,
        "CG": 0.19643086,
        "HA": 0.14030776,
        "HB1": 0.14030776,
        "HB2": 0.14030776,
        "HD11": 0.14030776,
        "HD12": 0.14030776,
        "HD13": 0.14030776,
        "HD21": 0.14030776,
        "HD22": 0.14030776,
        "HD23": 0.14030776,
        "HG": 0.14030776,
        "HN": 0.0,
        "N": 0.18240008000000002,
        "O": 0.16612438000000002
    },
    "LYS": {
        "C": 0.21046163,
        "CA": 0.19643086,
        "CB": 0.19643086,
        "CD": 0.19643086,
        "CE": 0.19643086,
        "CG": 0.19643086,
        "HA": 0.14030776,
        "HB1": 0.14030776,
        "HB2": 0.14030776,
        "HD1": 0.14030776,
        "HD2": 0.14030776,
        "HE1": 0.14030776,
        "HE2": 0.14030776,
        "HG1": 0.14030776,
        "HG2": 0.14030776,
        "HN": 0.0,
        "HZ1": 0.0,
        "HZ2": 0.0,
        "HZ3": 0.0,
        "N": 0.18240008000000002,
        "NZ": 0.18240008000000002,
        "O": 0.16612438000000002
    },
    "MET": {
        "C": 0.21046163,
        "CA": 0.19643086,
        "CB": 0.19643086,
        "CE": 0.19643086,
        "CG": 0.19643086,
        "HA": 0.14030776,
        "HB1": 0.14030776,
        "HB2": 0.14030776,
        "HE1": 0.14030776,
        "HE2": 0.14030776,
        "HE3": 0.14030776,
        "HG1": 0.14030776,
        "HG2": 0.14030776,
        "HN": 0.0,
        "N": 0.18240008000000002,
        "O": 0.16612438000000002,
        "SD": 0.20204317
    },
    "PHE": {
        "C": 0.21046163,
        "CA": 0.19643086,
        "CB": 0.19643086,
        "CD1": 0.19923701,
        "CD2": 0.19923701,
        "CE1": 0.19923701,
        "CE2": 0.19923701,
        "CG": 0.19923701,
        "CZ": 0.19923701,
        "HA": 0.14030776,
        "HB1": 0.14030776,
        "HB2": 0.14030776,
        "HD1": 0.13581791000000001,
        "HD2": 0.13581791000000001,
        "HE1": 0.13581791000000001,
        "HE2": 0.13581791000000001,
        "HN": 0.0,
        "HZ": 0.13581791000000001,
        "N": 0.18240008000000002,
        "O": 0.16612438000000002
    },
    "PRO": {
        "C": 0.21046163,
        "CA": 0.19643086,
        "CB": 0.19643086,
        "CD": 0.19643086,
        "CG": 0.19643086,
        "HA": 0.14030776,
        "HB1": 0.14030776,
        "HB2": 0.14030776,
        "HD1": 0.14030776,
        "HD2": 0.14030776,
        "HG1": 0.14030776,
        "HG2": 0.14030776,
        "N": 0.18240008000000002,
        "O": 0.16612438000000002
    },
    "SER": {
        "C": 0.21046163,
        "CA": 0.19643086,
        "CB": 0.19643086,
        "HA": 0.14030776,
        "HB1": 0.14030776,
        "HB2": 0.14030776,
        "HG1": 0.0,
        "HN": 0.0,
        "N": 0.18240008000000002,
        "O": 0.16612438000000002,
        "OG": 0.17510408
    },
    "THR": {
        "C": 0.21046163,
        "CA": 0.19643086,
        "CB": 0.19643086,
        "CG2": 0.19643086,
        "HA": 0.14030776,
        "HB": 0.14030776,
        "HG1": 0.0,
        "HG21": 0.14030776,
        "HG22": 0.14030776,
        "HG23": 0.14030776,
        "HN": 0.0,
        "N": 0.18240008000000002,
        "O": 0.16612438000000002,
        "OG1": 0.17510408
    },
    "TRP": {
        "C": 0.21046163,
        "CA": 0.19643086,
        "CB": 0.19643086,
        "CD1": 0.19923701,
        "CD2": 0.19923701,
        "CE2": 0.19923701,
        "CE3": 0.19923701,
        "CG": 0.19923701,
        "CH2": 0.19923701,
        "CZ2": 0.19923701,
        "CZ3": 0.19923701,
        "HA": 0.14030776,
        "HB1": 0.14030776,
        "HB2": 0.14030776,
        "HD1": 0.13581791000000001,
        "HE1": 0.0,
        "HE3": 0.13581791000000001,
        "HH2": 0.13581791000000001,
        "HN": 0.0,
        "HZ2": 0.13581791000000001,
        "HZ3": 0.13581791000000001,
        "N": 0.18240008000000002,
        "NE1": 0.18240008000000002,
        "O": 0.16612438000000002
    },
    "TYR": {
        "C": 0.21046163,
        "CA": 0.19643086,
        "CB": 0.19643086,
        "CD1": 0.19923701,
        "CD2": 0.19923701,
        "CE1": 0.19923701,
        "CE2": 0.19923701,
        "CG": 0.19923701,
        "CZ": 0.19923701,
        "HA": 0.14030776,
        "HB1": 0.14030776,
        "HB2": 0.14030776,
        "HD1": 0.13581791000000001,
        "HD2": 0.13581791000000001,
        "HE1": 0.13581791000000001,
        "HE2": 0.13581791000000001,
        "HH": 0.0,
        "HN": 0.0,
        "N": 0.18240008000000002,
        "O": 0.16612438000000002,
        "OH": 0.17229792
    },
    "VAL": {
        "C": 0.21046163,
        "CA": 0.19643086,
        "CB": 0.19643086,
        "CG1": 0.19643086,
        "CG2": 0.19643086,
        "HA": 0.14030776,
        "HB": 0.14030776,
        "HG11": 0.14030776,
        "HG12": 0.14030776,
        "HG13": 0.14030776,
        "HG21": 0.14030776,
        "HG22": 0.14030776,
        "HG23": 0.14030776,
        "HN": 0.0,
        "N": 0.18240008000000002,
        "O": 0.16612438000000002
    }
}


# In[ ]:


oplsaa_residues = {
    "": {"": ""
    }
}


# In[ ]:



