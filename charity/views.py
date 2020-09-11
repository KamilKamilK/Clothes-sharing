from django.core.paginator import Paginator
from django.db.models import Sum
from django.shortcuts import render
from django.views import View

from charity.models import Donation, Institution


class LandingPageView(View):
    def get(self, request):
        fundations = Institution.objects.filter(type=Institution.FUNDATION)

        # list = []
        # instit = Institution.objects.institution
        # if instit is not None:
        #     list.append(instit)

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
            # 'list': Institution.objects.filter(isnull=True),
            'donations': Donation.objects.all(),
            'quantity': Donation.objects.aggregate(Sum('quantity')),
            'fundations': fundations,
            'organizations': Institution.objects.filter(type=Institution.ORGANIZATION),
            'collections': Institution.objects.filter(type=Institution.COLLECTION),
        }
        return render(request, 'index.html', ctx)


class AddDonationView(View):
    def get(self, request):
        ctx = {
            'donations': Donation.objects.all()
        }
        return render(request, 'form.html', ctx)




