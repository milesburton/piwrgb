#!/usr/bin/env node

fetch('https://www.randomnumberapi.com/api/v1.0/random?min=0&max=254&count=1')
    .then(response => response.json())
    .then(data => {
        const number = data[0];
        console.log(number);
    })
    .catch(error => {
        console.error('Error fetching random number:', error);
        process.exit(1);
    });

