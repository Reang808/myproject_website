document.addEventListener('DOMContentLoaded', function() {
  const calendarEl = document.getElementById('calendar');
  const timeSelect = document.getElementById('id_time');
  const availableTimesDiv = document.getElementById('available-times');
  const calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'dayGridMonth',
    locale: 'ja',
    events: '/reservation/api/timeslot-events/',
    dateClick: function(info) {
      const dateStr = info.dateStr;
      document.getElementById('id_date').value = dateStr;
      // 空き時間取得
      fetch(`/reservation/api/available-timeslots/?date=${dateStr}`)
        .then(res => res.json())
        .then(data => {
          availableTimesDiv.innerHTML = '';
          if (data.times && data.times.length > 0) {
            const label = document.createElement('div');
            label.textContent = '予約可能な時間:';
            label.style.marginBottom = '8px';
            availableTimesDiv.appendChild(label);
            data.times.forEach(function(time) {
              const btn = document.createElement('button');
              btn.type = 'button';
              btn.textContent = time;
              btn.className = 'time-btn';
              btn.style.margin = '0 8px 8px 0';
              btn.style.padding = '6px 16px';
              btn.style.borderRadius = '4px';
              btn.style.border = '1px solid #4CAF50';
              btn.style.background = '#fff';
              btn.style.color = '#4CAF50';
              btn.style.cursor = 'pointer';
              btn.onclick = function() {
                timeSelect.value = time;
                document.getElementById('id_date').value = dateStr;
                // 選択中ボタンの色変更
                Array.from(availableTimesDiv.querySelectorAll('button')).forEach(b => b.style.background = '#fff');
                btn.style.background = '#4CAF50';
                btn.style.color = '#fff';
              };
              availableTimesDiv.appendChild(btn);
            });
          } else {
            availableTimesDiv.textContent = '空き時間なし';
          }
        });
    }
  });
  calendar.render();
});