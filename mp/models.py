from django.contrib.auth.models import User
from django.db import models

status_choices = (
        ('Pass', 'Pass'),
        ('Fail', 'Fail'),
        ('In Progress', 'In Progress'),
        )

class board_type(models.Model):
    board_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Board Type'
        verbose_name_plural = 'Board Types'


class board_faults_categories(models.Model):
    board_faults_categories_id = models.AutoField(primary_key=True)
    board_type = models.ForeignKey(board_type, on_delete=models.CASCADE)
    board_issue = models.CharField(max_length=255)

    def __str__(self):
        return self.board_issue

    class Meta:
        verbose_name = 'Board Type Categories'
        verbose_name_plural = 'Board Type Categories'


class board(models.Model):
    board_id = models.AutoField(primary_key=True)
    board_type = models.ForeignKey(board_type, on_delete=models.CASCADE)
    mac_no = models.CharField(max_length=255, default='')
    batch_no = models.CharField(max_length=255, default='')
    serial_number = models.CharField(max_length=255,unique=True, default='')
    status = models.CharField(max_length=200, choices=status_choices,verbose_name='status')

    def __str__(self):
        return self.serial_number

    class Meta:
        verbose_name = 'Board'
        verbose_name_plural = 'Board'


class repair_record(models.Model):
    repair_record_id = models.AutoField(primary_key=True)
    board_serial_number = models.ForeignKey(board, on_delete=models.CASCADE)
    open_date = models.DateField()
    closed_date = models.DateField()
    issue_no = models.CharField(max_length=200)
    fault_local_agent = models.CharField(max_length=200)
    suspect_fault_after_checkup = models.ManyToManyField(board_faults_categories)

    def get_board_issues(self):
        return ",".join([p.board_issue for p in self.suspect_fault_after_checkup.all()])

    class Meta:
        verbose_name = 'Repair Record'
        verbose_name_plural = 'Repair Records'


class repair_record_progress(models.Model):
    board_repair_record_progress_id = models.AutoField(primary_key=True)
    repair_record = models.ForeignKey(repair_record, on_delete=models.CASCADE)
    date = models.DateField()
    staff = models.CharField(max_length=255)
    workdone = models.TextField()

    def __str__(self):
        return self.staff

    class Meta:
        verbose_name = 'Repair records progess'
        verbose_name_plural = 'Repair records progess'
