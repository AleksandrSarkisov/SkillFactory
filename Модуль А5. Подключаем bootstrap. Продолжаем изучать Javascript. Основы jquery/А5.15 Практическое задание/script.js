$(document).ready(function(){

  const story = data => {
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
    for (string in data['text']){
      for ch in string{
        if ch == '{'
      }
    }
    $html.appendTo(document.body);
  }

  $.getJSON('https://api.myjson.com/bins/jcmhn', function(data){
    story(data)

  });
});
