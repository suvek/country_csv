from django.shortcuts import render
from django.http import HttpResponse

from csv_parser.models import Countrydata


def home(request):
	"""
	Home page view.
	"""

	countries = Countrydata.objects.all()
	return render(request,"home.html", {'countries':countries})


def countrydetails(request):
	"""
	Country details page view.
	"""

	passed_id = request.GET["id"]
	country_detail = Countrydata.objects.get(pk = passed_id)
	return render(request,"country_details.html", {'country_detail':country_detail})