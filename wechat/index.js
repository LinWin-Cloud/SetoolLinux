﻿function logon(){
    var password=document.getElementById("password").value;
    var usersname=document.getElementById("usersname").value;
    if
    ( 
        password == ""
    )
    {
        alert("微信号不可为空")
        console.log("Error!")
        console.log("pwd:"+password)
        console.log("users:"+usersname)
        return false
    }
    if(usersname == ""){
        alert("密码不可为空")
        console.log("Error!")
        console.log("pwd:"+password)
        console.log("users:"+usersname)
        return false
    }
    else
    {
        console.log("Right")
        console.log("password:"+password)
        console.log("usersname:"+usersname)
        var url="'"+"usersname="+usersname+"password="+password
        window.location.href=url
    }
}
