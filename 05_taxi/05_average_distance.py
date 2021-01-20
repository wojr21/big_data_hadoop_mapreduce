from mrjob.job import MRJob
from mrjob.step import MRStep

class MRTaxi(MRJob):

    def steps(self):
        return [
            MRStep(mapper = self.mapper,
                   reducer=self.reducer)
        ]

    def mapper(self, _, line):
        (VendorID, tpep_pickup_datetime, tpep_dropoff_datetime, passenger_count, trip_distance, pickup_longitude,
         pickup_latidute, RatecodeID, store_and_fwd_flag, dropoff_longitude, dropoff_latidute, payment_type,
         fare_amount, extra, mta_tax, tip_amount, tolls_amount, improvement_surcharge, total_amount) = line.split(',')

        yield None, float(trip_distance)

    def reducer(self, key, values):
        distance = 0
        count = 0
        for value in values:
            distance += value
            count += 1

        yield None, distance / count

if __name__ == '__main__':
    MRTaxi.run()