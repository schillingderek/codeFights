def ringRoads(innerRing, outerRing, roads, travels):
        ans = []
        rad = outerRing - innerRing
        for travel in travels:
                angle = 0
                min_dist = math.pi*innerRing*2 + rad + math.pi*outerRing*2
                for r in roads:
                        arc1 = min(abs(travel[0] - r), abs(travel[0] - r + 360), abs(travel[0] - r - 360))
                        arc1_len = arc1/360.0*math.pi*innerRing*2
                        arc2 = min(abs(r - travel[1]), abs(r - travel[1] + 360), abs(r - travel[1] - 360))
                        arc2_len = arc2/360.0*math.pi*outerRing*2
                        cur_len = arc1_len + arc2_len + rad
                        min_dist = min(min_dist, cur_len)                                

                ans.append(min_dist)
        return ans
