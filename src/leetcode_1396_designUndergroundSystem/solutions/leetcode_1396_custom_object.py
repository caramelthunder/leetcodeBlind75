class Passenger:
    def __init__(self, id: int):
        self.id = id
        self.checkin_station = None
        self.checkin_time = None
        self.checkout_station = None
        self.checkout_time = None

    def checkin(self, station_name: str, time: int):
        self.checkin_station = station_name
        self.checkin_time = time

    def checkout(self, station_name: str, time: int):
        self.checkout_station = station_name
        self.checkout_time = time


class Route:
    def __init__(self, start_station: str, end_station: str):
        self.trip = (start_station, end_station)
        self.total_time = 0
        self.total_trips = 0

    def add_trip(self, travel_time: int):
        self.total_time += travel_time
        self.total_trips += 1

    def get_avg_trip_time(self):
        return self.total_time / self.total_trips


class UndergroundSystem:
    def __init__(self):
        self.passengers_log = {}
        self.routes_log = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        """
        Records the check-in details for a passenger.

        :param id: Integer representing the ID of the passenger.
        :param stationName: String representing the name of the station where the check-in occurred.
        :param t: Integer representing the check-in time.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if id not in self.passengers_log:
            self.passengers_log[id] = Passenger(id)
            self.passengers_log[id].checkin(stationName, t)
        else:
            raise Exception(f"Passenger {id} already checked in.")

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        """
        Records the check-out details for a passenger and updates the route log.

        :param id: Integer representing the ID of the passenger.
        :param stationName: String representing the name of the station where the check-out occurred.
        :param t: Integer representing the check-out time.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if id in self.passengers_log:
            passenger = self.passengers_log.pop(id)
            passenger.checkout(stationName, t)
            self._add_route(
                passenger.checkin_station,
                passenger.checkout_station,
                passenger.checkout_time - passenger.checkin_time,
            )
        else:
            raise Exception(f"Passenger {id} has not checked in.")

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        """
        Calculates and returns the average trip time between two stations.

        :param startStation: String representing the start station.
        :param endStation: String representing the end station.

        :return: Float representing the average trip time, or 0.0 if the route does not exist.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        trip = (startStation, endStation)
        if trip in self.routes_log:
            return self.routes_log[trip].get_avg_trip_time()
        return 0.0

    def _add_route(
        self, start_station: str, end_station: str, travel_time: int
    ):
        """
        Adds a trip to the route log.

        :param start_station: String representing the start station of the trip.
        :param end_station: String representing the end station of the trip.
        :param travel_time: Integer representing the travel time of the trip.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        trip = (start_station, end_station)
        if trip not in self.routes_log:
            self.routes_log[trip] = Route(start_station, end_station)
        self.routes_log[trip].add_trip(travel_time)
