from django.core.paginator import Paginator
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import FormView

from charity.forms import CategoryForm, AjaxForm
from charity.models import Donation, Institution, Category


class LandingPageView(View):
    def get(self, request, *args, **kwargs):
        fundations = Institution.objects.filter(type=Institution.FUNDATION)

        # list = []
        # instit = Institution.objects.all()
        # if instit is not None:
        #     list.append(instit)
        #
        # paginator = Paginator(fundations,5)
        # try:
        #     page = int(request.GET.get("page", "1"))
        # except:
        #     page = 1
        #
        # try:
        #     posts = paginator.page(page)
        # except Exception:
        #     posts = paginator.page(paginator.num_pages)

        ctx = {
            # 'posts': posts,
            'list': Institution.objects.filter(dotations__isnull=False),
            'donations': Donation.objects.all(),
            'quantity': Donation.objects.aggregate(Sum('quantity')),
            'fundations': fundations,
            'organizations': Institution.objects.filter(type=Institution.ORGANIZATION),
            'collections': Institution.objects.filter(type=Institution.COLLECTION),
        }
        return render(request, 'index.html', ctx)


class AddDonationView(View):
    def get(self, request, *args, **kwargs):
        form_class = CategoryForm

        ctx = {
            'donations': Donation.objects.all(),
            'categories': Category.objects.all(),
            'institutions': Institution.objects.all(),
            'form_category': form_class,
        }
        return render(request, 'form.html', ctx)

    def post(self, request, *args, **kwargs):
        form_category = CategoryForm(request.POST)
        if form_category.is_valid():
            form_category.save()
            name = form_category.cleaned_data.get('name')

        return render(request, 'form.html', {'form_category': form_category})


class AjaxView(FormView):
    form_class = AjaxForm
    template = "ajax.html"

    def get(self, *args, **kwargs):
        form = self.form_class()
        donations = Donation.objects.all()
        return render(self.request, self.template_name, {"form": form, "donations": donations})

    def post(self, *args, **kwargs):
        if self.request.is_ajax():
            form = self.form_class(self.request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({}, status=200)
            return JsonResponse({}, status=400)
        return JsonResponse({}, status=400)
