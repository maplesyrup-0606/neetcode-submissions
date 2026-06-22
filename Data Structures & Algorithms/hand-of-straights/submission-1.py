class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand = Counter(hand)
        keys = sorted(hand.keys())

        baseKey = keys[0]
        lastKey = keys[-1] + 1
        while True:
            if baseKey == lastKey:
                break

            if hand[baseKey] == 0:
                baseKey += 1
            
            elif hand[baseKey] < 0:
                return False
            
            else:
                for i in range(groupSize):
                    if baseKey + i < 0:
                        return False
                    hand[baseKey + i] -= 1

                    if hand[baseKey + i] < 0:
                        return False
        return True 