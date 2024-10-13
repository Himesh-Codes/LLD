# CronField Class (the actual expansion logic remains the same for all)
class CronField:
    def __init__(self, field_expr: str, min_value: int, max_value: int):
        self.field_expr = field_expr
        self.min_value = min_value
        self.max_value = max_value

    def expand(self):
        """
        Expands the cron field expression into a list of valid values.
        Supports wildcards (*), ranges, step values, and lists.
        """
        if self.field_expr == "*":
            return list(range(self.min_value, self.max_value + 1))
        elif "," in self.field_expr:
            return self._expand_list()
        elif "-" in self.field_expr and "/" not in self.field_expr:
            return self._expand_range(self.field_expr)
        elif "/" in self.field_expr:
            return self._expand_step()
        else:
            return [int(self.field_expr)]

    def _expand_list(self):
        return sorted(set(int(x) for x in self.field_expr.split(",")))

    def _expand_range(self, range_expr):
        start, end = map(int, range_expr.split("-"))
        return list(range(start, end + 1))

    def _expand_step(self):
        if self.field_expr.startswith("*/"):
            step = int(self.field_expr[2:])
            return list(range(self.min_value, self.max_value + 1, step))
        elif "-" in self.field_expr:
            range_part, step = self.field_expr.split("/")
            start, end = map(int, range_part.split("-"))
            step = int(step)
            return list(range(start, end + 1, step))
        else:
            step = int(self.field_expr.split("/")[1])
            return list(range(int(self.field_expr.split("/")[0]), self.max_value + 1, step))