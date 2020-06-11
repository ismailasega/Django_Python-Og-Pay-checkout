from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import CheckoutForm


class CheckoutView(View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        context = {
            'form': form
        }
        return render(self.request, 'checkout.html', context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.Post or None)
        if form.is_valid():
            print("hi asega")
            return redirect('ogcheckout:checkout')