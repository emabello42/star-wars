import json


class StartshipJsonEncoder(json.JSONEncoder):

    def default(self, o):
        try:
            to_serialize = {
                'code': str(o.code),
                'name': o.name,
                'hyperdrive_rating': o.hyperdrive_rating
            }
            return to_serialize
        except AttributeError:
            return super().default(o)