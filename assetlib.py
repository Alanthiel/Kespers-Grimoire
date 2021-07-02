# Todo: Implement Asset Skeletal Structure:
#       Asset Needed: Maps, Events, DM Ideas, Characters, Notes, Images Repository
# Todo: Implement as Data Class
# Note: Asset

from dataclasses import dataclass
from dataclasses import asdict
import appdirs


@dataclass
class Config:
    config_loc = (appdirs.user_config_dir() + "/kespersgrimoire")  # noqa
    tag_type: str


@dataclass
class AssetType:
    typecount = 0
    definition: str

    def __init__(self, definition):
        self.id = AssetType.typecount + 1
        self.definition = definition
        AssetType.typecount += 1


@dataclass
class Asset:
    maxid = 0
    tags: list
    id: int
    type: AssetType

    def __init__(self, tags, type):
        self.tags = tags
        self.type = type
        self.id = Asset.maxid + 1
        Asset.maxid += 1


# Predefined Asset Types
@dataclass(frozen=True)
class PredefinedAssets:
    Maps = AssetType(definition='Predefined')
    Dm_ideas = AssetType(definition='Predefined')
    Characters = AssetType(definition='Predefined')
    Events = AssetType(definition='Predefined')
    Plots = AssetType(definition='Predefined')
    Notes = AssetType(definition='Predefined')


def main():
    # testing profile:
    Config.config_loc = "./local/"
    snapshot = asdict(Config('FileBased'))
    pass


if __name__ == "__main__":
    main()
