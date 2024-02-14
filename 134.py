"""
134. Gas Station

There are n gas stations along a circular route, where the amount of gas at the 
ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to 
travel from the ith station to its next (i + 1)th station. 
You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index 
if you can travel around the circuit once in the clockwise direction, 
otherwise return -1. If there exists a solution, it is guaranteed to be unique.
"""

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_surplus = 0  # Total surplus of gas
        current_surplus = 0  # Current surplus of gas
        start_station = 0  # Potential start station

        for i in range(len(gas)):
            total_surplus += gas[i] - cost[i]
            current_surplus += gas[i] - cost[i]

            # If current_surplus is negative, i can't be the starting station
            if current_surplus < 0:
                start_station = i + 1  # Try the next station as the starting one
                current_surplus = 0  # Reset the current surplus

        # If total_surplus is negative, it means we can't complete the circuit
        if total_surplus < 0:
            return -1

        return start_station
