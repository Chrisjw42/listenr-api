import json

def analyse_sample(audio_sample):
    with open("dummy_result.json") as fp:
        abc = json.loads(fp.read())
        ret = json.dumps(abc)
        return ret