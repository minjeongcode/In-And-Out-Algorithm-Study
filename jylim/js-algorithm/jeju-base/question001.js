var nums = [100, 200, 300, 400, 500];

// answer 1
var splicedNums = nums.splice(3, 2);
console.log(nums);
// [100, 200, 300]
console.log(splicedNums);
// [400, 500]

// answer 2: 제주베이스 정답
// nums.pop();
// nums.pop();
console.log(nums);
// [100, 200, 300]

// answer 3
const filteredNums = nums.filter((num) => num < 4);
console.log(nums);
// [100, 200, 300]
console.log(filteredNums);
// [400, 500]
