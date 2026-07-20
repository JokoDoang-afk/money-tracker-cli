# Money Tracker CLI v0.11

## Description

Money Tracker CLI is a simple command-line application that helps users manage their income and expenses. By recording every transaction, users can easily track their spending habits and understand where their money goes.

## Features

- Add income
- Add expense
- Categorize transactions
- View transaction history
- Calculate balance from transaction history
- View balance
- Search Categorize base on transaction


## Technologies

- Python 3.x
- JSON
- Git
- GitHub

## Installation

1. Clone this repository

```bash
git clone https://github.com/JokoDoang-afk/money-tracker-cli.git
```

2. Go to the project folder

```bash
cd money-tracker-cli
```

3. Run the application

```bash
python main.py
```

After running the application, choose one of the available menu options.

## Usage

After running the application, choose one of the available menu options.

Example:

```text
===== Money Tracker =====
1. Add Income
2. Add Expense
3. View Balance
4. View Transaction History
5. Exit
```

## Project Structure

money-tracker-cli/
│
├── main.py
├── data.json
├── storage.py
├── transactions.py
└── README.md

## Future Features
- Monthly reports
- Edit transactions
- Delete transactions
- Export to CSV
- SQLite Database
- REST API
- Desktop GUI

## Current Version

Current version: **v0.11**

Implemented features:

- ✅ Add income
- ✅ Add expense
- ✅ Transaction history
- ✅ JSON persistence
- ✅ Input validation
- ✅ Modular architecture