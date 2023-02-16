import importlib


def get_dataset(config):
    """
    according the config['dataset_class'] to create the dataset

    Args:
        config(ConfigParser): config

    Returns:
        AbstractDataset: the loaded dataset
    """
    try:
        dataset = getattr(importlib.import_module('libcity.data.dataset'),
                          config['dataset_class'])
        return dataset(config)
    except Exception as e:
        print(e)
        raise AttributeError('dataset_class is not found')
