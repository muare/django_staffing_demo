from django.db import models
from django.conf import settings
# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=256, blank=False, verbose_name="客户名称")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    modified_date = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "客户"
        verbose_name_plural = "客户"


class Product(models.Model):
    name = models.CharField(max_length=256, blank=False, verbose_name="产品名称")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    modified_date = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "产品"
        verbose_name_plural = "产品"


class Project(models.Model):
    name = models.CharField(max_length=256, blank=False, verbose_name="项目名称")
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='projects', verbose_name="客户")
    product = models.ManyToManyField(
        Product, related_name='projects', verbose_name="产品")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    modified_date = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "项目"
        verbose_name_plural = "项目"


class Team(models.Model):
    name = models.CharField(max_length=256, blank=False, verbose_name="团队名称")
    parent_team = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='sub_teams', verbose_name="上级团队")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    modified_date = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "团队"
        verbose_name_plural = "团队"


class Employee(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="员工")
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='members', verbose_name="团队名称")
    leader = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='subordinates', verbose_name="上级")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "员工"
        verbose_name_plural = "员工"


class Effort(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='efforts', verbose_name="员工")
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='efforts', verbose_name="项目")
    interval = models.DecimalField(
        max_digits=3, decimal_places=1, verbose_name="工时(小时)")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    modified_date = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        verbose_name = "工时"
        verbose_name_plural = "工时"
