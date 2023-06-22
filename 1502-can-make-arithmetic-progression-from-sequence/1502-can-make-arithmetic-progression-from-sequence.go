import "sort"

func canMakeArithmeticProgression(arr []int) bool {
    sort.Ints(arr)
    var store int = arr[1] - arr[0]
    
    var j int
    var i int = 0
    for j = 1; j < len(arr); j += 1 {
        curr := arr[j] - arr[i]
        if store != curr {
            return false
        }
    
        i += 1
    }
    return true
}
