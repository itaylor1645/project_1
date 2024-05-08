"""Use opendatasets to download the CSVs for metal futures from Kaggle.

opendatasets will need to be installed:
```shell
pip install opendatasets --upgrade
```

Running will ask for your Kaggle API credentials (username, key). Learn more at
http://bit.ly/kaggle-creds
"""

import opendatasets

if __name__ == "__main__":
    dataset = "https://www.kaggle.com/datasets/guillemservera/precious-metals-data"
    target_dir = "."
    opendatasets.download(dataset, target_dir)
