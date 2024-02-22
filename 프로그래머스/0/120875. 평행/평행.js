function solution(dots) {
  var answer = 0;

  function cal(a, b, c, d) {
    let x, y;

    x = (b[1] - a[1]) / (b[0] - a[0]);
    y = (d[1] - c[1]) / (d[0] - c[0]);

    if (x === y) {
      answer = 1;
    }
  }

  cal(dots[0], dots[1], dots[2], dots[3]);

  cal(dots[0], dots[2], dots[1], dots[3]);

  cal(dots[0], dots[3], dots[1], dots[2]);

  return answer;
}