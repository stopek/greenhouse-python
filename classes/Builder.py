import json

from classes.Generator import display_segment
from classes.Web import get_json

old_json = {}


def build(segments, url):
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
                    # else:
                    #     print("Segment ", segment["segment"], " not found!")
            # else:
            #     print("No changes.")
        # else:
        #     print("Segment key doesnt exists...")
    except ValueError:
        print("Oops! We have a problem. Try again...")
