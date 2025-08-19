from django.db import models

class Reservation(models.Model):
    name = models.CharField('お名前', max_length=50)
    email = models.EmailField('メールアドレス')
    date = models.DateField('予約日')
    time = models.TimeField('予約時間')
    message = models.TextField('ご要望・メッセージ', blank=True)
    created_at = models.DateTimeField('予約日時', auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"

class TimeSlot(models.Model):
    date = models.DateField()
    time = models.TimeField()
    is_booked = models.BooleanField(default=False)  # 管理者が埋める or 自動で予約済みにする

    def __str__(self):
        status = "予約済み" if self.is_booked else ""
        return f"{self.date} {self.time} ({status})"