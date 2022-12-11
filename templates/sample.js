


function validateform()
{
    var username = document.myform.username.value;
    var password = document.myform.password.value;
    if(username=="" || username==null)
    {
       alert("username should not be empty");
       return false;
    }
    else if (password.length<6)
    {
        alert("password must be 6 char length");
        return false;
    }
}