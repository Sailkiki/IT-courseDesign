from apps.Book.views import FrontAddView, FrontListView, UpdateView, DeletesView, FrontShowView, AddView, \
    ListView, OutToExcelView, BackModifyView, FrontModifyView
from django.conf.urls import url

# 正在部署的应用的名称
app_name = 'Book'

urlpatterns = [
    url(r'^frontAdd$', FrontAddView.as_view(), name='frontAdd'),  # 前台商品添加
    url(r'^frontModify/(?P<barcode>.+)$', FrontModifyView.as_view(), name='frontModify'),  # 前台更新商品
    url(r'^frontList$', FrontListView.as_view(), name='frontList'),  # 前台商品查询列表
    url(r'^frontShow/(?P<barcode>.+)$', FrontShowView.as_view(), name='frontShow'),  # 前台显示图片详情页

    url(r'^update/(?P<barcode>.+)$', UpdateView.as_view(), name='update'),  # Ajax方式商品更新

    url(r'^add$', AddView.as_view(), name='add'),  # 后台添加商品
    url(r'^backModify/(?P<barcode>.+)$', BackModifyView.as_view(), name="backModify"),  # 后台更新商品
    url(r'^list$', ListView.as_view(), name='list'),  # 后台商品列表
    url(r'^deletes$', DeletesView.as_view(), name="deletes"),  # 删除商品信息
    url(r'^OutToExcel$', OutToExcelView.as_view(), name='OutToExcel')  # 导出商品信息到excel并下载
]
