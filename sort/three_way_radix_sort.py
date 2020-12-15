class ThreeWayRadixSort(object):

    @classmethod
    def sort(cls, a):
        cls.__sort(a, 0, len(a) - 1, 0)

    @classmethod
    def __sort(cls, a, lo, hi, d):
        if hi <= lo:
            return
        lt = lo
        gt = hi
        v = cls.__char_at(a[lo], d)
        i = lo + 1
        while i <= gt:
            t = cls.__char_at(a[i], d)
            if t < v:
                cls.__exch(a, lt, i)
                lt += 1
                i += 1
            elif t > v:
                cls.__exch(a, i, gt)
                gt -= 1
            else:
                i += 1

        cls.__sort(a, lo, lt-1, d)
        if v >= 0:
            cls.__sort(a, lt, gt, d+1)
        cls.__sort(a, gt+1, hi, d)

    @staticmethod
    def __char_at(s, d):
        return ord(s[d]) if d < len(s) else -1

    @staticmethod
    def __exch(s, i, j):
        t = s[i]
        s[i] = s[j]
        s[j] = t
