from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from aplicatie1.views import LocationView, CreateLocationView
from aplicatie2.models import Company, AuditCompany


# Create your views here.

class CompanyView(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'aplicatie2/company_index.html'
    paginate_by = 5
    queryset = model.objects.all().order_by('id')

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data()
        data['page'] = self.request.GET.get('page') if self.request.GET.get('page') else 1
        return data


class CreateCompanyView(LoginRequiredMixin, CreateView):
    model = Company
    fields = ['name', 'website', 'location']
    template_name = 'aplicatie2/company_form.html'

    def get_success_url(self):
        return reverse('companies:lista_companii')


class UpdateCompanyView(LoginRequiredMixin, UpdateView):
    model = Company
    fields = ['name', 'website', 'location']
    template_name = 'aplicatie2/company_form.html'

    def get_success_url(self):
        return reverse('companies:lista_companii')


@login_required
def delete_company(request, pk):
    company_value = Company.objects.get(id=pk)
    AuditCompany.objects.create(location_id=company_value.location.id,
                                city=company_value.location.city,
                                country=company_value.location.country,
                                name=company_value.name,
                                website=company_value.website,
                                active=company_value.location.active,
                                user_id=request.user.id)
    Company.objects.filter(id=pk).delete()
    return redirect(f'/companies/?page={request.GET.get("page")}')


@login_required
def deactivate_company(request, pk):
    # company_value = Company.objects.filter(id=pk)
    # company_value.update(active=1)
    Company.objects.filter(id=pk).update(active=0)
    return redirect(f'/companies/?page={request.GET.get("page")}')


@login_required
def activate_company(request, pk):
    Company.objects.filter(id=pk).update(active=1)
    return redirect(f'/companies/?page={request.GET.get("page")}')