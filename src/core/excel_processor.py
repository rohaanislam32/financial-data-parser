import pandas as pd

class ExcelProcessor:
    def __init__(self):
        self.files = {}

    def load_files(self, file_paths):
        for path in file_paths:
            try:
                xls = pd.ExcelFile(path, engine='openpyxl')
                self.files[path] = xls
            except Exception as e:
                print(f"Failed to load {path}: {e}")

    def get_sheet_info(self):
        for path, xls in self.files.items():
            print(f"\nFile: {path}")
            for sheet in xls.sheet_names:
                try:
                    df = xls.parse(sheet)
                    print(f"Sheet: {sheet}, Rows: {df.shape[0]}, Columns: {df.shape[1]}")
                    print("Columns:", df.columns.tolist())
                except Exception as e:
                    print(f"Error reading sheet {sheet}: {e}")

    def extract_data(self, path, sheet):
        return self.files[path].parse(sheet)

    def preview_data(self, path, sheet, rows=5):
        df = self.extract_data(path, sheet)
        print(df.head(rows))
