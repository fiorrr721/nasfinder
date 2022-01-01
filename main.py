#!/usr/bin/env python3

import os
import random
from flask import Flask, render_template, request
import configparser
import glob


app = Flask(__name__)
config = configparser.ConfigParser()
config.read("config.ini")

localpathsep = '/'
smbpathsep = '\\'

# URLパラメータ
# http://localhost:8000/test2?path=hoge


@app.route("/")
def test2():
    keyword = request.args.get('q', default=None, type=str)
    result = []
    for key in config.sections():
        pathroot = config[key]['localpath']
        files = glob.glob(f"{pathroot}/**/*{keyword}*.*", recursive=True)
        for f in files:
            if os.path.isdir(f):
                continue
            f = f.replace(config[key]['localpath'], config[key]['smbpath'])
            f = f.replace(localpathsep, smbpathsep)
            result.append(f)
    return render_template('top.html', paths=result, q=keyword)


# おまじない
if __name__ == "__main__":
    app.run(debug=True)
