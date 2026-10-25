#!/usr/bin/env python3
"""Fetch latest YouTube videos for @HosannaInExcelsis into data/videos.json."""
import json, urllib.request, xml.etree.ElementTree as ET
CH = "UCW8KVz_QO-1y2W_yQLCcG3w"
URL = f"https://www.youtube.com/feeds/videos.xml?channel_id={CH}"
NS = {"a": "http://www.w3.org/2005/Atom", "yt": "http://www.youtube.com/xml/schemas/2015", "media": "http://search.yahoo.com/mrss/"}
req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
root = ET.fromstring(urllib.request.urlopen(req, timeout=30).read())
vids = []
for e in root.findall("a:entry", NS)[:6]:
    vid = e.find("yt:videoId", NS).text
    vids.append({"id": vid, "title": e.find("a:title", NS).text,
                 "published": e.find("a:published", NS).text,
                 "url": f"https://www.youtube.com/watch?v={vid}",
                 "thumb": f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg"})
if not vids:
    raise SystemExit("no videos in feed; keeping existing file")
with open("data/videos.json", "w", encoding="utf-8") as f:
    json.dump({"channel": "https://www.youtube.com/@HosannaInExcelsis", "videos": vids}, f, ensure_ascii=False, indent=2)
    f.write("\n")
print(len(vids), "videos")
