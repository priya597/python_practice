class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        max_units = 0
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        for box, unit in boxTypes:
            if(box) <= truckSize:
                max_units += box*unit
                console.debug('Maximum units', max_units)
                truckSize -= box
            else:
                return max_units+(truckSize*unit)
        return max_units


boxTypes = [[5, 10], [2, 5], [4, 7], [3, 9]]
truckSize = 4
unitcount = maximumUnits(boxTypes, truckSize)
print(unitcount)
