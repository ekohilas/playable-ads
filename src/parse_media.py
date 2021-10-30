#!/usr/bin/env python3
import json
from pprint import pprint
import urllib.parse
import sys
import xml.etree.ElementTree as ET
import urllib.request
import os

def main():
    media = json.load(sys.stdin)

    for key in media:
        content = media[key]["content"]
        ad_type = media[key]["adType"]
        if ad_type == "MRAID":
            html = parse_into_html(content)
            with open(f"{key}.html", "w") as file:
                file.write(html)
        elif ad_type == "VIDEO":
            url = parse_into_video_url(content)
            file_basename = os.path.basename(url)
            urllib.request.urlretrieve(url, f"{key}-{file_basename}".strip())
        else:
            raise NotImplementedError

def parse_into_html(content):
    json_decoded_content = json.loads(content)
    url_encoded_html = json_decoded_content["markup"]
    html = urllib.parse.unquote(url_encoded_html)
    return html

def parse_into_video_url(content):
    url_decoded_xml_string = urllib.parse.unquote(content)
    root = ET.fromstring(url_decoded_xml_string)
    url = root.find(".//MediaFile").text
    return url

if __name__ == "__main__":
    main()

