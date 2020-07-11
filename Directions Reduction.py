def dirReduc(arr):
    oposites = {
      "NORTH": "SOUTH",
      "SOUTH": "NORTH",
      "WEST": "EAST",
      "EAST": "WEST"
    }

    print("input data: ", arr)

    while True:
        if len(arr) == 1:
             return arr
        for i in range(len(arr)-1):
             if arr[i+1] == oposites[arr[i]]:
                print(i)
                print(arr)
                del(arr[i:i+2])
                print(arr)
                break
             elif i == len(arr) - 2:
                return arr

a = ["NORTH"]

print("result: ", dirReduc(a))
