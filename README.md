# MyImageDownloader

## Configuration
make config file as name `config.json`
example `config.json`
```
{
  "url": "http://...",
  "auth": {
    "user": "userid",
    "pass": "12345"
  },
  "directory": "image"
}
```

## Execution
```
$ python download_image.py -c path_to_config.json
```

`-c`, `--config` argument path to config.json