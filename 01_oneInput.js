// 1. 하나의 값을 입력받을 때
const fs = require('fs');
// 백준 테스트시 주석 제거
// const readFileSyncAddress = "/dev/stdin";

// vscode test시 주석 제거
const readFileSyncAddress = "../../input.txt";
const input = fs.readFileSync(readFileSyncAddress).toString().trim();