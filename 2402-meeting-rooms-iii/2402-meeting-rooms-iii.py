from typing import List
from queue import PriorityQueue
from collections import defaultdict

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Use defaultdict to track the number of bookings for each room
        booked = defaultdict(int)

        # Comparator function for PriorityQueue
        def compare(a, b):
            if a[0] == b[0]:
                return a[1] > b[1]
            else:
                return a[0] > b[0]

        # PriorityQueue to store meetings based on their end time
        pq = PriorityQueue()

        # PriorityQueue to store available rooms
        free_rooms = PriorityQueue()

        # Initialize available rooms
        for i in range(n):
            free_rooms.put(i)

        # Sort meetings based on their start time
        meetings.sort()

        # Iterate through sorted meetings
        for v in meetings:
            start, end = v[0], v[1]

            # Process finished meetings, free up rooms
            while not pq.empty() and pq.queue[0][0] <= start:
                free_rooms.put(pq.get()[1])

            # Check if there is an available room
            if not free_rooms.empty():
                room = free_rooms.get()
                booked[room] += 1
                pq.put((end, room))  # Schedule the meeting in the room
            else:
                # If no available rooms, delay the meeting and assign a room later
                booked[pq.queue[0][1]] += 1
                p = pq.get()
                pq.put((p[0] + end - start, p[1]))

        # Find the room that held the most meetings
        max_rooms = 0
        meeting_room = -1
        for p in booked.items():
            if p[1] > max_rooms:
                max_rooms = p[1]
                meeting_room = p[0]

        # Return the room number that held the most meetings
        return meeting_room

