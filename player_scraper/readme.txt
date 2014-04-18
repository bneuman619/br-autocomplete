To scrape Stephen Curry's stats, import 'make_curry' from scrape_curry.py and call make_curry().

make_curry() returns a PlayerStats object.
Calling stats() on a PlayerStats object returns a list of all the stat tables, by name.

Calling player_stats_object.table_name returns the corresponding StatsTable object.
  E.g., calling curry_stats.totals returns the Totals table.

A StatsTable object responds to a few different lookups.
  stats_table.lookup_by_year('1993-94') will return a StatsRow for that year.
  lookup_by_year (as of now) must exactly match the string - '93-94' won't work, nor will '1994', etc.
  
  You can also lookup by column: stats_table.column_name will return a dict of values for that column by year.
    E.g., curry_stats.totals.fga returns a dict of FGA by year for the Totals table.
    My __getattr__ trickery doesn't work with stats that start with a number, eg 3P%.
    For those stats you need to call lookup_by_stat(stat_header).
    The first lookup style is case-insensitive, but lookup_by_stat() must match exactly.

  stats_table.career() returns a dict for the 'Career' row.
  stats_table.get_years() returns a list of years for the table.

A StatsRow object can return a dictionary of stats for the year via stats_row.dict.
You can also lookup a particular stat via stats_row.fg style.

__repr__() for each of those objects tries to display useful information by default.

As of now, the dict just displays in whatever order, which isn't desirable. But the data is all there.

To scrape any player's stats, pull down the BeautifulSoup object via soupify(url).
Then pass the BS object to make_player_stats in br_player_scraper.py.
