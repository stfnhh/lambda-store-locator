from chalice import Chalice
from chalicelib.models import Location
import re
import os


app = Chalice(app_name='store-locator')
app.debug = True


@app.route('/locations/{postcode}', cors=True)
def locations(postcode):
    locations = Location.find(postcode, 5)

    return locations
