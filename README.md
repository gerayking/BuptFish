### 北邮二手交易平台
#### 已完成工作情况
+ 数据库表创建
#### 第一阶段内容
`负责人认领后在后面写上完成情况`
+ 买家卖家登录
+ 个人信息维护
+ 搜索物品和用户
+ 用户主页
#### 第二阶段
+ 物品发布
+ 浏览物品列表
+ 浏览物品详情
+ 物品下单

### Start
先删除原先的数据库schema
```
mysql -u root -p
drop database BuptFish
```
删除User migration文件下的所有文件
然后开始迁移
```
python manage.py makemigration
pytho manage.py migratate
```
上述命令报错没有django有可能是因为电脑安装了多个python,
pycharm选择的和环境变量中不一样,可以直接从Tools, Run manaky.py Task中输入.
```
makemigration
migratate
```
开发阶段移除了所有外键,为了便于各个开发人员进行不同模块的测试
### 规范
 + **驼峰命名**

### Push
push的过程中不要带上
+ .idea/
+ __pycache__/  
这些是pycharm在生成项目过程的中间文件,存储起来是为了下次编译