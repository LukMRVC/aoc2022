use std::io::{prelude::*, stdin, BufReader};

fn main() {
    let mut reader = BufReader::new(stdin());

    let mut calories: Vec<usize> = vec![];

    let mut calorie_counter = 0;
    for maybe_line in reader.lines() {
        if let Ok(line) = maybe_line {
            if line.trim().is_empty() {
                calories.push(calorie_counter);
                calorie_counter = 0;
                continue;
            }

            let calories: usize = line.parse().unwrap();
            calorie_counter += calories;
        }
    }

    let max_calories = calories.iter().max().unwrap();
    println!("{}", max_calories);
}
