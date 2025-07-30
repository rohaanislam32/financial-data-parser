import re
import pandas as pd

class DataTypeDetector:
    def analyze_column(self, series):
        sample = series.dropna().astype(str).head(20)
        total = len(sample)
        if total == 0:
            return {'detected_type': 'unknown', 'confidence': {}}

        date_matches, num_matches = 0, 0
        for val in sample:
            if re.search(r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}', val) or re.search(r'\d{4}[/-]\d{1,2}[/-]\d{1,2}', val):
                date_matches += 1
            try:
                float(re.sub(r'[^\d.-]', '', val))
                num_matches += 1
            except:
                continue

        date_conf = date_matches / total
        num_conf = num_matches / total
        string_conf = 1 - max(date_conf, num_conf)

        if date_conf > 0.7:
            dtype = 'date'
        elif num_conf > 0.7:
            dtype = 'number'
        else:
            dtype = 'string'

        return {
            'detected_type': dtype,
            'confidence': {
                'date': round(date_conf, 2),
                'number': round(num_conf, 2),
                'string': round(string_conf, 2)
            }
        }
