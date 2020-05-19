#!/usr/env python
# -*- coding:utf-8 -*-

class Solution(object):

    def first_inc_pos(self, prices, start):
        pos = start - 1
        prev = -1
        curr = 0
        found = False
        for curr in prices[start:]:
            if prev < 0:
                pos += 1
            elif prev < curr:
                found = True
                break
            else:  # prev >= curr
                pos += 1
            prev = curr
        if found:
            return pos
        else:
            return -1

    # 단, 시작 위치가 끝이 아니고, 찾지 못 한 경우는 마지막 위치를 반환한다
    def last_dec_pos(self, prices, start):
        pos = start - 1
        prev = -1
        curr = 0
        for curr in prices[start:]:
            if prev < 0:
                pos += 1
            elif prev > curr:
                break
            else:  # prev <= curr
                pos += 1
            prev = curr
        if len(prices) == pos:
            pos -= 1
        return pos

    def flip_bool(self, flip):
        flipped = False if flip else True
        return flipped

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prev = -1
        point = 0
        accum = 0
        buy = False
        while point >= 0:
            if not buy:
                point = self.first_inc_pos(prices, point)
                print("first_inc_pos: ", point)
            else:
                point = self.last_dec_pos(prices, point)
                print("last_dec_pos: ", point)
            if buy and prev >= 0:
                accum += prices[point] - prices[prev]
                print("accumulation: ", accum)
            buy = self.flip_bool(buy)
            prev = point
        return accum


if __name__ == "__main__":
    solution = Solution()
    prices = [7,1,5,3,6,4]
    actual = solution.maxProfit(prices)
    print(actual)
