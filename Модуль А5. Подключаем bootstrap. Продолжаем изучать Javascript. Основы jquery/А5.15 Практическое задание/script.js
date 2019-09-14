$(document).ready(function(){

  function replace(str){
    mask = /{\w+}/g;
    match = str.match(mask);
    for (let i = 0; i < match.length; i++){
      str = str.replace(match[i], "<input placeholder="+match[i]+">");
    }
    return str;
  }

  const story = data => {

    for (let i=0; i<data['text'].length; i++){
      data['text'][i] = replace(data['text'][i]);
    }

    const $html = $(`
    <div class="container">
      <div class="row">
        <div class="story">
          <h2>Текст</h2>
          <p>${data.text}</p>
        </div>
      </div>
    </div>
    `)

    $html.appendTo(document.body);
  }

  $.getJSON('https://api.myjson.com/bins/jcmhn', function(data){
    story(data);
    console.log(data);
  });
});
