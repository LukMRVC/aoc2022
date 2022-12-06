use std::fs::File;
use std::io::{prelude::*, stdin, BufReader};

fn push_onto_stacks(mut stacks: Vec<Vec<char>>, line: &String) -> Vec<Vec<char>> {
    for (stack, _box) in line.chars().collect::<Vec<char>>().chunks(4).enumerate() {
        if !_box[1].is_whitespace() {
            stacks[stack].push(_box[1]);
        }
    }

    stacks
}

fn main() {
    // let mut file = File::open("input.txt").unwrap();
    let mut reader = BufReader::new(stdin());
    let mut stack_count: usize = 0;

    let mut buf = String::new();
    reader.read_line(&mut buf);
    stack_count = buf.len() / 4;

    let mut stacks: Vec<Vec<char>> = vec![vec![]; stack_count];
    stacks = push_onto_stacks(stacks, &buf);

    buf.clear();
    while let Ok(bytes_read) = reader.read_line(&mut buf) {
        if bytes_read == 0 {
            break;
        }
        if buf.is_empty() || buf.len() == 1 {
            break;
        }
        if !buf.starts_with('[') {
            buf.clear();
            continue;
        }
        stacks = push_onto_stacks(stacks, &buf);
        buf.clear();
    }

    for s in stacks.iter_mut() {
        s.reverse();
    }

    for s in stacks.iter() {
        for c in s.iter() {
            print!("[{}] ", c);
        }
        println!(" ");
    }

    let mut tmp: Vec<char> = vec![];

    for line in reader.lines() {
        let line = line.unwrap();
        let parts: Vec<&str> = line.split(' ').collect();
        let (its, from, to) = (
            parts[1].parse::<usize>().unwrap(),
            parts[3].parse::<usize>().unwrap(),
            parts[5].parse::<usize>().unwrap(),
        );
        // task 1
        // for _ in 0..its {
        //     let to_move = stacks[from - 1].pop().unwrap();
        //     stacks[to - 1].push(to_move);
        // }

        // task 2
        for _ in 0..its {
            tmp.push(stacks[from - 1].pop().unwrap());
        }
        while let Some(item) = tmp.pop() {
            stacks[to - 1].push(item);
        }
    }

    let top_crates = stacks
        .iter_mut()
        .map(|s| s.pop().unwrap())
        .collect::<String>();

    println!("{}", top_crates);
}
