--  a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows AS ts 
JOIN tv_show_genres AS tg 
ON ts.id = tg.show_id
ORDER BY ts.title, tg.genre_id ASC;