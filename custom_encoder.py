import json
from decimal import Decimal

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,decimal):
            return float(obj)

        return json.JSONEncoder.default(self, obj)