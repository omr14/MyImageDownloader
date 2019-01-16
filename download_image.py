import requests
import datetime
import json
import os
import argparse

def download_image(url, auth=None):
    """
    urlに存在する画像を取得する
    arguments
        url: アクセス先URL
        auth: 認証情報タプル('user', 'password')
    return
        画像のバイナリデータ
    """
    
    # リクエストを送る
    if auth:
        res = requests.get(url, auth=auth)
    else:
        res = requests.get(url)
    
    # 失敗した場合を検出
    if res.status_code != 200:
        raise RuntimeError("HTTP Request Returns StatusCode " + str(res.status_code))
    elif 'image' not in res.headers["content-type"]:
        raise RuntimeError("HTTP Request Returns Bad Content-Type " + res.headers["content-type"])
    
    return res.content


def save_binary(binary, path):
    """
    バイナリデータの画像を保存する
    """
    with open(path, "wb") as imgfile:
        imgfile.write(binary)


def make_filepath(root_dir):
    """
    ファイルの保存先を返す、root_dirで保存先のディレクトリを指定する
    """
    if not os.path.exists(root_dir):
        os.mkdir(root_dir)

    today = datetime.datetime.today()
    path = root_dir + today.strftime("/%Y%m%d%H%M.png")
    return path

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
            prog="download_image.py",
            usage="to download image from url"
            )
    parser.add_argument('-c', '--config', help='path to config.json',
                        type=str, required=True)
    args = parser.parse_args()

    _f = open(args.config)
    config = json.load(_f)    
    _f.close()

    print("Fetch from: " + config["url"])

    auth = (config["auth"]["user"], config["auth"]["pass"])
    binary = download_image(config["url"], auth)

    image_root = config["directory"]
    path = make_filepath(image_root)

    print("Image saved: " + path)

    save_binary(binary, path)
