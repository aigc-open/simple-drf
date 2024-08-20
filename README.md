# simple-drf
以最简单的方式运行drf, 方便快速开发

## 使用指南
- 安装
```bash
pip install git+https://github.com/aigc-open/simple-drf.git
```
- 命令解析
```bash
[~]# python3 -m simple_drf.manage --help
Available subcommands:

[auth]
    changepassword
    createsuperuser

[contenttypes]
    remove_stale_contenttypes

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    optimizemigration
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[rest_framework]
    generateschema

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver
```
```bash
python3 -m simple_drf.init init_project # 最小化初始化项目
```

- 启动服务
```bash
python3 -m simple_drf.manage runserver 0.0.0.0:9000
```

```bash
uvicorn simple_drf.default_config.asgi:application --workers 10 --host 0.0.0.0 --port 9000
```

- 接口文档
    - `python3 -m simple_drf.manage collectstatic`
    - `http://127.0.0.1:9000/docs`

