# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 21:10:11 2023

@author: Nino
"""

from aoc import *
import pandas as pd
import numpy as np


hands = read_input('day07/input')


# =============================================================================
# PART 1
# =============================================================================
transform = {'A': 14,
             'K': 13,
             'Q': 12,
             'J': 11,
             'T': 10}

df = pd.DataFrame(index=np.arange(len(hands)), dtype=int)

for i, hand in enumerate(hands):
    df_temp = pd.Series(np.zeros(13), index=np.arange(2, 15), dtype=int)
    df_temp[:] = 0
    hand, bid = hand.split(' ')
    bid = int(bid)
    df.loc[i, 'bid'] = bid
    hand = list(hand)
    for n, card in enumerate(hand):
        if card.isdigit():
            card = int(card)
        else:
            card = transform[card]
        df_temp[card] += 1
        df.loc[i, n] = card
    df.loc[i, 'value'] = (df_temp**2).sum()

df = df.sort_values(by=['value', 0, 1, 2, 3, 4])
df = df.reset_index()
df['winning'] = (df.index+1) * df.bid

print(df['winning'].sum())


# =============================================================================
# PART 2
# =============================================================================
transform = {'A': 14,
             'K': 13,
             'Q': 12,
             'J': 1,
             'T': 10}

hands = read_input('day07/input')

df = pd.DataFrame(index=np.arange(len(hands)), dtype=int)


for i, hand in enumerate(hands):
    df_temp = pd.Series(np.zeros(14), index=np.arange(1, 15), dtype=int)
    df_temp[:] = 0
    hand, bid = hand.split(' ')
    bid = int(bid)
    df.loc[i, 'bid'] = bid
    hand = list(hand)
    for n, card in enumerate(hand):
        if card.isdigit():
            card = int(card)
        else:
            card = transform[card]
        df_temp[card] += 1
        df.loc[i, n] = card
    joker_card = df_temp[1:].sort_index(ascending=False).idxmax()
    if df_temp[1] > 0:
        df.loc[i, 'joker'] = joker_card
    for j in range(df_temp[1]):
        df_temp[1] -= 1
        df_temp[joker_card] += 1
    df.loc[i, 'value'] = (df_temp**2).sum()

df = df.sort_values(by=['value', 0, 1, 2, 3, 4])
df = df.reset_index()
df['winning'] = (df.index+1) * df.bid

print(df['winning'].sum())

