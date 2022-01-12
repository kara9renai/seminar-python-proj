# seminar-python-proj
## Set up by using docker
```
mkdir hogehoge && cd hogehoge
git clone https://github.com/kara9renai/seminar-python-proj.git
cd seminar-python-proj
docker compose up -d
```

## How to run python file.
```{python}
make container
# inside container
cd src
python3 year_dendrogram.py
# If you want to go out of the container, run this command.
exit
#outside the container
```