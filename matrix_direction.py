class MatrixDirection:
    def __init__(self):
        pass

    # BigO Time O(1)| Space 0(1)
    def get_Direction(self, N, M):
        if (N != M and N % 2 == 0 and
                M % 2 != 0 and N < M):
            print("L")
            return

        if (N != M and N % 2 == 0 and
                M % 2 == 0 and N > M):
            print("U")
            return

        if N == M and N % 2 != 0 and M % 2 != 0:
            print("R")
            return

        if N == M and N % 2 == 0 and M % 2 == 0:
            print("L")
            return

        if (N != M and N % 2 != 0 and
                M % 2 != 0 and N < M):
            print("R")
            return

        if (N != M and N % 2 != 0 and
                M % 2 != 0 and N > M):
            print("D")
            return

        if (N != M and N % 2 == 0 and
                M % 2 != 0 and R < M):
            print("L")
            return

        if (N != M and N % 2 == 0 and
                M % 2 == 0 and N > M):
            print("U")
            return

        if (N != M and N % 2 != 0 and
                M % 2 != 0 and N > M):
            print("D")
            return

        if (N != M and N % 2 != 0 and
                M % 2 != 0 and N < M):
            print("R")
            return

    # Define get_Cases function for console's use
    def get_Cases(self):
        print("Insert a number of cases:")
        cases = int(input())
        for i in range(cases):
            print("Insert N value:")
            N = int(input())
            print("Insert M value:")
            M = int(input())
            print("Direction:")
            self.get_Direction(N, M)


# Driver Code
test = MatrixDirection()
test.get_Cases()
