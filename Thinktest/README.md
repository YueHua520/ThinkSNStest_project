#这个是THinkSNS页面的Web自动化测试

datas是数据文件：
包含了上传文件（upload）,数据驱动测试的各类yaml格式文件

config是配置文件:
用于管理环境变量、全局设置,读取配置文件，如URL、浏览器类型、超时时间等


pages是页面对象文件：
每个页面一个Python文件.
base_page是页面的通用操作方法，blog_page是日志页面功能，photo_page是相册页面功能，
register_page是注册页面，home_page是个人空间主页，login_page是登录界面，


report是生成报告文件：html_reports是生成的HTML格式的报告


screeshot是截图文件：

testcases是测试用例文件：各类测试用例，包含日志发送，注册，登录，相册上传等等用例

testrun是测试执行文件(批量加载、执行测试用用例、生成测试报告文件的脚本)：打包所需的测试用例进行测试