# cs231n-final

## Initial Setup

- cd ./your-base-dir
- git clone https://github.com/Genoc/cs231n-final.git

- virtualenv -p python3 env
- source env/bin/activate
- pip install -r requirements.txt
- pip install http://download.pytorch.org/whl/cu80/torch-0.1.12.post2-cp35-cp35m-linux_x86_64.whl
- pip install kaggle-cli
- pip install torchvision


## Configure kaggle
- kg config -u 'username' -p 'password' -c 'painter-by-numbers'

## Pull the data
- kg download -f 'all_data_info.csv.zip'
- kg download -f 'train_1.zip'
- unzip all_data_info.csv.zip
- unzip train_1.zip


etc etc.

