pub fn raindrops(n: u32) -> String {
    let mut res = String::new();
    let lut = [3, 5, 7];
    let vals = ["Pling", "Plang", "Plong"];
    let mut flag = false;

    for i in 0..lut.len() {
        if n % lut[i] == 0 {
            flag = true;
            res += vals[i];
        }
    }

    return if flag { res } else { n.to_string() };
}
