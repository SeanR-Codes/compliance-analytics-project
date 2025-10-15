# Compliance Analytics: Suspicious Transaction Detection

## Overview

This project demonstrates the use of Python and Pandas to analyze a dataset of financial transactions and identify suspicious activity based on a set of compliance rules. The goal is to simulate a real-world scenario faced by a compliance analyst, where one must flag potentially fraudulent or non-compliant behavior for further investigation.

## Key Features

**Large Transaction Monitoring:** The script identifies and flags all transactions over a specified threshold ($1,000) that have been cancelled.
**Shared Infrastructure Detection:** It analyzes the data to find multiple user accounts operating from the same device ID, a common indicator of an organized account farm.
**Data-Driven Analysis:** Uses the Pandas library to efficiently load, filter, and analyze transactional data from a CSV file.

## How to Run This Project

1.  **Prerequisites:** You will need Python and the Pandas library installed.
2.  **Clone the repository (optional):** You can download the files directly or clone the repository to your local machine.
3.  **Execute the Script:** Run the `analyze_transactions.py` script from your terminal. The script will load `transactions.csv`, perform the analysis, and print the suspicious findings directly to the console.

## Example Findings

The script successfully identifies two primary types of suspicious activity from the sample data:

**High-Value Cancelled Orders:** Several accounts with structured usernames (e.g., `witty_ivy_*`, `flowy_ridge_*`) were found to have made and then cancelled purchases over $1,000.
**Linked Accounts:** Accounts `witty_ivy_bloom` and `witty_ivy_grove` were both linked to the same device ID (`JKL-101`), strongly suggesting they are controlled by the same entity.
