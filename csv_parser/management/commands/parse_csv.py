from django.core.management.base import BaseCommand, CommandError
import csv
from csv_parser.models import Countrydata

class Command(BaseCommand):
	help = "A sample command"


	def handle(self, *args, **options):
		

		ifile  = open('countries.csv', "rb")
		reader = csv.reader(ifile)

		for row in reader:
			c = Countrydata()
			c.sr_no = row[0]
			c.country_name = row[1]
			c.formal_name = row[2]
			c.country_type = row[3]
			c.country_sub_type = row[4]
			c.sovereignty = row[5]
			c.capital = row[6]
			c.currency_code = row[7]
			c.currency_name = row[8]
			c.telephone_code = row[9]
			c.iso_3166_12_letter_code = row[10]
			c.iso_3166_13_letter_code = row[11]
			c.iso_3166_1_number = row[12]
			c.iana_country_code_tld = row[13]
			
			c.save()

		ifile.close()

