# devops

该项目基于django开发，面向运维和开发工程师使用。


> 项目访问地址： http://140.143.157.207:7000
> 账号 devops777
> 密码 admin666

# 目标功能


- 支持git版本管理
- 用户分身份注册、登录
- 开发者发起上线任务申请、部署
- 项目管理
- 团队成员管理
- 资产管理
- 任务管理
- 微服务管理
- 文档协作
- git管理

# 开发
1. 安装模块
> pip install -r requirements.txt

2. 生成 requirements

当依赖模块发生变动时

> pip freeze > requirements.txt


3. 为了保证最小的依赖，请为项目使用独立的环境

一种简单的方式是使用 venv, 在 pycharm 新版本中自带对 venv 的支持，如果没使用 pycharm ,可参考
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432712108300322c61f256c74803b43bfd65c6f8d0d0000

4. 邮件通知

    在微服务添加项目以及项目访问失败时，添加邮件通知








