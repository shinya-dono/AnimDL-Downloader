import argparse
import os
from pathlib import Path
from AnimDL import AnimDL
from clint.textui import progress
import requests
import re
from urllib.parse import unquote


red = "\033[1;31m"
gr = "\033[1;32m"
cy = "\033[1;36m"

pars = argparse.ArgumentParser()

pars.add_argument("id")
pars.add_argument("-m", "--max-quality", action="store_true", dest="max")
pars.add_argument("-s", "--season", type=int, default=1)
pars.add_argument("-e", "--episodes", nargs="*", type=int)

args = pars.parse_args()

downloader = AnimDL(int(args.id))
print(f"{gr}[+] downloading {cy} {downloader.anime.title}")

if not args.max:
    i = 0
    for q in downloader.anime.qualities:
        print(gr + '[' + cy + str(i) + gr + ']' + cy + ' - ' + q)
        i += 1

    print(gr + '[+] Choose a quality to download')
    g_index = input(gr + "[+] Enter a Number : " + red)
    downloader.select_quality(int(g_index))
else:
    downloader.select_quality(len(downloader.anime.qualities) - 1)


print(gr + '[+] enter your anime directory (e.x : D:/anime)')
anime_path = input(gr + "[+] your anime path : " + red)
anime_path = Path(f"{anime_path}/{downloader.anime.title.capitalize()}/Season {args.season}/")

ep = 0
for url in downloader.anime.links:
    ep += 1
    if args.episodes:
        if ep not in args.episodes:
            continue

    r = requests.get(url, stream=True)

    name = ''
    if "Content-Disposition" in r.headers.keys():
        name = re.findall("filename=(.+)", r.headers["Content-Disposition"])[0]
    else:
        name = url.split("/")[-1]

    path = anime_path / unquote(name)
    os.makedirs(os.path.dirname(path), exist_ok=True)

    print(f"{gr}[+] downloading episode {red} {ep}")

    with open(path, 'wb') as f:
        total_length = int(r.headers['Content-Length'])
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length / 1024) + 1):
            if chunk:
                f.write(chunk)
                f.flush()

print(red + "done")
