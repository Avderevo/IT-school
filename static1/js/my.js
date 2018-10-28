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
          
          $("#users-list").html(data.users);
          $("#modal-user").modal("hide");  // <-- This is just a placeholder for now for testing
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
          
          $("#users-list").html(data.users);
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
      success: function (data) {
        if (data.form_is_valid) {
          
          $("#users-list").html(data.users);
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