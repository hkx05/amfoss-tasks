use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let n: i32 = input.trim().parse().expect("Invalid input");

    for i in 2..n {
        let mut prime = true;
        for b in 2..i {
            if i % b == 0 {
                prime = false;
                break;
            }
        }
        if prime {
            println!("{}", i);
        }
    }
}