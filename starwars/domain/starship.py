class Starship:
    def __init__(self, code, name, hyperdrive_rating):
        self.code = code
        self.name = name
        self.hyperdrive_rating = hyperdrive_rating

    @classmethod
    def from_dict(cls, adict):
        return cls(
            code=adict['code'],
            name=adict['name'],
            hyperdrive_rating=adict['hyperdrive_rating']
        )

    def to_dict(self):
        return {
            'code': self.code,
            'name': self.name,
            'hyperdrive_rating': self.hyperdrive_rating
        }
