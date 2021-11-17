-- lists all genres from hbtn_0d_tvshows and displays the number of shows in each
SELECT tv_genres.name AS genre, COUNT(*) AS 'number_shows'
FROM tv_genres INNER JOIN tv_show_genres ON tv_genre_id = tv_show.genres_id
GROUP BY genre
ORDER BY number_shows DESC;
