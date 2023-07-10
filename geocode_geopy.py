"""
    Name: geocode_geopy.py
    Author: William A Loring
    Created: 07/10/2021
    Purpose: Geocode using Nominatim from geopy
"""

# Windows: pip install geopy
# Linux: pip3 install geopy
from geopy.geocoders import Nominatim


def main():
    # Test forward geocode
    city = input("Enter City: ")
    state = input("Enter State: ")
    country = input("Enter Country: ")
    geocode(city, state, country)

    # Test reverse geocode
    LAT = 41.8666
    LON = -103.6672
    reverse_geocode(LAT, LON)


def geocode(city, state, country):
    """
        Get lat, lng, and address using geopy
        from city, state, and country
    """
    try:
        # Create geolocator object with Nominatim geocode service
        # Nominatim is a free geolocater that uses openstreetmaps.org
        geolocator = Nominatim(user_agent="location_practice")

        # Create location dictionary for geocode request
        location = {
            "city": city,
            "state": state,
            "country": country
        }

        # Get geocode object with location data
        # lat, lng, address
        geo_location = geolocator.geocode(location)

        # Uncomment for testing as a program
        # print(geo_location.raw)
        # print(geo_location.address)
        # print((geo_location.latitude, geo_location.longitude))

        # Return geocode location information to calling program
        return (
            geo_location.latitude,
            geo_location.longitude,
            geo_location.address
        )
    except Exception as e:
        print("An error occured while geocoding.")
        # Print exception message
        print(e)


def reverse_geocode(lat, lon):
    """
        Reverse geocode from lat, lon using geopy
    """
    try:
        # Create geolocator object
        geolocator = Nominatim(user_agent="location_practice")
        # Create location tuple
        location = (lat, lon)
        # Get address with resolution of town
        address = geolocator.reverse(location, zoom=10)

        # Uncomment For testing as a program
        # print(address)

        return address
    except Exception as e:
        print("An error occured while reverse geocoding.")
        # Print exception message
        print(e)


# If a standalone program, call the main function
# Else, use as a module
if __name__ == '__main__':
    main()
