function submitForm(event) {

 

  let username = document.getElementById("username").value;
  let password = document.getElementById("password").value;
  let confirmPassword = document.getElementById("confirmPassword").value;
  let email = document.getElementById("email").value;

  if (password !== confirmPassword) {
    alert("Password dose not match.");
    return;
  }

  let data = {
    username: username,
    password: password,
    email: email
  };


  let myrequest = new XMLHttpRequest();

  myrequest.open("POST","http://localhost:5000/users",true)
  myrequest.setRequestHeader("Content-Type", "application/json");
  myrequest.onload = function () {
    if (myrequest.status === 201) {
        // Data has been successfully submitted
        alert("Registration successful!");
        document.getElementById("registrationForm").reset();
    } else {
        // Request failed
        alert("Failed to register. Please try again later.");
    }
  };

   // Handle errors
   myrequest.onerror = function () {
    alert("Request failed. Please try again later.");
  };

// Convert data to JSON format and send the request
myrequest.send(JSON.stringify(data));

window.location.href = "log";
// Prevent the default form submission
event.preventDefault();
}

//   myrequest.send();
//   console.log(myrequest);


//   JSON.stringify(Data) // Before storing the data, it is converted to a JSON string. 
//   localStorage.setItem("data", JSON.stringify(Data));
//   document.getElementById("registrationForm").reset();
//   alert("Registration successful!");
// }

