const clock = document.querySelector("#clock");
const color = document.querySelector("#color");
const body = document.querySelector("body");

let count = 0;

(function  rgbClock(){
  const date = new Date()
  const h = String(date.getHours())
  const m = String(date.getMinutes())
  const s = String(date.getSeconds())

  const colorString = `rgb(${h*10}, ${m*4.25}, ${s*4.25})`;

  function checkTime(value){
    if (value.length < 2) return 0+value;
    return value;
  }

  clock.innerText = checkTime(h) + ":" + checkTime(m) + ":" + checkTime(s)
  color.innerText = colorString

  body.style.background = colorString;

  const timer = window.setTimeout(rgbClock, 1000);
  count++;

  if (count > 5){
    clearTimeout(timer)
  }

})()
