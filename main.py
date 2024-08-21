# a = int(input())
# b = int(input())

T = int(input().rstrip())
for _ in range(T):
    a, b = input().split()

    try:
        result = int(a) // int(b)
        # print(result)

    except ZeroDivisionError as e:
        print("Error Code: ", e)

    except ValueError as e:
        print("Error Code: ", e)

    else:
        print(result)
        break