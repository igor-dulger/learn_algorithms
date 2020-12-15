class MSD(object):

    @classmethod
    def sort(cls, a):
        if len(a) <= 1:
            return
        aux = [""] * len(a)
        cls.__inner_sort(a, aux, 0, len(a)-1, 0)

    @classmethod
    def __inner_sort(cls, a, aux, lo, hi, d):
        r = 256
        count = [0] * (r + 2)

        for i in range(lo, hi+1):
            count[cls.__char_at(a[i], d) + 2] += 1

        for r in range(r+1):
            count[r+1] += count[r]

        for i in range(lo, hi+1):
            code = cls.__char_at(a[i], d) + 1
            aux[count[code]] = a[i]
            count[code] += 1

        for i in range(lo, hi+1):
            a[i] = aux[i - lo]

        for i in range(r):
            if hi > lo:
                cls.__inner_sort(a, aux, lo + count[i], lo + count[i+1] - 1, d+1)

    @staticmethod
    def __char_at(s, d):
        return ord(s[d]) if d < len(s) else -1

