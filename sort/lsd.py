class LSD(object):
    @staticmethod
    def sort(a, w):
        r = 256
        n = len(a)
        aux = [""] * n
        for d in range(w):
            d = w - d - 1
            count = [0] * (r + 1)
            for i in range(n):
                count[ord(a[i][d]) + 1] += 1

            for r in range(r):
                count[r+1] += count[r]

            for i in range(n):
                aux[count[ord(a[i][d])]] = a[i]
                count[ord(a[i][d])] = count[ord(a[i][d])] + 1

            for i in range(n):
                a[i] = aux[i]
