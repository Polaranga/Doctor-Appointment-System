function userFields() {
    var userType = document.getElementById("Usertype").value;
    if (userType == "Doctor") {
        document.getElementById("doctor-fields").style.display = "block";
        document.getElementById("patient-fields").style.display = "none";
        
    } else if (userType == "Patient") {
        document.getElementById("doctor-fields").style.display = "none";
        document.getElementById("patient-fields").style.display = "block";
        
    } else {
        document.getElementById("doctor-fields").style.display = "none";
        document.getElementById("patient-fields").style.display = "none";
    }
}
