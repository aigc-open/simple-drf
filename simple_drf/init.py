import os
import sys
from django.conf import settings
from django.core.wsgi import get_wsgi_application
import os
from fire import Fire

def set_settings():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", os.environ.get("DJANGO_SETTINGS_MODULE", "config.settings"))

default_settings = """
from simple_drf.default_config.settings import *
# 请添加或者覆盖
# INSTALLED_APPS.extend(["demo_api"])
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = 'simple_drf.default_config.wsgi.application'

"""

default_urls = '''
"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers

urlpatterns = [
    path('admin/', admin.site.urls),
]
router = routers.DefaultRouter()

# 请添加路由
# from demo_api.views import CategoryViewSet, EventViewSet
# router.register(r'category', CategoryViewSet)

# urlpatterns.append(path('', include(router.urls)),)
urlpatterns.append(path('docs/', include_docs_urls(title='站点页面标题', authentication_classes=[])))

'''

default_requirements = """
djangorestframework==3.15.1
Django==4.2.11
uvicorn==0.29.0
django-filter==24.2
drf-spectacular==0.27.2
coreapi==2.3.3
"""

default_dockerfile = """
FROM python:3.9-buster

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

COPY . /workspace

WORKDIR /workspace

CMD "uvicorn simple_drf.default_config.asgi:application --workers 10 --host 0.0.0.0 --port 8000"

"""

def init_project():
    os.makedirs("config", exist_ok=True)
    if os.path.exists("config/settings.py"):
        print("config/settings.py 已经存在，跳过初始化")
    else:
        with open("config/settings.py", "w") as f:
            f.write(default_settings)

        with open("config/__init__.py", "w") as f:
            f.write("")

        with open("config/urls.py", "w") as f:
            f.write(default_urls)
    if os.path.exists("requirements.txt"):
        print("requirements.txt 已经存在，跳过初始化")
    else:
        print("初始化 requirements.txt")
        with open("requirements.txt", "w") as f:
            f.write(default_requirements)

    with open("Dockerfile", "w") as f:
        f.write(default_dockerfile)

if __name__ == '__main__':
    Fire()