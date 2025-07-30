# 📊 Financial Data Parser

A robust and extensible Python-based tool for reading, analyzing, parsing, and querying complex financial Excel datasets. This project is designed to work with real-world banking and ledger files that use inconsistent formatting across amounts, currencies, and dates.

---

## 🔍 Project Overview

The goal of this project is to build a structured pipeline that:

- Reads Excel files using `pandas` and `openpyxl`
- Automatically detects column types (e.g., amount, date, string)
- Parses various complex formats like:
  - Amounts: `$1,234.56`, `€1.234,56`, `₹1,23,456`, `(1,234.56)`, `1.2M`
  - Dates: `MM/DD/YYYY`, `Q4 2023`, `Dec-23`, Excel serial numbers
- Stores data using efficient structures for fast querying and aggregation
- Supports queries such as filtering by date/amount range

---

## 🧰 Technologies Used

- `pandas` for data manipulation  
- `openpyxl` for Excel file support  
- `re` for format parsing  
- `datetime`, `decimal`, `locale` for specialized formatting  
- `sqlite3` as a lightweight optional backend

## 📁 Project Structure
``` 
Financial-data-parser/ ├── config/ # Configuration files │ └── settings.py │ ├── data/ # Input and output data │ ├── sample/ # Sample input Excel files │ │ ├── KH_Bank.XLSX │ │ └── Customer_Ledger_Entries_FULL.xlsx │ └── processed/ # Processed output (optional) │ ├── examples/ # Example usage scripts │ ├── basic_usage.py │ ├── advanced_parsing.py │ └── performance_demo.py │ ├── scripts/ # Benchmark and automation scripts │ └── run_benchmarks.py │ ├── src/ # Core functionality │ ├── core/ │ │ ├── excel_processor.py │ │ ├── type_detector.py │ │ ├── format_parser.py │ │ └── data_storage.py │ ├── utils/ │ │ ├── helpers.py │ │ └── validators.py │ └── __init__.py │ ├── tests/ # Unit tests │ ├── test_excel_processor.py │ ├── test_type_detector.py │ ├── test_format_parser.py │ └── test_data_storage.py │ ├── main.py # Main script to run the parser ├── requirements.txt # Project dependencies ├── README.md # Project documentation └── setup.py # Project setup (optional)

```

## 🧪 Sample Output

**File:** `KH_Bank.XLSX`  
**Sheet:** Sheet1, Rows: 1221, Columns: 56  
**Columns:** `['GroupHeader.MessageIdentification', ..., 'TransactionDetails.AdditionalTransactionInformation']`

**File:** `Customer_Ledger_Entries_FULL.xlsx`  
**Sheet:** Customer Ledger Entries, Rows: 5505, Columns: 44  
**Columns:** `['Posting Date', 'VAT Date', ..., 'Document Subtype']`

=== Amount Parsing ===
$1,234.56 -> 1234.56
(2,500.00) -> -2500.0
€1.234,56 -> 1234.56
1.5M -> 1500000.0
₹1,23,456 -> 123456.0

=== Date Parsing ===
12/31/2023 -> 2023-12-31
2023-12-31 -> 2023-12-31
Q4 2023 -> 2023-10-01
Dec-23 -> 2023-12-01
44927 -> 2023-01-01

yaml
Copy
Edit

---

## 🚀 How to Run

1. Clone the repo or download the code.
2. Make sure your Excel files are located in `data/sample/`.
3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
Run the main script:

python main.py


🧠 Future Improvements

Add support for more currency and locale-specific formats

Interactive dashboard with filters

Integration with cloud storage and APIs

📝 License
This project is for educational and internal demonstration purposes only.
