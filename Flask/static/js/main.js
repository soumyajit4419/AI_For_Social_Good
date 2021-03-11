let time = new Date();
let hour = time.getHours();
let minute = time.getMinutes();
const url = "https://ai-for-social-good.herokuapp.com";
$(".set-time").text(`${hour}:${minute}`);

function getPredictions(text) {
  $.ajax({
    url: url + "/predict",
    method: "POST",
    data: {
      text: text,
    },
    crossDomain: true,
    success: function (res) {
      console.log(res);
      let time = new Date();
      let hour = time.getHours();
      let minute = time.getMinutes();
      var ml_pred = res.ml_pred;
      var dl_pred = res.dl_pred;
      let outputMsg = "";

      if (ml_pred == "1" && dl_pred == "1") {
        outputMsg = "Message is a suicide ideation";
      } else if (ml_pred == "0" && dl_pred == "0") {
        outputMsg = "Mesage is not realted to suicide ideation";
      } else if (
        (ml_pred == "0" && dl_pred == "1") ||
        (ml_pred == "1" && dl_pred == "0")
      ) {
        outputMsg = "Mesage may be or may not be related suicide ideation";
      } else {
        outputMsg = "Sorry, Unable to understand";
      }

      $("#new-res").append(`
      <div class="msg right-msg">
      <div class="msg-img"
          style="background-image: url(https://image.flaticon.com/icons/svg/145/145867.svg)">
      </div>
      <div class="msg-bubble">
          <div class="msg-info">
              <div class="msg-info-name">Champ</div>
              <div class="msg-info-time set-time">${hour}:${minute}</div>
          </div>
    
          <div class="msg-text">
              ${text}
          </div>
      </div>
    </div>
    
    <div class="msg left-msg">
    <div class="msg-img" style="background-image: url(https://image.flaticon.com/icons/svg/327/327779.svg)">
    </div>
    
    <div class="msg-bubble">
        <div class="msg-info">
            <div class="msg-info-name">BOT</div>
            <div class="msg-info-time set-time">${hour}:${minute}</div>
        </div>
    
        <div class="msg-text">
           ${outputMsg}
        </div>
    </div>
    </div>
    `);
    },
    error: function (err) {
      console.log(err);
    },
  });
  return;
}

function submitHandler() {
  var input = $("#user-input").val();
  if (input == "") return;
  getPredictions(input);
  $("#user-input").val("");
}
