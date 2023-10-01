package main
import "fmt"

func main() {
    var num int
    fmt.Println("Enter the number")
    fmt.Scanln(&num)
    for i := 2; i <= num; i++ {
        prime := true
        for j := 2; j*j <= i; j++ {
            if i%j == 0 {
                prime = false
                break
            }
        }
        if prime {
            fmt.Println(i)
        }
    }
}

