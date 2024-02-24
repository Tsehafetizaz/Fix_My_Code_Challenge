// 1-print_square.js: Corrected implementation
function printSquare(size) {
    for (let row = 0; row < size; row++) {
        let line = '';
        for (let col = 0; col < size; col++) {
            line += '#';
        }
        console.log(line);
    }
}

// Extract the square size from the command line argument and print the square
const size = parseInt(process.argv[2], 10);
if (!isNaN(size)) {
    printSquare(size);
} else {
    console.error('Usage: node 1-print_square.js <size>');
    console.error('<size> should be an integer.');
}
