_ff="-fflags +nofillin -fflags +genpts -fflags +igndts"

#_1="-bsf:a aac_adtstoasc"
_1="-map 0:v:0 -map 0:a:2"
_2="-bsf:v mpeg4_unpack_bframes"

_add="$_1 $_2"

#_subs="-i ${1%.avi}.srt -scodec mov_text -metadata:s:s:0 language=eng"

ffmpeg -hide_banner $_ff  -i "$1" $_subs -vcodec copy -acodec ac3 -y $_add "${1%.avi}.mp4"
#ffprobe -hide_banner -show_streams "${1%.avi}".mp4
