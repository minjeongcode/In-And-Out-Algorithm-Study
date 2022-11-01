function solution(ingredient) {
  let answer = 0;
  for (let i = 0; i < ingredient.length; i++) {
    if (ingredient[i] === 1) {
      if (
        ingredient[i + 1] === 2 &&
        ingredient[i + 2] === 3 &&
        ingredient[i + 3] === 1
      ) {
        answer++;
        ingredient.splice(i, 4);
        i -= 4;
      }
    }
  }

  return answer;
}
console.log(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]));
