from django.shortcuts import render, redirect
from .forms import CustomerForm

def customer_form(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = CustomerForm()

    return render(request, 'customer_form.html', {'form': form})

def thank_you(request):
    return render(request, 'thank_you.html')
