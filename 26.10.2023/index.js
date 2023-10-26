function calculate_pi() {
    /**
     * 1/1 + 1/4 + 1/9 + 1/16 + 1/25 + ... = (pi^2)/6
     */
    let a = 0;
    for (let i = 1; i <= 10_000_000_000; i++) {
        a += 1 / (i ** 2);
    }
    console.log(Math.sqrt(a * 6));
}

calculate_pi();
