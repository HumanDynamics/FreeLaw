There are three periods of time. The 2013-1926 is acceptable. 1926-1878 data has minor errors, documented below. The pre-1878 data should be discarded with prejudice at the present time. There exist pages documenting all changes, and this does not seem like a theoretically unsolvable problem: merely a pain that I do not have time to deal with adequately. It is currently a recommendation that anyone wishing to do analysis remove all pre-1926 data.

Everything before 1926 has sections that have been changed all over the place relative to the post-1926 stuff. On the order of a thousand changes seem to have been made. A rough Fermi estimate is that the 1878-1926 has roughly 5% error. http://uscode.house.gov/tables/usctable1.htm

The revised statutes: "R.S. — Revised Statutes of 1878; where “R.S.” followed by a section number appears, the provision was restated in the cited section of the Revised Statutes of 1878 (locations in the Code where sections of the Revised Statutes of 1878 can be found are included in Table II, which is a separate table for the Code)" http://uscode.house.gov/tables/usctable2.htm

If you just want to run the code, fileShifter.primary is the function you want, and it has reasonably sensible defaults.

The basic flow is as follows:
	table3_scraper.main() will fetch a large number of files. This program takes a long time to run.
	import parseAllTables as pat
	pat.all_years(lambda x:(pat.title_mods(pat.directory_to_changes_list(x)))) will get you the full dictionaries.
	fileShifter.dict_to_json_file will take that and give a json file, and from there fileShifter.changes_json_to_csv is good.

Folders:
----products contains everything you have as an output from your analysis.
----jsonFrequencies has files for each year, and each year has a json file roughly equivalent to a dict.
----crosslaws contains additional information on the table3 analysis from sunlight labs, and it's very handy.
----yearlyChanges is just the written forms of python lists containing all the information about each change. It's totally lossless relative to what ParseTable would give you, and much faster because you won't have to wade through html.
----table3_pages is only to be used in emergencies, as it will take minutes to parse through.