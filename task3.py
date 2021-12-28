import pandas as pd
import sqlite3

conn = sqlite3.connect("/Users/varungandhi/Downloads/codes_python_assignment/assignment2_2122/chinook.db")

curs = conn.cursor()
curs.execute("SELECT name FROM sqlite_master WHERE type='table';")

# print(curs.fetchall())


data = pd.read_sql(
    """

SELECT t.Name AS name_of_track, t.Composer,a.Title AS album_name, ar.Name as artist_name

FROM tracks as t
INNER JOIN albums a ON t.AlbumId= a.AlbumId
INNER JOIN artists ar ON a.ArtistId= ar.ArtistId
WHERE t.milliseconds >= 90000 and t.milliseconds <= 120000
ORDER BY t.Composer
""",
    conn,
)


with pd.option_context(
    "display.max_rows", None, "display.max_columns", None
):  # more options can be specified also
    print(data)

#data.to_excel('/Users/varungandhi/Downloads/data.xlsx')
