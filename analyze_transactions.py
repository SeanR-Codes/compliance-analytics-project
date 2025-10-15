#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 04:25:41 2025

@author: SeanR-Codes
"""

import pandas as pd

try:
    df = pd.read_csv('transactions.csv')
    print("Successfully loaded.")
except FileNotFoundError:
    print("Error: Not found.")
    exit()

# Find large, cancelled transactions.
print("\n--- Finding large, cancelled transactions ---")
large_cancelled_transactions = df[
    (df['transaction_amount'] > 1000) &
    (df['status'] == 'Cancelled')
]
print(large_cancelled_transactions)

# Find devices used by more than one account.
print("--- Finding shared device IDs ---")
device_counts = df['device_id'].value_counts()

# Filter by device IDs that appear more than once
shared_devices = device_counts[device_counts > 1].index.tolist()

# Get all transactions from accounts using these shared devices.
suspicious_shared_devices = df[df['device_id'].isin(shared_devices)]
print(suspicious_shared_devices)
