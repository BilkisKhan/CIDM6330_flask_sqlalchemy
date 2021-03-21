import pytest
import requests

import config


from flask_sqlalchemy_tutorial import create_app

app = create_app()


@pytest.fixture
def test_add_bookmark_flask_api(add_stock):

    bookmarkData = BookMarks(
        title='Testing Add Bookmark',
        url='www.bookmarktest.com',
        createdDate=dt.now(),
        notes='My Flask API Add Bookmark test'
    )

   # data = {"orderid": random_orderid(), "sku": sku, "qty": 3}
    url = config.
    print(url)

   # r = requests.post(f"{url}/allocate", json=data)

   # assert r.status_code == 201
   # assert '201' == '201'
   # assert r.json()["batchref"] == earlybatch
