import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.custom.cronexceptions import FieldExpansionError

# CronField Class (the actual expansion logic remains the same for all)
class CronField:
    def __init__(self, field_expr: str, min_value: int, max_value: int):
        self.field_expr = field_expr
        self.min_value = min_value
        self.max_value = max_value

    def expand(self, expression=None):
        """
        Expands the cron field expression into a list of valid values.
        Supports wildcards (*), ranges, step values, and lists.
        """
        parse_expression = ""
        if expression is None:
            parse_expression = self.field_expr
        else:
            parse_expression = expression

        if parse_expression == "*":
            return list(range(self.min_value, self.max_value + 1))
        elif "," in parse_expression:
            return self._expand_list(parse_expression)
        elif "-" in parse_expression and "/" not in parse_expression:
            return self._expand_range(parse_expression)
        elif "/" in parse_expression:
            return self._expand_step(parse_expression)
        else:
            if not(self.max_value >= int(parse_expression) >= self.min_value):
                raise FieldExpansionError(f"Value {int(parse_expression)} out of bounds for field value min: {self.min_value} and max: {self.max_value}") 
            return [int(parse_expression)]

# 1,2-40/15 0 1,15 * 1-5 /usr/bin/find
    def _expand_list(self, parse_expression: str):
        computed_set = set()
        try:
            for x in parse_expression.split(","):
                result = self.expand(x)
                if isinstance(result, list):
                    result.extend(list(computed_set))
                    computed_set = set(result)
                else:
                    computed_set.add(int(result))
               
        except Exception as e:
            raise FieldExpansionError(e)       
        return sorted(computed_set)

    def _expand_range(self, range_expr):
        try:
            start, end = map(int, range_expr.split("-"))
            if not(self.max_value >= start >= self.min_value and self.max_value >= end >= self.min_value):
                raise FieldExpansionError(f"Value {start}/{end} out of bounds for field value min: {self.min_value} and max: {self.max_value}")
            if start < end:
                return list(range(start, end + 1))
            else:
                # adding custom round-about range
                pending_range = list(range(start, self.max_value + 1))
                next_range = list(range(self.min_value, end + 1))
                pending_range.extend(next_range)
                return pending_range
        except Exception as e:
            raise FieldExpansionError(e)

    def _expand_step(self,parse_expression: str):
        try:
            if parse_expression.startswith("*/"):
                step = int(parse_expression[2:])
                return list(range(self.min_value, self.max_value + 1, step))
            elif "-" in parse_expression:
                range_part, step = parse_expression.split("/")
                start, end = map(int, range_part.split("-"))
                if not(self.max_value >= start >= self.min_value and self.max_value >= end >= self.min_value):
                    raise FieldExpansionError(f"Value {start}/{end} out of bounds for field value min: {self.min_value} and max: {self.max_value}")
                step = int(step)
                return list(range(start, end + 1, step))
            else:
                step = int(parse_expression.split("/")[1])
                return list(range(int(parse_expression.split("/")[0]), self.max_value + 1, step))
        except Exception as e:
            raise FieldExpansionError(e)