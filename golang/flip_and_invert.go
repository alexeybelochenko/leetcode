package flipAndInvertImage

func flipAndInvertImage(A [][]int) [][]int {
    for _, v := range A {
        l := 0
        r := len(v) - 1
        for l < r {
            if v[l] == v[r] {
                v[l] ^= 1
                v[r] ^= 1
            }
            l++ 
            r--
        }
        if l == r {
            v[l] ^= 1
        }
    }
    
    return A
}