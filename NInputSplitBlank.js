// 3. 여러 줄의 값들을 입력받을 때
const fs = require('fs');
const [n, ...arr] = fs.readFileSync("/dev/stdin").toString().trim().split(/\s/);
