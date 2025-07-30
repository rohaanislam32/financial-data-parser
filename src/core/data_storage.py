class FinancialDataStore:
    def __init__(self):
        self.data = {}
        self.indexes = {}
        self.metadata = {}

    def add_dataset(self, name, df, column_types):
        self.data[name] = df
        self.metadata[name] = column_types
        self.indexes[name] = {
            'date_index': df.set_index(column_types['date']) if 'date' in column_types else None,
            'amount_index': df.sort_values(by=column_types.get('amount', df.columns[0]))
        }

    def query_by_criteria(self, name, date_range=None, amount_range=None):
        df = self.data.get(name)
        if df is None:
            return None

        if date_range and 'date' in self.metadata[name]:
            date_col = self.metadata[name]['date']
            df = df[(df[date_col] >= date_range[0]) & (df[date_col] <= date_range[1])]

        if amount_range and 'amount' in self.metadata[name]:
            amt_col = self.metadata[name]['amount']
            df = df[(df[amt_col] >= amount_range[0]) & (df[amt_col] <= amount_range[1])]

        return df
