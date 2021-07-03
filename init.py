from assetlib import Config
from assetlib import AssetBase
import os


def make_asset_dir():
    asset_types = [i.asset_type for i in AssetBase.__subclasses__()]
    data_dir = "{}/assets".format(Config.app_dir)
    list_of_dir = os.listdir(data_dir)
    if not set(asset_types).issubset(set(list_of_dir)):
        for i in asset_types:
            os.mkdir(path="{}/{}".format(data_dir, i), mode=0o755)
    return asset_types


def make_config():
    with open(Config.config_loc, 'w') as config:
        config.write('''{
                "Version":"0.0.1b"
            }''')


def main():
    make_asset_dir()


if __name__ == '__main__':
    main()