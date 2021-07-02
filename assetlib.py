# Todo: Implement Asset Management Systems
# Note: Asset

from dataclasses import dataclass
from dataclasses import asdict # noqa
import appdirs


@dataclass
class Config:
    config_loc = appdirs.user_config_dir(appname='kespersgrimoire')  # noqa
    tag_type: str


@dataclass
class AssetBase:
    tags: list
    asset_id: str
    asset_count: int = 0
    notes: list = None

    def __init__(self, tags=None, notes=None):
        self.notes = notes
        self.tags = tags


@dataclass
class Map(AssetBase):
    location: str = None
    point_of_interest: list = None
    map_features: list = None

    def __init__(self, tags=None, notes=None, location=None, points_of_interest=None, map_features=None):
        super().__init__(tags, notes)
        self.location = location
        self.point_of_interest = points_of_interest
        self.map_features = map_features
        self.asset_id = '{}_map'.format(AssetBase.asset_count + 1)
        AssetBase.asset_count += 1


@dataclass
class Character(AssetBase):

    def __init__(self, tags=None, notes=None):
        super().__init__(tags, notes)
        self.asset_id = '{}_cha'.format(AssetBase.asset_count + 1)
        AssetBase.asset_count += 1


def main():
    # testing profile:
    # Config.config_loc = "./local/"
    print(Config.config_loc)
    pass


if __name__ == "__main__":
    main()
