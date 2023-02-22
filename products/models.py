from django.db import models
from django.utils.translation import gettext_lazy as _



class   Category(models.Model):

    parent =\
        models.ForeignKey(
            'self',
            verbose_name=_('parent'),
            blank=True,
            null=True,
            on_delete=models.CASCADE
        )

    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avaatar'), blank=True, upload_to='categories/')
    is_enable = models.BooleanField(_('is_enable'), default=True)
    created_time = models.DateTimeField(_('created_time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated_time'), auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')



class Product(models.Model):

    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    categories = models.ManyToManyField('Category', verbose_name=_('categoris'), blank=True)
    avatar = models.ImageField(_('avaatar'), blank=True, upload_to='products/')
    is_enable = models.BooleanField(_('is_enable'), default=True)
    created_time = models.DateTimeField(_('created_time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated_time'), auto_now=True)

    class Meta:
        db_table = 'Products'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class File(models.Model):

    parent = \
        models.ForeignKey(
            'Product',
            verbose_name=_('product'),
            on_delete=models.CASCADE
        )

    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    file = models.FileField(_('file'), upload_to='files/%y/%m/%d/')
    is_enable = models.BooleanField(_('is_enable'), default=True)
    created_time = models.DateTimeField(_('created_time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated_time'), auto_now=True)

