import os
from datetime import datetime
from src.core.excel_processor import ExcelProcessor
from src.core.type_detector import DataTypeDetector
from src.core.format_parser import FormatParser
from src.core.data_storage import FinancialDataStore

def main():
    # File paths
    file_paths = [
        "C:\\Users\\HP\\Desktop\\financial-data-parser\\data\\sample\\KH_Bank.XLSX",
        "C:\\Users\\HP\\Desktop\\financial-data-parser\\data\\sample\\Customer_Ledger_Entries_FULL.xlsx"
    ]

    # Initialize components
    excel = ExcelProcessor()
    detector = DataTypeDetector()
    parser = FormatParser()
    store = FinancialDataStore()

    # Load and analyze files
    excel.load_files(file_paths)
    excel.get_sheet_info()

    for path, xls in excel.files.items():
        for sheet in xls.sheet_names:
            df = xls.parse(sheet)
            types = {}

            # Detect column types
            for col in df.columns:
                result = detector.analyze_column(df[col])
                types[result['detected_type']] = col

            # Parse values
            if 'amount' in types:
                df[types['amount']] = df[types['amount']].apply(parser.parse_amount)
            if 'date' in types:
                df[types['date']] = df[types['date']].apply(parser.parse_date)

            # Store dataset
            dataset_name = f"{os.path.basename(path)}:{sheet}"
            store.add_dataset(dataset_name, df, types)

    # Sample query
    print("\nQuery Sample:")
    for name in store.data:
        result = store.query_by_criteria(name, amount_range=(1000, 5000))
        if result is not None:
            print(f"\n{name}:")
            print(result.head())


if __name__ == "__main__":
    main()

    # Run FormatParser tests
    parser = FormatParser()

    test_amounts = [
        "$1,234.56",
        "(2,500.00)",
        "€1.234,56",
        "1.5M",
        "₹1,23,456"
    ]

    test_dates = [
        "12/31/2023",
        "2023-12-31",
        "Q4 2023",
        "Dec-23",
        "44927"
    ]

    print("\n=== Amount Parsing ===")
    for val in test_amounts:
        parsed = parser.parse_amount(val)
        print(f"{val} -> {parsed}")

    print("\n=== Date Parsing ===")
    for val in test_dates:
        parsed = parser.parse_date(val)
        print(f"{val} -> {parsed}")
