from django.db import models
from apps.BookType.models import BookType
from tinymce.models import HTMLField


class Book(models.Model):
    barcode = models.CharField(max_length=20, default='', primary_key=True, verbose_name='商品条形码')
    bookName = models.CharField(max_length=20, default='', verbose_name='商品名称')
    bookTypeObj = models.ForeignKey(BookType,  db_column='bookTypeObj', on_delete=models.CASCADE, verbose_name='商品类别')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品价格')
    count = models.IntegerField(default=0, verbose_name='商品库存')
    publishDate = models.CharField(max_length=20, default='', verbose_name='出版日期')
    publish = models.CharField(max_length=20, default='', verbose_name='出版社')
    bookPhoto = models.ImageField(upload_to="img", max_length='80', verbose_name='商品图片')  #指定文件保存的路径名 系统自动创建
    bookDesc = HTMLField(verbose_name='商品简介')
    bookFile = models.FileField(upload_to='file', max_length='100', verbose_name='商品文件')

    class Meta:
        db_table = 't_Book'
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name

    def getJsonObj(self):
        book = {
            "barcode": self.barcode,
            "bookName": self.bookName,
            'bookTypeObj': self.bookTypeObj.bookTypeName,
            'bookTypeObjPri': self.bookTypeObj.bookTypeId,
            'price': self.price,
            'count': self.count,
            'publishDate': self.publishDate,
            'publish': self.publish,
            'bookPhoto': self.bookPhoto.url,
            'bookDesc': self.bookDesc,
            'bookFile': self.bookFile.url
        }
        return book
