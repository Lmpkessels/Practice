function toUpperLastLetter(str) {
  return str
    .toLowerCase()
    .split(" ")
    .map((word) => {
      let last = word[word.length - 1].toUpperCase();
      let rest = word.slice();
      return last + rest;
    })
    .join(" ");
}

console.log(toUpperLastLetter("luuk kessels"));
