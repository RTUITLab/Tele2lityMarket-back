from urllib.parse import quote_plus as quote

import ssl
import pymongo

url = 'mongodb://{user}:{pw}@{hosts}/?replicaSet={rs}&authSource={auth_src}'.format(
    user=quote('user1'),
    pw=quote('realityTele2lity'),
    hosts=','.join([
        'rc1c-tplly2g13saa2p6m.mdb.yandexcloud.net:27018'
    ]),
    rs='rs01',
    auth_src='db1')
dbs = pymongo.MongoClient(
    url,
    ssl_ca_certs='/usr/local/share/ca-certificates/Yandex/YandexInternalRootCA.crt',
    ssl_cert_reqs=ssl.CERT_REQUIRED)['db1']

# dbs.test_collection.find(...)