-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download
-- list all shows contained in  hbtn_0d_tvshows without a genre linked.
SELECT tv_shows.title, tv_show_genres.genre_id FROM cities
LEFT JOIN tv_show_genres ON tv_show.id = tv_show_genres.show_id WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC