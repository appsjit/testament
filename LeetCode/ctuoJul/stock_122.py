# / *
#
# buy and sell
# stocks * /
#
# function
# buyStock(arr, k)
# {
#     let
# profit = []
# for (let i = 0; i < arr.length; i++){
#     profit.push(0)
# }
# for (let i = 0; i < k; i++){
# let min = arr[0]
# let max = 0
#
# for (let j = 1; j < arr.length; j++ ){
# min = Math.min(min, arr[j]-profit[j]) //= ==
# max = Math.max(max, arr[j]- min)
# profit[j] = max
#
# }
# }
#
# return profit.pop()
# }
# console.log(buyStock([0, 3, 1, 5], 2))