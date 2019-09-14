function replace(str, userInput){
  mask = /{\w+}/g;
  match = str.match(mask);
  for (let i = 0; i < match.length; i++){
    str = str.replace(match[i], "<input placeholder="+match[i]+">");
  }
  return str;
}

function story (data){
  inputs = []
  mask = /{\w+}/g;
  for (let i=0; i<data['text'].length; i++){
    match = data['text'][i].match(mask)
    for (let j = 0; j<match.length; j++){
      if (!inputs.includes(match[j])){
        inputs.push(match[j]);
      }
    }
  }
  for (let i = 0; i<inputs.length; i++){
    html = '<input name="'+inputs[i]+'" style="margin-bottom: 10px; width: 200px;" placeholder="'+inputs[i]+'">';
    $('form div').append(html);
  }
}


$(document).ready(function(){
  $.getJSON('https://api.myjson.com/bins/jcmhn', function(data){
    story(data);
    $('button').click(function(){
      mask = /{\w+}/g;
      for (let i=0;i<data['text'].length;i++){
        match = data['text'][i].match(mask);
        for (let j=0;j<match.length;j++){
          data['text'][i] = data['text'][i].replace(match[j], $('input[name="'+match[j]+'"]')[0].value);
        }
      }
      $('.result').append('<p>'+data['text']+'</p>');
    });
  });

});
