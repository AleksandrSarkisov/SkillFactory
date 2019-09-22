const numDivs = 36;
const maxHits = 10;

let hits = 0;
// let firstHitTime = 0;
let miss = 0
let startTime

function round() {

  // Done FIXME: надо бы убрать "target" прежде чем искать новый
  $(".game-field").removeClass("target");
  let divSelector = randomDivId();
  $(divSelector).addClass("target");
  // Done TODO: помечать target текущим номером
  $(divSelector).text(String(hits+1))
  // Done FIXME: тут надо определять при первом клике firstHitTime

  if (hits === maxHits) {
    endGame();
  }
}

function endGame() {
  // Done FIXME: спрятать игровое поле сначала
  $(".gameArea").addClass("d-none");
  let totalPlayedMillis = getTimestamp() - startTime;
  let totalPlayedSeconds = Number(totalPlayedMillis / 1000).toPrecision(3);
  let points = hits-miss
  if (points%10 == 1 && points != 11 && points != -11){
    $("#number-of-points").text(String(points)+" балл");
  }
  else if (points%10 == 2 || points%10 == 3 || points%10 == 4){
    $("#number-of-points").text(String(points)+" балла");
  }
  else{
    $("#number-of-points").text(String(points)+" баллов");
  }
  $("#total-time-played").text(totalPlayedSeconds);


  $("#win-message").removeClass("d-none");
}

function handleClick(event) {
  // Done FIXME: убирать текст со старых таргетов. Кажется есть .text?
  if ($(event.target).hasClass("target")) {
    hits = hits + 1;
    $(".target").text("");
    $(".game-field").removeClass("miss");
    round();
  }
  // Done TODO: как-то отмечать если мы промахнулись? См CSS класс .miss
  else{
    $(event.target).addClass("miss");
    miss += 1;
  }
}

function init() {
  // Done TODO: заказчик просил отдельную кнопку, запускающую игру а не просто по загрузке
  $("#button-start").click(function(){
    $(this).attr("class", "d-none");
    $("#button-reload").removeClass("d-none");
    startTime = getTimestamp();
    round();
    $(".game-field").click(handleClick);
  });

  $("#button-reload").click(function() {
    location.reload();
  });
}

$(document).ready(init);
