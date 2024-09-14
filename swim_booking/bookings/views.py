from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Class, Parent, Child, Booking
from .forms import UserRegistrationForm, ChildForm, BookingForm

# Register View
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            Parent.objects.create(user=user, name=user.username)
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'bookings/register.html', {'user_form': user_form})

# Booking View
@login_required
def book_class(request):
    parent = Parent.objects.get(user=request.user)
    children = Child.objects.filter(parent=parent)
    swim_classes = Class.objects.all()
    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.save()
            # Redirect to payment gateway (not implemented here)
            return redirect('payment')
    else:
        booking_form = BookingForm()
    return render(request, 'bookings/book_class.html', {
        'children': children,
        'swim_classes': swim_classes,
        'booking_form': booking_form,
    })

# Admin functionality
@login_required
def admin_cancel_class(request, class_id):
    if request.user.is_superuser:
        swim_class = Class.objects.get(id=class_id)
        swim_class.delete()
    return redirect('admin_dashboard')
