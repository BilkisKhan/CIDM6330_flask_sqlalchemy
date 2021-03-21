import pytest
import requests

# import config

import config
from flask_sqlalchemy_tutorial import create_app


@pytest.fixture
def client():
    app = create_app()
    app.run(host='127.0.0.1', port=5000)


def test_add_bookmark_flask_api():

    # bookmarkData = BookMarks(
    #     title='Testing Add Bookmark',
    #     url='www.bookmarktest.com',
    #     createdDate=dt.now(),
    #     notes='My Flask API Add Bookmark test'
    # )

   # data = {"orderid": random_orderid(), "sku": sku, "qty": 3}
   # url = config.get_api_url()
    # app = create_app()
    # app.run(host="127.0.0.1", port=5000)
    # url = config.Config.get_api_url()
    # print(url)

    # r = requests.post(f"{url}/?title='test&email='rrrrr'", json=data)
    r = requests.get('http://127.0.0.1:5000/')

    assert r.status_code == 201
   # assert '201' == '201'
   # assert r.json()["batchref"] == earlybatch
