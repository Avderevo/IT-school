$(function () {

  $(".js-create-book").click(function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-user").modal("show");
      },
      success: function (data) {
        $("#modal-user .modal-content").html(data.html_form);
      }
    });
  });

});


$("#modal-user").on("submit", ".js-user-login-form", function () {
    
    var form = $(this);
 
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          
         
          $("#modal-user").modal("hide"); 
          location.reload();
        }
        else {
          $("#modal-user .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  });


   
$("#modal-user").on("submit", ".js-user-create-form", function () {
    
  var form = $(this);
      
        $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
            
            /*$("#users-list").html(data.users);*/
            $("#modal-user").modal("hide");  // <-- This is just a placeholder for now for testing
          }
          else {
            $("#modal-user .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    
  });


$("#modal-user").on("submit", ".js-user-remind-form", function () {
    
  var form = $(this);  
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      beforeSend: function () {
       
      
      },
      success: function (data) {
        if (data.form_is_valid) {
          
          /*$("#users-list").html(data.users);*/
          $("#modal-user").modal("hide");  // <-- This is just a placeholder for now for testing
        }
        else {
          $("#modal-user .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  });

$(function () {
  $(".js-remind-password").click(function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
       
        $("#modal-user").modal("hide");
      },
      success: function (data) {
        $("#modal-user").modal("show");
        $("#modal-user .modal-content").html(data.html_form);
      }
    });
  });

});

 
var card = document.getElementsByClassName("card-additions"); 
for (var i = 0; i < card.length; i++) {
  MakeIconHover(card[i]);
}

function MakeIconHover(row) {
  row.addEventListener("mouseover", function() {
    var icon = this.getElementsByClassName('md-100');
    icon[0].style.color = "#37927a";
});  

  row.addEventListener("mouseout", function() {
    var icon = this.getElementsByClassName('md-100');
    icon[0].style.color = "#346896";
});
}

var card = document.getElementsByClassName("curses-card"); 
for (var i = 0; i < card.length; i++) {
  MakehrefHover(card[i]);
}

function MakehrefHover(row) {
  row.addEventListener("mouseover", function() {
    var href = this.getElementsByTagName('hr');
    href[0].style.background = "#fff";
    href[0].style.width = "17rem";
});  

  row.addEventListener("mouseout", function() {
    var href = this.getElementsByTagName('hr');
    href[0].style.background = "#f24903";
    href[0].style.width = "10rem";
});
}