pub fn nth(n: u32) -> u32 {
    let mut primes = vec![2];

    while n > (primes.len() - 1) as u32 {
        let mut test = primes[primes.len() - 1] + 1;
        

        let mut prime_ck = |n| {
            for i in 0..primes.len() {
                if n % primes[i] == 0 { return false };
            }
            primes.push(n);
            return true;
        };

        while !prime_ck(test) {
            test += 1;
        }
    }

    return primes[n as usize];
}
