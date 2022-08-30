import argparse

p = argparse.ArgumentParser()
p.add_argument("source", default="full.mp3")
p.add_argument("tracks", default="trackslist.txt")  # '{track_name} {track_start}' lines, track_start is seconds as colon time, e.g 'Title 0:00'
p.add_argument("artist", default="")
p.add_argument("album", default="")
p.add_argument("--out", default="out")  # output directory
p.add_argument("--ext", default="mp3")

args = p.parse_args()

def to_seconds(t):
    secs = 0
    for i, v in enumerate(t.split(":")[::-1]):
        secs = secs + int(v) * (60 ** i)
    return secs


with open(args.tracks) as f:
    tracks = f.readlines()

res = []
for i, track in enumerate(tracks):
    name, start = track.strip().rsplit(" ", 1)
    res.append([name, start, None])
    if i > 0:
        res[i-1][2] = start 


print("mkdir -p", args.out)
for i, (name, start, end) in enumerate(res):
    meta = "-id3v2_version 3 -write_id3v1 1 -metadata track={!r} -metadata title={!r} -metadata artist={!r} -metadata album={!r}"
    s = "ffmpeg -ss {start} -i {src} {meta} {end} {dest!r}".format(
        start=to_seconds(start),
        src=args.source,
        meta=meta.format(i+1, name, args.artist, args.album),
        end="-t {}".format(to_seconds(end) - to_seconds(start)) if end else "",
        dest="{}/{:02d} - {}.{}".format(args.out, i+1, name, args.ext),
    )
    print(s)
