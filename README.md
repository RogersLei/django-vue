# django-vue
django and vue 

![](https://github.com/RogersLei/django-vue/blob/master/images/index.png)

# Introduction
利用 Vue 和 Django 搭建一个增删改查的Demo

# Dependence

![Depfu](https://img.shields.io/badge/Npm-6.1.0-green.svg)
![Depfu](https://img.shields.io/badge/Node-v8.9.3-green.svg)
![Depfu](https://img.shields.io/badge/Python-2.7.10-green.svg)
![Depfu](https://img.shields.io/badge/Pip-18.0-green.svg)
![Depfu](https://img.shields.io/badge/Django-1.11.15-green.svg)
![Depfu](https://img.shields.io/badge/Vue-2.5.17-green.svg)
![Depfu](https://img.shields.io/badge/elementui-2.4.6-green.svg)
![Depfu](https://img.shields.io/badge/axios-0.18.0-green.svg)

# Deploy

first 
```
git clone git@github.com:RogersLei/django-vue.git

cd django-vue
```

``` Shell

``` Shell
//  frontend/  it's default port is 8080
  cd frontend
  npm install
  npm run dev
```

if you can't make db in your PC, you should config your database first for mysql and name is python_use

then you should do this: 
``` Shell
// it's default port is 8000
  cd django-vue
  python manage.py makemigrations crud
  python manage.py migrate
  python manage.py runserver 8000
```

# Directory Structure
![](https://github.com/RogersLei/django-vue/blob/master/images/dir.png)
