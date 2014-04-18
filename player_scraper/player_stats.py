import pandas as pd

class PlayerStats:
    def __init__(self, name, tables):
        self.name = name
        self.tables = tables

    def __getattr__(self, attr):
        for table in self.tables:
            if table.name.lower() == attr.lower():
                return table

        raise AttributeError

    def __repr__(self):
        return "Player: " + self.name + "\n" + "Stats tables: " + ' '.join(self.table_names())

    def table_names(self):
        return map(lambda x: x.name, self.tables)

    def stats(self):
        return ' '.join(self.totals.indices())

    def advanced_stats(self):
        return ' '.join(self.advanced.indices())

    def lookup_by_stat(self, stat):
        return self._lookup_across_tables(stat)

    def lookup_by_year(self, year):
        if year.lower() == 'career':
            return self.lookup_by_career()

        else:
            return self._lookup_across_tables(year)

    def _lookup_across_tables(self, lookup):
        results = []

        for table in self.tables:
            try:
                result = table[lookup]

            except KeyError:
                pass

            else:
                results.append(result)

        return results


    def lookup_by_career(self):
        results = []

        for table in self.tables:
            career = table.career_stats()
            results.append(career)

        return results


