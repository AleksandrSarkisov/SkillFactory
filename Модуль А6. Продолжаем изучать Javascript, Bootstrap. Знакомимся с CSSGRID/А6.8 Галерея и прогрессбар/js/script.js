$(document).ready(function() {
   // Stuff to do as soon as the DOM is ready

   function increase(val){
     progress = Number($(".progress-bar").attr("aria-valuenow"));
     if (progress+val <= 100){
       progress += val;
       $(".progress-bar").attr("aria-valuenow",progress);
       $(".progress-bar").width(String(progress)+"%");
       $(".progress-bar").html(String(progress)+"%")
     }
   };

   $(".btn").click(function(){
     val = Number($(this).attr("value"));
     increase(val);
   });
});
