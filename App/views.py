from django.shortcuts import render
from datetime import datetime

def home(request):
    context = {}
    current_time = datetime.today().strftime("%I:%M %p")
    current_time = current_time.split(' ')
    
    if current_time[-1] == 'PM':
        if int(current_time[0].split(':')[0]) > 6:
            context['data'] = 'Good Evening'
        else:
            context['data'] = 'Good Afternoon'
    else:
        context['data'] = 'Good morning'

    return render(request, 'index.html', context)
