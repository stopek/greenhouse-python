import json

from classes.Generator import display_segment
from classes.Log import Log
from classes.Web import get_json

old_json = {}


def build(segments, url):
    Log.empty()
    Log.line()
    global old_json

    try:
        api_json = get_json(url)

        if "segments" in api_json.keys():
            a = json.dumps(old_json)
            b = json.dumps(api_json)
            if a != b:
                old_json = api_json
                for segment in api_json["segments"]:
                    if "segment" in segment.keys() and segment["segment"] in segments.keys():
                        display_segment(segment, segments[segment["segment"]])
                    else:
                        Log.log("Segment " + segment["segment"] + " not found.")
            else:
                Log.log("No changes.")
        else:
            Log.log("Segment key doesnt exists...")
    except ValueError:
        Log.log("Oops! We have a problem. Try again...")
