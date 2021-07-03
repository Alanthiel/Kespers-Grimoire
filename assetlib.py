# Todo: Implement Asset Management Systems
# Todo: Separate Config Script

from dataclasses import dataclass


@dataclass
class Config:
    app_dir = "./local"
    config_loc = "{}/config.json".format(app_dir)
    tag_type: str


@dataclass
class AssetBase:
    tags: list
    asset_id: str
    asset_count: int = 0
    notes: list = None
    definition = 'Undeclared'

    def __init__(self, tags=None, notes=None):
        self.notes = notes
        self.tags = tags


@dataclass
class Map(AssetBase):
    location: str = None
    point_of_interest: list = None
    map_features: list = None
    asset_type = "Map"
    definition = 'Predefined'

    def __init__(self, tags=None, notes=None, location=None, points_of_interest=None, map_features=None):
        super().__init__(tags, notes)
        self.location = location
        self.point_of_interest = points_of_interest
        self.map_features = map_features
        self.asset_id = '{}_map'.format(AssetBase.asset_count + 1)
        AssetBase.asset_count += 1


@dataclass
class Character(AssetBase):
    asset_type = "Character"
    definition = 'Predefined'

    def __init__(self, tags=None, notes=None):
        super().__init__(tags, notes)
        self.asset_id = '{}_cha'.format(AssetBase.asset_count + 1)
        AssetBase.asset_count += 1


# Asset Management System


def main():
    pass


if __name__ == "__main__":
    main()
