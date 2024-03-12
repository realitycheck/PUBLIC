# Using ffmpeg to convert DTS audio track to AC3 and add back into MKV?

> ffmpeg -i my_movie.mkv -map 0:v -map 0:a:0 -map 0:a -map 0:s -c:v copy -c:a copy -c:s copy -c:a:0 ac3 -b:a:0 640k my_movie_ac2.mkv
