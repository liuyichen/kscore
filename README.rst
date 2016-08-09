kscore
========

A low-level interface to a growing number of KSC Web Services. Reference from botocore.

`Documentation <http://www.ksyun.com/doc/search?word=API>`__

----------------
Credentials 配置
----------------

+ 参考examples内示例
  + config file: ``.kscore.cfg``

::

  [Credentials]
  aws_access_key_id=AKLTyW1V6ZWET7aIvdCeIH1cwQ
  aws_secret_access_key=OEoTK4IgEBIq3rlFsbpcNDs87w513D6aOwdXxP6QHuvWlonSRYeKQyTzqc1XkUvpuQ==


+ 或运行时配置
  + session.set_credentials(access_key_id, secret_access_key, session_token=None)

----------------
Service 使用
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

+ 更多

::

    欢迎补充

------------------
Data 更多服务配置
------------------

+ ENDPOINT 配置
  + data\endpoints.yaml

::

    version: n
    partitions:
    - partition:
      ...
      # REGION 列表
      regions:
        ...
    # 服务列表
    - service:
      ...

+
  + data\[service]\[version]\service-2.yaml

::

    version: n
    # API 配置
    metadata:
      ...
    # 操作方法
    operations:
      ...
    # 请求及返回的结构体
    shapes:
      ...

+ 请参考IAM,KEC等配置

--------------------
Contact Information
--------------------

群   号: 367780788
邮   箱: liuyc.mail@gmail.com
