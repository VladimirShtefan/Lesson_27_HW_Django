import csv
import os

from django.core.management.base import BaseCommand

from ads.forms import AdsForm
from categories.forms import CategoryForm


class Command(BaseCommand):
    help = "Loads fixtures from fixtures dir"
    filenames = {
        "ads.csv": AdsForm,
        "categories.csv": CategoryForm,
    }

    def handle(self, *args, **options):
        self.prepare()
        self.main()
        self.finalise()

    def prepare(self):
        self.imported_counter = 0
        self.skipped_counter = 0

    def main(self):
        self.stdout.write("Loading fixtures")
        for file, form in self.filenames.items():
            path = os.path.join('fixtures', file)
            with open(path, 'r') as f:
                reader = csv.DictReader(f)
                for index, row_dict in enumerate(reader):
                    current_form = form(data=row_dict)
                    if current_form.is_valid():
                        current_form.save()
                        self.imported_counter += 1
                    else:
                        self.skipped_counter += 1
                        self.stderr.write(f"Errors importing {file}\n"
                                          f"{row_dict}")
                        self.stderr.write(f'{current_form.errors.as_json()}\n')

    def finalise(self):
        self.stdout.write("Finalising fixtures")
        self.stdout.write(f"Imported: {self.imported_counter}\n")
        self.stdout.write(f"Skipped: {self.skipped_counter}\n")








