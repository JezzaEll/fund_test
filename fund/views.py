from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from django.db.models import Sum
from .models import Fund
from .forms import FundUploadForm
from csv import DictReader
from io import TextIOWrapper
import csv

class FundListView(View):
    template_name = 'fund/fund_list.html'

    def get(self, request):
        print(type(request))
        strategy = request.GET.get('strategy', '')
        funds = Fund.objects.filter(strategy=strategy) if strategy else Fund.objects.all()
        strategies = Fund.objects.all().order_by('strategy').values_list('strategy', flat=True).distinct()
        total_aum = funds.aggregate(Sum('aum'))
        context = {'funds': funds, 'total_aum': total_aum['aum__sum'], 'strategies': strategies}
        return render(request, self.template_name, context)

class FundUploadView(View):
    template_name = 'fund/fund_upload.html'

    def get(self, request):
        form = FundUploadForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = FundUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file'].read().decode('utf-8-sig').splitlines()
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                # check if fund already exists
                if not Fund.objects.filter(name=row['Name']).exists():
                    # Create new fund
                    fund = Fund.objects.create(
                        name=row['Name'],
                        strategy=row['Strategy'],
                    )
                    if row['AUM (USD)'] != '':
                        fund.aum = int(row['AUM (USD)'])
                    if row['Inception Date'] != '':
                        fund.inception_date = row['Inception Date']
                    fund.save()
                else:
                    # update fund
                    fund = Fund.objects.get(name=row['Name'])

                    if row['AUM (USD)'] != '':
                        fund.aum = int(row['AUM (USD)'])
                    else:
                        fund.aum = None
                    if row['Inception Date'] != '':
                        fund.inception_date = row['Inception Date']
                    fund.save()
            return redirect('fund_list')
        return render(request, self.template_name, {'form': form})

class FundAPIListView(View):
    def get(self, request):
        strategy = request.GET.get('strategy', '')
        funds = Fund.objects.filter(strategy=strategy) if strategy else Fund.objects.all()
        data = [{'id': fund.id, 'name': fund.name, 'strategy': fund.strategy, 'aum': fund.aum} for fund in funds]
        return JsonResponse(data, safe=False)

class FundAPIDetailView(View):
    def get(self, request, fund_id):
        fund = Fund.objects.get(id=fund_id)
        data = {'id': fund.id, 'name': fund.name, 'strategy': fund.strategy, 'aum': fund.aum}
        return JsonResponse(data)
