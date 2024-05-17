function submitForm(event) {
  //let user;
  let username1 = document.getElementById("username").value;
  let password1 = document.getElementById("password").value;


  let data = {
    username: username1,
    password: password1
};

  let myrequest = new XMLHttpRequest();
  
  myrequest.open("POST","http://localhost:5000/login",true)
  myrequest.setRequestHeader("Content-Type", "application/json");
  myrequest.onload = function () {
    if (myrequest.status === 201) {
        // Data has been successfully submitted
        alert("Login successful!")
       // document.getElementById("Login successful!").reset();
    } 
    else {
        // Request failed
        alert("Invalid username or password. Please try again.");
    }
  };

   // Handle errors
   myrequest.onerror = function () {
    alert("Request failed. Please try again later.");
  };
  myrequest.send(JSON.stringify(data));
  window.location.href = "signin";
  
  // to get item from storgae and we get this Data from Refister page.
  // let u = localStorage.getItem("data");
  // user = JSON.parse(u);
  // if (user.username1 === username1 && user.password1 === password1) {
  //   alert("Login successful!");
  // } 
  // else {
  //   alert("Invalid username or password.");
  // }
  event.preventDefault();
}
