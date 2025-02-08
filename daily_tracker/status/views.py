



from django.shortcuts import render, redirect
from .models import DailyStatus
from .forms import DailyStatusForm

# Home Page - Form for adding status
def home(request):
    form = DailyStatusForm(request.POST or None, request.FILES or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('view_status')  # Redirect to the view status page

    return render(request, 'status/home.html', {'form': form})

# New Page - Displays submitted details
def view_status(request):
    statuses = DailyStatus.objects.all().order_by('-date')
    return render(request, 'status/view_status.html', {'statuses': statuses})
