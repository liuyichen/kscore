SDK 使用文档
========

A low-level interface to a growing number of KSC Web Services.

`Documentation <http://www.ksyun.com/doc/search?word=API>`__

----------------
Install 安装
----------------

+ pip 安装
    + pip install kscore
+ github 安装
    + https://github.com/liuyichen/kscore 下载
    + python setup.py install

----------------
Config 配置
----------------

+ 通过文件配置，参考examples内示例

    + 所在位置: '/etc/kscore.cfg' 或 './.kscore.cfg' 或 'C:\\kscore.cfg'

    + 注意: 使用相对路径时，需与运行目录保持一致。
::

    [Credentials]
    ks_access_key_id=AKLTyW1V6ZWET7aIvdeeIH1cwQ
    ks_secret_access_key=OEoTK4IgEBIq3rlFsbpcESs87w513D6aOwdXxP6QHuvWlonSRYeKQyTzqc1XkUvpuQ==

+ 或运行时配置，

::

    from kscore.session import get_session
    ACCESS_KEY_ID = "AKLTyW1V6ZWET7aIvdeeIH1cwQ"
    SECRET_ACCESS_KEY = "OEoTK4IgEBIq3rlFsbpcESs87w513D6aOwdXxP6QHuvWlonSRYeKQyTzqc1XkUvpuQ=="
    s = get_session()
    client = s.create_client("iam", ks_access_key_id=ACCESS_KEY_ID, ks_secret_access_key=SECRET_ACCESS_KEY)

----------------
Service 服务
----------------

+ 已支持大区 region_name

    +-------------------+------------+
    | region_name       | 大区       |
    +===================+============+
    | cn-beijing-5      | 北京5区    |
    +-------------------+------------+
    | cn-beijing-6      | 北京6区    |
    +-------------------+------------+
    | cn-shanghai-2     | 上海2区    |
    +-------------------+------------+

+ 服务列表 service_name， 详情参考API手册
    +-------------------+------------+
    | service_name      | 服务名     |
    +===================+============+
    | iam               |            |
    +-------------------+------------+
    | eip               |            |
    +-------------------+------------+
    | kec               |            |
    +-------------------+------------+
    | slb               |            |
    +-------------------+------------+
    | vpc               |            |
    +-------------------+------------+
    | monitor           |            |
    +-------------------+------------+

----------------
Method 方法
----------------

+ 常用方法

    + get_session

    +---------------------------+---------------------------------------+
    | 参数                       | 说明                                 |
    +===========================+=======================================+
    | env_vars                  | 环境变量                              |
    +---------------------------+---------------------------------------+

    + create_client

    +---------------------------+---------------------------------------+
    | 参数                       | 说明                                 |
    +===========================+=======================================+
    | service_name              | 服务，必须参数，例：iam               |
    +---------------------------+---------------------------------------+
    | region_name=None          | 大区，必须参数，全局服务可以为None    |
    +---------------------------+---------------------------------------+
    | api_version=None          | API 版本，默认使用最近版本            |
    +---------------------------+---------------------------------------+
    | use_ssl=True              | 是否使用HTTPS，优先使用               |
    +---------------------------+---------------------------------------+
    | verify=None               | 是否验证SSL证书                       |
    +---------------------------+---------------------------------------+
    | endpoint_url=None         |                                       |
    +---------------------------+---------------------------------------+
    | ks_access_key_id=None     |                                       |
    +---------------------------+---------------------------------------+
    | ks_secret_access_key=None |                                       |
    +---------------------------+---------------------------------------+
    | ks_session_token=None     |                                       |
    +---------------------------+---------------------------------------+


----------------
Examples 示例
----------------

+ IAM

::

    from kscore.session import get_session

    if __name__ == "__main__":
        s = get_session()

        client = s.create_client("iam", use_ssl=False)

        users = client.list_users()

+ KEC

::

    from kscore.session import get_session

    if __name__ == "__main__":
        s = get_session()

        client = s.create_client("kec", "cn-beijing-6", use_ssl=False)

        client.[your method]()

+ MONITOR

::

    from kscore.session import get_session

    if __name__ == "__main__":
        s = get_session()

        client = s.create_client("monitor", "cn-beijing-5", use_ssl=True)

        m=client.get_metric_statistics(InstanceID="6f582c78-5d49-438e-bf2d-db4345daf503",Namespace="eip",MetricName="qos.bps_in",StartTime="2016-08-16T17:09:00Z",EndTime="2016-08-16T23:56:00Z",Period="600",Aggregate="Average")

        print json.dumps(m,sort_keys=True,indent=4)

+ 更多

--------------------
TESTS 测试
--------------------

+ 基本接口测试

\tests\acceptance> behave

+ 各服务测试用例

\tests>nosetests --with-xunit --cover-erase --with-coverage --cover-package kscore --cover-xml -v integration

--------------------
Contact Information
--------------------

服 务 群 号: 580681922
