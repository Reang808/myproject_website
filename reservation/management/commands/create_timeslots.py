from django.core.management.base import BaseCommand
from reservation.models import TimeSlot
from datetime import datetime, timedelta, time

class Command(BaseCommand):
	help = '1ヶ月分のTimeSlot（10:00～22:00）を全日付で一括作成します'

	def handle(self, *args, **options):
		today = datetime.today().date()
		for day_offset in range(0, 31):
			d = today + timedelta(days=day_offset)
			for h in range(10, 23):
				t = time(hour=h, minute=0)
				TimeSlot.objects.get_or_create(date=d, time=t)
		self.stdout.write(self.style.SUCCESS('1ヶ月分のTimeSlotを作成しました'))
