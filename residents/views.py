
# Create your views here.
from django.shortcuts import render
from .models import Resident
from collections import defaultdict
from django.db.models import Count


def reports_home(request):
    return render(request, 'residents/reports_home.html')


def voters_precinct_dashboard(request):
    data = (
        Resident.objects
        .filter(
            voters_id__gt='',
            precinct_number__gt='',
            is_active=True
        )
        .values('precinct_number')
        .annotate(total=Count('id'))
        .order_by('precinct_number')
    )

    labels = [item['precinct_number'] for item in data]
    totals = [item['total'] for item in data]

    return render(request, 'residents/voters_precinct_dashboard.html', {
        'labels': labels,
        'totals': totals,
        'data': data
    })

def voters_report(request):
    voters = Resident.objects.exclude(voters_id='').exclude(voters_id__isnull=True)
    return render(request, 'residents/voters_report.html', {
        'voters': voters
    })

def voters_by_precinct_report(request):
    voters = Resident.objects.filter(
        voters_id__gt='',
        precinct_number__gt='',
        is_active=True
    ).order_by('precinct_number', 'last_name', 'first_name')

    precincts = defaultdict(list)

    for voter in voters:
        precincts[voter.precinct_number].append(voter)

    return render(request, 'residents/voters_by_precinct.html', {
        'precincts': dict(precincts)
    })



def voters_report(request):
    voters = Resident.objects.filter(
        voters_id__gt='',
        precinct_number__gt='',
        is_active=True
    ).order_by('precinct_number', 'last_name', 'first_name')

    return render(request, 'residents/voters_report.html', {
        'voters': voters
    })
