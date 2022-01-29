from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from landing.forms import UserUpdateForm, ProfileUpdateForm


@login_required
def home(request):
    return render(request, 'mandaread/home.html')


@login_required
def updateProfile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request, f'Success. Your profile has been updated!')
            return redirect('mandaread-edit-profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm()

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'mandaread/update-profile.html', context)


@login_required
def updatePass(request):
    return render(request, 'mandaread/update-pass.html')


@login_required
def deleteAccount(request):
    return render(request, 'mandaread/delete-acc-prompt.html')


@login_required
def accountDelete(request):
    try:
        u = User.objects.get(id=request.user.id)
        u.delete()
        messages.warning(
            request, f'Your account has been deleted. It\'s sad to see you leave.')
    except User.DoesNotExist:
        messages.error(request, f'This user does not exist')

    return redirect('landing-login')


######## CLASS BASED VIEWS ########

class NewPasswordChangeView(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    success_message = "Your password was updated successfully!"
    success_url = reverse_lazy('mandaread-edit-profile')