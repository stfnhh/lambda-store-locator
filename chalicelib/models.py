from chalicelib import db
from chalice import NotFoundError

class Postcode(object):
    @classmethod
    def find(self, postcode):
        """
        Returns latitude and longitude of a given postcode

        Keyword arguments:
          postcode - A US or Canadian postal code.
        """
        db.execute("""
            SELECT 
                latitude, 
                longitude 
            FROM postcodes 
            WHERE postcode = '%s' 
            LIMIT 1;
        """ % postcode.replace('%20', ''))

        coordinates = db.fetchone()

        if not coordinates:
            raise NotFoundError("Unknown postcode %s" % postcode)

        return coordinates

class Location(object):
    @classmethod
    def find(self, postcode, limit=5):
        """
        Returns a list of n nearest locations from the locations table.

        Keyword arguments:
          postcode - A US or Canadian postal code.
          limit - The maximum amount of locations to be returned (default 5)
        """

        coordinates = Postcode.find(postcode)

        db.execute("""
            SELECT 
              l.*, 
              ROUND(SQRT(POWER(69.1 * (%f - l.latitude), 2) + POWER(69.1 * (l.longitude - %f) * COS(41.929599 / 57.3), 2)), 2) AS distance 
            FROM postcodes p 
            INNER JOIN locations l ON(l.postcode = p.postcode) 
            ORDER BY distance 
            LIMIT %i;
        """ % (coordinates['latitude'], coordinates['longitude'], limit))

        locations = db.fetchall()

        if not locations:
            raise NotFoundError("No locations found")

        return locations
    