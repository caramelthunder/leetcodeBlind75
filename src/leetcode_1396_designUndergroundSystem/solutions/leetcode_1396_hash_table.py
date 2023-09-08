class UndergroundSystem:
    def __init__(self):
        self.checked_ins = {}
        self.trips = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        """
        Records the check-in details for a passenger.

        :param id: Integer representing the ID of the passenger.
        :param stationName: String representing the name of the station where the check-in occurred.
        :param t: Integer representing the check-in time.

        :raises Exception: If the passenger is already checked in.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if id not in self.checked_ins:
            self.checked_ins[id] = (stationName, t)
        else:
            raise Exception(f"Passenger {id} already checked in.")

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        """
        Records the check-out details for a passenger and updates the trip log.

        :param id: Integer representing the ID of the passenger.
        :param stationName: String representing the name of the station where the check-out occurred.
        :param t: Integer representing the check-out time.

        :raises Exception: If the passenger has not checked in.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if id in self.checked_ins:
            start_station, start_time = self.checked_ins.pop(id)
            trip = (start_station, stationName)
            self._add_trip(trip, t - start_time)
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
        if trip in self.trips:
            total_time, total_trips = self.trips[trip]
            return total_time / total_trips
        return 0.0

    def _add_trip(self, trip: tuple[str, str], travel_time: int):
        """
        Adds a trip to the trip log.

        :param trip: Tuple of strings representing the start and end stations of the trip.
        :param travel_time: Integer representing the travel time of the trip.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if trip not in self.trips:
            self.trips[trip] = (0, 0)
        total_time, total_trips = self.trips[trip]
        self.trips[trip] = (total_time + travel_time, total_trips + 1)
