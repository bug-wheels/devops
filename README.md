# devops
自动化运维工具

该项目基于django开发，面向运维和开发工程师使用。

# 暂时完成功能


# 目标功能
1. 微服务监控
1. 持续集成
1. 项目上线
1. 资产管理
1. WEBSSH

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








