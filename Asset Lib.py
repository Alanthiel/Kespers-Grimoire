# Todo: Implement Asset Skeletal Structure:
#       Asset Needed: Maps, Events, DM Ideas, Characters, Notes, Images Repository
# Todo: Implement as Data Class
# Note: Asset

from dataclasses import dataclass


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


# Predefined Asset Types
Maps = AssetType(definition='Predefined')
Dm_ideas = AssetType(definition='Predefined')
Characters = AssetType(definition='Predefined')
Events = AssetType(definition='Predefined')
Plots = AssetType(definition='Predefined')


def main():
    print(AssetType.typecount)
    pass


if __name__ == "__main__":
    main()
