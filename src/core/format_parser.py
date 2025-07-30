import re
from datetime import datetime, timedelta
import pandas as pd

class FormatParser:
    def parse_amount(self, value: str) -> float:
        if not isinstance(value, str):
            value = str(value)

        # Handle negative in parentheses
        is_negative = False
        if re.match(r'^\(.*\)$', value):
            is_negative = True
            value = value.strip("()")

        # Handle trailing minus
        if value.endswith("-"):
            is_negative = True
            value = value.rstrip("-")

        # Remove currency symbols and whitespace
        value = re.sub(r'[^\d,\.\-KMBkmb]', '', value)

        # Handle abbreviated values
        if re.match(r'^[\d,.]+[KMBkmb]$', value):
            num = float(re.sub(r'[^\d.]', '', value[:-1]))
            suffix = value[-1].upper()
            multiplier = {'K': 1e3, 'M': 1e6, 'B': 1e9}.get(suffix, 1)
            return -num * multiplier if is_negative else num * multiplier

        # Handle European (1.234,56) and Indian (1,23,456.78) formats
        if ',' in value and '.' in value:
            if value.find(',') < value.find('.'):
                value = value.replace(',', '')  # US style
            else:
                value = value.replace('.', '').replace(',', '.')  # European style
        elif ',' in value and '.' not in value:
            value = value.replace(',', '')  # Could be Indian or European

        try:
            result = float(value)
            return -result if is_negative else result
        except:
            return 0.0

    def parse_date(self, value, detected_format=None):
        if pd.isnull(value):
            return pd.NaT

        try:
            # Excel serial date (numeric or numeric string)
            if isinstance(value, (int, float)) and 30 < value < 60000:
                return datetime(1899, 12, 30) + timedelta(days=int(value))

            value_str = str(value).strip()

            if value_str.isdigit():
                serial = int(value_str)
                if 30 < serial < 60000:
                    return datetime(1899, 12, 30) + timedelta(days=serial)

            known_formats = [
                "%m/%d/%Y", "%d/%m/%Y", "%Y-%m-%d", "%d-%b-%Y", "%b-%y", "%B %Y"
            ]
            for fmt in known_formats:
                try:
                    return datetime.strptime(value_str, fmt)
                except:
                    continue

            quarter_match = re.match(r"Q([1-4])[- ]?(\d{2,4})", value_str, re.IGNORECASE)
            if quarter_match:
                q, y = int(quarter_match[1]), int(quarter_match[2])
                if y < 100: y += 2000
                return datetime(y, 3 * (q - 1) + 1, 1)

            return pd.to_datetime(value_str, errors="coerce")

        except Exception as e:
            print(f"Date parse error: {e}")
            return pd.NaT
